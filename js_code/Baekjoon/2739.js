const readline = require('readline')
const rl = readline.createInterface({
  input: Process.stdin,
  output: Process.stdout,
})

rl.on('line', line => {
  const N = parseInt(line)
  rl.close()
})


rl.on('close', () => {
  for (let i = 1; i < 10; i ++) {
    console.log(`${N} * ${i} = ${N*i}`)
  }
})