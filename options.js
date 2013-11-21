var codecs = ["VP8","H264", "Theora", "H261", "H263"];
var levels = ["MUST", "SHOULD"];
var counter = 0;
function id(x) {
	return x;
    }
function times(a,b) { return a*b; }

for (var counter = 0; counter < Math.pow(3,codecs.length); ++counter) {
    var reqs = codecs.map(function(codec, i) {
	var x = Math.floor((counter / Math.pow(3, i))) % 3;
	if (x > 0) {
	    return {level: levels[x - 1], codec: codec };
	}
	return null;
    }).filter(id).reduce(function(a, cl) {
	if (!a[cl.level]) {
	    a[cl.level] = [];
	}
	a[cl.level].push(cl.codec);
	return a;
    }, {});

    var subsetCounts = levels.map(function(l) {
	if (!reqs.hasOwnProperty(l)) {
	    return 1;
	}
	return reqs[l].length;
    })
    var subsetCounter = subsetCounts.reduce(times, 1);
    for (; subsetCounter > 0; --subsetCounter) {
	console.log(levels.map(function(l, i) {
	    if (!reqs.hasOwnProperty(l)) {
		return null;
	    }
	    var x = Math.floor(subsetCounter / subsetCounts.slice(0, i).reduce(times, 1));
	    x %= subsetCounts[i];
	    
	    return l + ' implement ' + ((reqs[l].length > 1) ? (((x === 0) ? 'all' : (subsetCounts[i] - x).toString()) + ' of { ' + reqs[l].join(', ') + ' }') : reqs[l][0]);
	}).filter(id).join(' and '));
    }
}
