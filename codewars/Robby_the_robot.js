/**
 * Created by abnerzheng on 16/2/13.
 */

function getCommands(field, power) {
    // insert awesome code here
    function varify(location) {
        if (location < 0 || location >= l) {
            return -1;
        } else {
            return location;
        }
    }

    function goForward(location) {
        return varify(location + l);
    }

    function goDown(location) {
        return varify(location - l);
    }

    function goRight(location) {
        return varify(location + 1);
    }

    function goLeft(location) {
        return varify(location - 1);
    }

    function State(location, path) {
        this.location = location;
        this.path = path;
        return this;
    }

    var l = Number(Math.sqrt(field.length));
    var count = 0;
    var queue = []; //广度优先搜索
    var visited = {};
    var location = field.indexOf('S');
    visited[location] = 1;
    var temp;
    queue.push(new State(location, []));

    while (count < power && queue.length) {
        var current_state = queue.shift();
        if ((temp = goUp(current_state.location)) != -1 && !(temp in visited)) {
            var path = current_state.path.push('')
            if(field[temp] == 'T'){
                return
            }
        }
    }

}

console.log(getCommands('S#.##...T', 20))