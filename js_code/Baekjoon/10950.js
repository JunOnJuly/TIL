const T = require('readline')

const t = T.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let N

t.on('line', line => {
    N = parseInt(line)
}).on('close', () => {
    for (let i = 0; i < N; i++) {
        let readline = require('readline')
        let rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout,
        })

        let dataInput = []

        rl.on('line', line => {
            dataInput = line.split(' ').map((num) => {
                parseInt(num)
            })
        }).on('close', () => {
            console.log(dataInput[0] + dataInput[1])
        })
    }
})