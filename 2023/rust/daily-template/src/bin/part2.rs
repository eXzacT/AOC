use {{crate_name}}::part2::process;
use miette::Context;

fn main() -> miette::Result<()> {
    let file = include_str!("../../../../day-01.txt");
    let result = process(file).context("process part 2")?;
    println!("{}", result);
    Ok(())
}