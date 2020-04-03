const fs = require('fs');

if (process.argv.length !== 4) {
    console.log("Usage: node csv-to-json.js <csv-file> <json-file>");
}
const args = process.argv.splice(2);
const [inFile, outFile] = args;

const input = fs.readFileSync(inFile, 'UTF-8');
const lines = input.split(/[\r\n]+/);

let output = [];

const cap = (string) => string.replace(/^\w/, c => c.toUpperCase());

lines.forEach(line => {
    const parts = line.split(',');
    const type = parts[0];
    const name = parts[1];
    const period = parts[2];
    const semester = (parts[3] === "S1") ? "s1" :
        (parts[3] === "S2") ? "s2" : "year";
    const teacher = parts[4] + ', ' + parts[5];
    const room = parts[6];

    let entry = output.find((course) => course.name === name)
    if (entry == null) {
        output.push({
            name: name,
            type: type,
            [semester]: {
                [period]: [
                    {
                        name: name,
                        semester: cap(semester),
                        period: period,
                        teacher: teacher,
                        room: room
                    }
                ]
            }
        })
    } else {
        entry[semester] = entry[semester] || {}
        entry[semester][period] = entry[semester][period] || [];
        entry[semester][period].push({
            name: name,
            semester: cap(semester),
            period: period,
            teacher: teacher,
            room: room
        })
    }
})

fs.writeFileSync(outFile, JSON.stringify(output, null, 2));