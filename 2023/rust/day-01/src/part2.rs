use crate::custom_error::AocError;

pub fn process(input: &str) -> miette::Result<String, AocError> {
    let output: u32 = input.lines().map(process_line).sum::<u32>();

    Ok(output.to_string())
}

fn process_line(line: &str) -> u32 {
    let mut it = (0..line.len()).filter_map(|index| {
        let reduced_line = &line[index..];
        let result = if reduced_line.starts_with("one") {
            '1'
        } else if reduced_line.starts_with("two") {
            '2'
        } else if reduced_line.starts_with("three") {
            '3'
        } else if reduced_line.starts_with("four") {
            '4'
        } else if reduced_line.starts_with("five") {
            '5'
        } else if reduced_line.starts_with("six") {
            '6'
        } else if reduced_line.starts_with("seven") {
            '7'
        } else if reduced_line.starts_with("eight") {
            '8'
        } else if reduced_line.starts_with("nine") {
            '9'
        } else {
            reduced_line.chars().next().unwrap()
        };

        result.to_digit(10)
    });
    let first = it.next().expect("should be a number");

    match it.last() {
        Some(num) => format!("{first}{num}"),
        None => format!("{first}{first}"),
    }
    .parse::<u32>()
    .expect("should be a valid number")
}

#[cfg(test)]
mod tests {
    use super::*;

    use rstest::rstest;

    #[rstest]
    #[case("two1nine", 29)]
    #[case("eightwothree", 83)]
    #[case("eighthree", 83)]
    #[case("xtwoone3four", 24)]
    #[case("4nineightseven2", 42)]
    #[case("zoneight234", 14)]
    #[case("7pqrstsixteen", 76)]
    fn line_test(#[case] line: &str, #[case] expected: u32) {
        assert_eq!(expected, process_line(line))
    }

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "two1nine
        eightwothree
        eighthree
        xtwoone3four
        4nineightseven2
        zoneight234
        7pqrstsixteen";

        assert_eq!(
            (29 + 83 + 83 + 24 + 42 + 14 + 76).to_string(),
            process(input)?
        );
        Ok(())
    }
}
