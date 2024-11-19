function main(): void {
  const test = process.env.TEST ?? "world";
  console.log(`Hello ${test}`)
}

main();
