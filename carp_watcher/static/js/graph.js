dataset1 = [
    {key: 0, value: 0},
    {key: 20, value: 50},
    {key: 40, value: 100},
    {key: 60, value: 150},
    {key: 80, value: 200},
    {key: 100, value: 250},
];

dataset2 = [
    {key: 0, value: 0},
    {key: 30, value: 70},
    {key: 50, value: 150},
    {key: 70, value: 200},
    {key: 90, value: 250},
    {key: 110, value: 300}
];

var key = function (d) {
    return d.key;
};

var margin = 40;
var w = 300;
var h = 400;

//axis sizes
var xScale = d3.scale.linear()
    .domain([0, w])
    .range([margin, w]);

var yScale = d3.scale.linear()
    .domain([0, h])
    .range([h, 0]);

var xAxis = d3.svg.axis().scale(xScale),
    yAxis = d3.svg.axis().scale(yScale).orient("left");


function init() {



//Create Graph element
     svg = d3.select("body")
        .append("svg")
         .attr("class", "graph")
        .attr("width", w + margin)
        .attr("height", h + margin);

    svg.selectAll("circle")
        .data(dataset1, key)
        .enter()
        .append("circle")
        .attr("cx", function (d) {
            return (d.key + margin);
        })
        .attr("cy", function (d) {
            return (h - d.value);
        })
        .attr("title", function (d) {
            return d.value;
        })
        .attr("r", 5);

    //Render x-axis
   svg.append("g")
        .attr("class", "axis x-axis")
        .attr("width", w)
        .attr("transform", "translate(0," + h + ")")
        .call(xAxis);

    //Render y-axis
    svg.append("g")
        .attr("class", "axis y-axis")
        .attr("height", h)
        .attr("transform", "translate(" + margin + ", 0)")
        .call(yAxis);
}


function update() {
    console.log("updating");

    //TODO: get new data, call endpoint;
    // var newData = ...

    svg.selectAll("circle")
        .data(dataset2)  // Update with new data HERE
        .transition()  // Transition from old to new data
        .duration(1000)  // Length of animation
        .each("start", function() {  // Start animation
            d3.select(this)  // 'this' means the current element
                .attr("fill", "yellow")  // Change color
                .attr("r", 5);  // Change size
        })
        .delay(function(d, i) {
            return i / dataset2.length * 500;  // Dynamic delay (i.e. each item delays a little longer)
        })
        //.ease("linear")  // Transition easing - default 'variable' (i.e. has acceleration), also: 'circle', 'elastic', 'bounce', 'linear'
        .each("end", function() {  // End animation
            d3.select(this)  // 'this' means the current element
                .transition()
                .duration(500)
                .attr("fill", "green")  // Change color
                .attr("r", 8)  // Change radius
                .transition()
                .duration(100)
                .attr("cx", function (d) { return d.key + margin; })
                .attr("cy", function (d) { return (h - d.value); })
                .attr("title", function (d) {
                    return d[1];
                })
                .transition()
                .duration(500)
                .attr("r", 5)  // Change radius
                .attr("fill", "black")  // Change color
        });
}

