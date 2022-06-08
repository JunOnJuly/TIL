const readNum = require('readline')

const rn = readNum.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let T

rn.on('line', line => {
    T = parseInt(line)
    rn.close()
}).on('close', line => {
    const readNums = require('readline')

    const rns = readNums.createInterface({
        input: process.stdin,
        output: process.stdout,
    })

    let dataInput = []

    rns.on('line', line => {
        dataInput.push(line.split(' ').map((data) => {
            return parseInt(data)
            })
        )
    })