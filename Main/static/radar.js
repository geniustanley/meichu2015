Chart.defaults.global = {
	// Boolean - Whether to animate the chart
    animation: true,

    // Number - Number of animation steps
    animationSteps: 60,

    // String - Animation easing effect
    // Possible effects are:
    // [easeInOutQuart, linear, easeOutBounce, easeInBack, easeInOutQuad,
    //  easeOutQuart, easeOutQuad, easeInOutBounce, easeOutSine, easeInOutCubic,
    //  easeInExpo, easeInOutBack, easeInCirc, easeInOutElastic, easeOutBack,
    //  easeInQuad, easeInOutExpo, easeInQuart, easeOutQuint, easeInOutCirc,
    //  easeInSine, easeOutExpo, easeOutCirc, easeOutCubic, easeInQuint,
    //  easeInElastic, easeInOutSine, easeInOutQuint, easeInBounce,
    //  easeOutElastic, easeInCubic]
    animationEasing: "easeOutQuart",

    // Boolean - If we should show the scale at all
    showScale: true,

    // Boolean - If we want to override with a hard coded scale
    scaleOverride: false,

    // ** Required if scaleOverride is true **
    // Number - The number of steps in a hard coded scale
    scaleSteps: null,
    // Number - The value jump in the hard coded scale
    scaleStepWidth: null,
    // Number - The scale starting value
    scaleStartValue: null,

    // String - Colour of the scale line
    scaleLineColor: "rgba(255,255,255,0.75)",

    // Number - Pixel width of the scale line
    scaleLineWidth: 1,

    // Boolean - Whether to show labels on the scale
    scaleShowLabels: true,

    // Interpolated JS string - can access value
    scaleLabel: "<%=value%>",

    // Boolean - Whether the scale should stick to integers, not floats even if drawing space is there
    scaleIntegersOnly: true,

    // Boolean - Whether the scale should start at zero, or an order of magnitude down from the lowest value
    scaleBeginAtZero: false,

    // String - Scale label font declaration for the scale label
    scaleFontFamily: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",

    // Number - Scale label font size in pixels
    scaleFontSize: 12,

    // String - Scale label font weight style
    scaleFontStyle: "normal",

    // String - Scale label font colour
    scaleFontColor: "#666",

    // Boolean - whether or not the chart should be responsive and resize when the browser does.
    responsive: true,

    // Boolean - whether to maintain the starting aspect ratio or not when responsive, if set to false, will take up entire container
    maintainAspectRatio: true,

    // Boolean - Determines whether to draw tooltips on the canvas or not
    showTooltips: true,

    // Function - Determines whether to execute the customTooltips function instead of drawing the built in tooltips (See [Advanced - External Tooltips](#advanced-usage-custom-tooltips))
    customTooltips: false,

    // Array - Array of string names to attach tooltip events
    tooltipEvents: ["mousemove", "touchstart", "touchmove"],

    // String - Tooltip background colour
    tooltipFillColor: "rgba(0,0,0,0.8)",

    // String - Tooltip label font declaration for the scale label
    tooltipFontFamily: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",

    // Number - Tooltip label font size in pixels
    tooltipFontSize: 14,

    // String - Tooltip font weight style
    tooltipFontStyle: "normal",

    // String - Tooltip label font colour
    tooltipFontColor: "#fff",

    // String - Tooltip title font declaration for the scale label
    tooltipTitleFontFamily: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",

    // Number - Tooltip title font size in pixels
    tooltipTitleFontSize: 14,

    // String - Tooltip title font weight style
    tooltipTitleFontStyle: "bold",

    // String - Tooltip title font colour
    tooltipTitleFontColor: "#fff",

    // Number - pixel width of padding around tooltip text
    tooltipYPadding: 6,

    // Number - pixel width of padding around tooltip text
    tooltipXPadding: 6,

    // Number - Size of the caret on the tooltip
    tooltipCaretSize: 8,

    // Number - Pixel radius of the tooltip border
    tooltipCornerRadius: 6,

    // Number - Pixel offset from point x to tooltip edge
    tooltipXOffset: 10,

    // String - Template string for single tooltips
    tooltipTemplate: "<%if (label){%><%=label%>: <%}%><%= value %>",

    // String - Template string for multiple tooltips
    multiTooltipTemplate: "<%= value %>",

    // Function - Will fire on animation progression.
    onAnimationProgress: function(){},

    // Function - Will fire on animation completion.
    onAnimationComplete: function(){}
}


var data = {
    labels: ["0 ~ 4", "5 ~ 9", "10 ~ 14", "15 ~ 19", "20 ~ 24", "25 ~ 29", "30 ~ 34", "35 ~39", "40 ~ 44", "45 ~ 49", "50 ~ 54", "55 ~ 59", "60 ~ 64", "65 ~ 69", "70 +"],
    datasets: [
        {
            label: "東區",
            fillColor: "rgba(233, 30, 99, 0.4)",
            strokeColor: "rgba(220,220,220,1)",
            pointColor: "rgba(220,220,220,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(220,220,220,1)",
            data: [65, 59, 90, 81, 56, 55, 40, 70, 30, 29, 90, 12, 28, 70, 78]
        },
        {
            label: "安平區",
            fillColor: "rgba(238,255,65,0.4)",
            strokeColor: "rgba(151,187,205,1)",
            pointColor: "rgba(151,187,205,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(151,187,205,1)",
            data: [28, 48, 40, 19, 96, 27, 100, 50, 14, 23, 54, 23, 12, 64, 23]
        }
    ]
};

var data2 = [
	[12, 13, 14, 15, 16, 29, 18, 19, 20, 29, 22, 30, 24, 25, 26],
	[22, 23, 24, 20, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
	[32, 33, 34, 35, 36, 37, 29, 39, 40, 41, 42, 43, 20, 45, 46],
	[42, 43, 44, 45, 100, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56],
	[52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 100, 64, 65, 66],
	[62, 63, 64, 65, 100, 67, 68, 59, 70, 71, 72, 73, 30, 75, 76]
]

// Get context with jQuery - using jQuery's .get() method.
var ctx = $("#myChart").get(0).getContext("2d");
// This will get the first returned node in the jQuery collection.
var myRadarChart = new Chart(ctx).Radar(data, {
	angleLineColor : "rgba(255, 255, 255, 0.3)",
	pointLabelFontColor : "rgb(255, 255, 255)",
	pointLabelFontSize : 15,
});

var cur = 0;

$('#2003').click(function() {
	if(cur == 0) {
		for(i = 0; i < 15; i++)
			myRadarChart.datasets[0].points[i].value = data2[0][i];
		cur = 1;
	}
	else {
		for(i = 0; i < 15; i++)
			myRadarChart.datasets[1].points[i].value = data2[0][i];
		cur = 0;
	}
	myRadarChart.update();
})

$('#2004').click(function() {
	if(cur == 0) {
		for(i = 0; i < 15; i++)
			myRadarChart.datasets[0].points[i].value = data2[1][i];
		cur = 1;
	}
	else {
		for(i = 0; i < 15; i++)
			myRadarChart.datasets[1].points[i].value = data2[1][i];
		cur = 0;
	}
	myRadarChart.update();
})

$('#2005').click(function() {
	if(cur == 0) {
		for(i = 0; i < 15; i++)
			myRadarChart.datasets[0].points[i].value = data2[2][i];
		cur = 1;
	}
	else {
		for(i = 0; i < 15; i++)
			myRadarChart.datasets[1].points[i].value = data2[2][i];
		cur = 0;
	}
	myRadarChart.update();
})

$('#2006').click(function() {
	if(cur == 0) {
		for(i = 0; i < 15; i++)
			myRadarChart.datasets[0].points[i].value = data2[3][i];
		cur = 1;
	}
	else {
		for(i = 0; i < 15; i++)
			myRadarChart.datasets[1].points[i].value = data2[3][i];
		cur = 0;
	}
	myRadarChart.update();
})

$('#2007').click(function() {
	if(cur == 0) {
		for(i = 0; i < 15; i++)
			myRadarChart.datasets[0].points[i].value = data2[4][i];
		cur = 1;
	}
	else {
		for(i = 0; i < 15; i++)
			myRadarChart.datasets[1].points[i].value = data2[4][i];
		cur = 0;
	}
	myRadarChart.update();
})

$('#2008').click(function() {

	if(cur == 0) {
		for(i = 0; i < 15; i++)
			myRadarChart.datasets[0].points[i].value = data2[5][i];
		cur = 1;
	}
	else {
		for(i = 0; i < 15; i++)
			myRadarChart.datasets[1].points[i].value = data2[5][i];
		cur = 0;
	}
	myRadarChart.update();
})