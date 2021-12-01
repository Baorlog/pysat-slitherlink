var row = 5, col = 5;
var slitherContainer = "#slitherlink-container"
var slither = "#slitherlink"
var slitherMatrix = [];

$(document).ready(() => {
    generateSlither(row, col);

    $("#generate").click(() => {
        row = $("#size-row").val();
        col = $("#size-col").val();
        generateSlither(row, col);
    });

    $("#solve").click(() => {
        solve();
    })
})

const generateSlither = (row, col) => {

    $(slither).html("");
    $(slither).css("width", col*59+7);

    for(let i = 0; i < 2*row+1; i++) {
        if(i % 2) {
            slitherMatrix.push([]);
        }
        for(let j = 0; j < 2*col+1; j++) {
            let x = parseInt(i/2);
            let y = parseInt(j/2);
            if(i % 2) {
                if(j % 2) {
                    // let x = parseInt(i/2);
                    // let y = parseInt((j-1)/2);
                    slitherMatrix[x].push(-1);
                    $(slither).append($("<div>", {class: "cell", id: `c-${x}-${y}`}).click(() => {
                        let cellNextVal = getCellNextVal(x, y);
                        if(cellNextVal === -1) {
                            $(`#c-${x}-${y}`).html("");
                        }
                        else {
                            $(`#c-${x}-${y}`).html("" + cellNextVal);
                        }
                        slitherMatrix[x][y] = cellNextVal;
                    }));
                }
                else {
                    $(slither).append($("<div>", {class: "vertical", id: `e-${(row+1)*col + y*row + x + 1}`}));
                }
            }
            else {
                if(j % 2) {
                    $(slither).append($("<div>", {class: "horizontal", id: `e-${x*col + y + 1}`}));
                }
                else {
                    $(slither).append($("<div>", {class: "dot"}))
                }
            }
        }
    }
}

const getCellNextVal = (i, j) => {
    if (slitherMatrix[i][j] === 3) {
        return -1;
    }
    else {
        return parseInt(slitherMatrix[i][j]) + 1
    }
}

const solve = async () => {
    let input = {
        "slitherlink": []
    };
    for(let i = 0; i < slitherMatrix.length; i++) {
        let line = slitherMatrix[i];
        let newLine = ""
        for(let j = 0; j < line.length; j++) {
            if(line[j] === -1) {
                newLine += ".";
            }
            else {
                newLine += "" + line[j];
            }
            if(j < line.length - 1) {
                newLine += " ";
            }
        }
        input["slitherlink"].push(newLine);
    }
    
    let response = await fetch('/solve', {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(input)
    });

    let body = await response.json();

    if(body['success']) {
        $("#time").html(body["time"] + " (ms)");
        $("#clause").html(body["clause"] + " clauses.");
        $("#loop").html(body["loop"] + " loops.");
        $("#variable").html(body["var"] + " variables.");
    
        let solution = body["solution"];
        console.log(solution);
        for(let i = 0; i < solution.length; i++) {
            if(solution[i] > 0) {
                $(`#e-${solution[i]}`).addClass("connected");
            }
        }
    }
    else {
        alarm("UNSAT");
    }

}