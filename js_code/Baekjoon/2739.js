const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

let N

rl.on('line', line => {
  N = parseInt(line)
  rl.close()
})


rl.on('close', () => {
  for (let i = 1; i < 10; i ++) {
    console.log(`${N} * ${i} = ${N * i}`)
  }
})