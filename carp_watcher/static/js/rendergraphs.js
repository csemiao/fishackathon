liveData = [];
var initialized = false;
var currentStream;
var margin = 40;
var containerHeight;
//Fit to screen
var w = $(window).width();
// var h = $('liveGraph').height() - 2* margin;
var h,
    minDate,
    maxDate,
    xScale,
    yScale;

function initGraphContainer() {
    containerHeight = $(window).height()/3;
    $('liveGraph').height(containerHeight);
    h = containerHeight;
    initGraph();
}

function initGraph() {
    if (initialized) {
        update();
    } else {
//axis sizes
        xScale = d3.time.scale()
            .domain([minDate, maxDate])
            .range([margin, w]);

        yScale = d3.scale.linear()
            .domain([0, 15])
            .range([h, 0]);

        var xAxis = d3.svg.axis()
                .scale(xScale)
                .tickFormat(d3.time.format("%Y-%m-%d")),
            yAxis = d3.svg.axis()
                .scale(yScale)
                .orient("left");
// Define the div for the tooltip
        var tooltip = d3.select(".liveGraph").append("div")
            .attr("class", "tooltip")
            .style("opacity", 0);
        var format = d3.time.format("%Y-%m-%d");
        var dateFn = function (d) {
            return format.parse(d.key)
        };

//Create Graph element
        svg = d3.select(".liveGraph")
            .append("svg")
            .attr("class", "graph")
            .attr("width", "100%")
            .attr("height", "100%")
            .attr("viewBox", "0 0 " + (w + 2 * margin) + " " + (h + 2 * margin))
            .attr("preserveAspectRatio", "xMinYMin meet");

        svg.selectAll("circle")
            .data(liveData,
                function (d) {
                    return d.key;
                })
            .enter()
            .append("circle")
            .attr("class", "datapoint")
            .attr("fill", "dodgerblue")
            .attr("cx", function (d) {
                return xScale(d.key);
            })
            .attr("cy", function (d) {
                return (h - d.value);
            })
            .attr("title", function (d) {
                return d.key;
            })
            .attr("r", 3)
            .on("mouseover", function (d) {
                tooltip.transition()
                    .duration(200)
                    .style("opacity", .9);
                tooltip.html("Day : " + d.key + "<br>" + "Temp: " + d.value / 10)
                    .style("left", (d3.event.pageX) + "px")
                    .style("top", (d3.event.pageY - 28) + "px");
            })
            .on("mouseout", function (d) {
                tooltip.transition()
                    .duration(500)
                    .style("opacity", 0);
            });

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

        initialized = true;
    }
}

function stringToDate(dateString) {
    var year = dateString.substring(0, 4);
    var month = dateString.substring(5, 7);
    var day = dateString.substring(8, 10);
    return new Date(year, month-1, day);
}

function getStreamData(streamName){
    console.log("getStreamData: " + streamName);
     $.ajax({
    url: "/tempdata/",
    type:"GET",
    data: {stream: streamName}
     }).done(function (data) {
         currentStream = streamName;
         liveData = [];
         for (var i = 0; i < data.length; i++) {
             // convert date strings to date objects
             data[i].key = stringToDate(data[i].key);
             data[i].value *= 10;
             liveData.push(data[i]);
         }
         minDate = liveData[0].key;
         maxDate = liveData[liveData.length - 1].key;
     });

}

function update() {
    console.log("updating");

    //get new data, recall endpoint;
     $.ajax({
    url: "/tempdata/",
    type:"GET",
    data: {stream: currentStream}
     }).done(function (data) {
         for (var i = 0; i < data.length; i++) {
             liveData.push(data[i]);
             console.log(data[i]);
         }
         minDate = liveData[0].key;
         maxDate = liveData[liveData.length - 1].key;
     });

    svg.selectAll("circle")
        .data(liveData)  // Update with new data HERE
        .transition()  // Transition from old to new data
        .duration(1000)  // Length of animation
        .each("start", function() {  // Start animation
            d3.select(this)  // 'this' means the current element
                .attr("fill", "orange")  // Change color
                .attr("r", 3);  // Change size
        })
        .delay(function(d, i) {
            return i / liveData.length * 500;  // Dynamic delay (i.e. each item delays a little longer)
        })
        //.ease("linear")  // Transition easing - default 'variable' (i.e. has acceleration), also: 'circle', 'elastic', 'bounce', 'linear'
        .each("end", function() {  // End animation
            d3.select(this)  // 'this' means the current element
                .transition()
                .duration(500)
                .attr("fill", "green")  // Change color
                .attr("r", 5)  // Change radius
                .transition()
                .duration(100)
                .attr("cx", function (d) { return xScale(d.key); })
                .attr("cy", function (d) { return (h - d.value); })
                .attr("title", function (d) {
                    return d[1];
                })
                .transition()
                .duration(500)
                .attr("r", 3)  // Change radius
                .attr("fill", "dodgerblue")  // Change color
        });
}




