var excel;
var filename = document.getElementById("filename").value;
var lisCalcUrl = document.getElementById("lis_calculation_url").value;
var nisCalcUrl = document.getElementById("nis_calculation_url").value;
var downloadFileUrl = document.getElementById("download_file_url").value;
var successUpload = document.getElementById("uploaded").value;

$( document ).ready(function() {
    document.getElementById("fileUpload").style.visibility = "visible";
    console.log( filename);
    if (filename != null){
        document.getElementById("uploaded").innerHTML = "Successfully uploaded:  "
                                                        + filename;
    }

});

function calculate_risk_score(){
    document.getElementById("results_download").style.display = "none";

    if(document.getElementById("selectScore").value == "lis"){
        calculate_location_impact_score();
    }
    else
        calculate_network_impact_score();
    document.getElementById("fileUpload").style.visibility = "hidden";

}

function calculate_location_impact_score() {
    document.getElementById("results").innerHTML = ""

    var table_title = "Location impact score of the 5-point scale and correspondence with the voxel-wise risk coefficient (ln(OR)*):"
    var table_scale1 = "scale 1 &#8594 score range –1.25 to 0.25"
    var table_scale2 = "scale 2 &#8594 score range 0.25 to 0.54"
    var table_scale3 = "scale 3 &#8594 score range 0.54 to 0.83"
    var table_scale4 = "scale 4 &#8594 score range 0.83 to 1.2"
    var table_scale5 = "scale 5 &#8594 score range 1.22 to 2.44"
    var table_notes = "* odds ratio"
    var table_notes2 = "Note: highest scores indicate increased probabilities for post-stroke cognitive impairement"

    console.log("ajax - location impact score")
    var csrfToken = readCookie("csrftoken")
    post_data = {'infarct_image': {'filename': filename }}
    console.log(csrfToken)

    $.ajax({
        type: 'POST',
        headers: {
                    'X-CSRFToken':csrfToken,
                },
        data: JSON.stringify(post_data),
        url: lisCalcUrl,

        success: function (response) {

            var result = JSON.parse(response["LocationImpactScore"])

            if (result == -100)
                alert("The infarct file does not have the same number of dimensions with the atlas!");
            else if (result == -200)
                alert("The infarct file does not have the same shape with the atlas!");
            else if (result == -300)
                alert("The infarct file does not have the same voxels dimension with the atlas!");
            else if (result == -400)
                alert("The infarct file is not binary!");
            else if (result == -500)
                alert("Please upload a file to proceed.");
            else{
                document.getElementById("results").innerHTML = "The Location Impact Score is: "
                + result
                +"<br/> "
                +"<br/> "
                +"<br/> " + (table_title.fixed()).fontsize(5)
                +"<br/> " + table_scale1.fixed()
                +"<br/>	" + table_scale2.fixed()
                +"<br/>	" + table_scale3.fixed()
                +"<br/>	" + table_scale4.fixed()
                +"<br/>	" + table_scale5.fixed()

                +"<br/> "
                +"<br/> "
                +"<br/> " + table_notes2.fixed()
                +"<br/> " + table_notes.fixed()

                ;
            }
        },

    })
}


function calculate_network_impact_score() {
    document.getElementById("results").innerHTML = ""

    console.log("ajax - network impact score")
    post_data = {'infarct_image': {'filename': filename }}

     var csrfToken = readCookie("csrftoken")

    $.ajax({
        type: 'POST',
        headers: {
            'X-CSRFToken':csrfToken,
        },
        data: JSON.stringify(post_data),
        url: nisCalcUrl,
        success: function (response) {
            var result = JSON.parse(JSON.stringify(response));
            console.log(result)

            if (result.NetworkImpactScore == -100)
                alert("The infarct file does not have the same number of dimensions with the atlas!");
            else if (result.NetworkImpactScore == -200)
                alert("The infarct file does not have the same shape with the atlas!");
            else if (result.NetworkImpactScore == -300)
                alert("The infarct file does not have the same voxels dimension with the atlas!");
            else if (result.NetworkImpactScore == -400)
                alert("The infarct file is not binary!");
            else if (result.NetworkImpactScore == -600){
                document.getElementById("results").innerHTML = "The Network Impact Score cannot be calculated!"
                + "<br/> "
                + "<br/> "
                + "The infarct does not overlap with any of the regions, "
                + "meaning that the patient has an isolated white matter or infratentorial infarct."
                ;
            }
            else if (result.NetworkImpactScore == -500)
                alert("Please upload a file to proceed.");
            else{
                document.getElementById("results").innerHTML = "The Network Impact Score is: "
                + result.Log
                + "<br/> "
                + " and corresponds to the "
                + (result.MaxIndexRegionName).fixed()
                + " region"
                + "<br/> "
                + "<br/> "
                + "<br/> "
                ;
                excel = result.ExcelFilename
                download_file();
            }
        },

    })
}

function download_file(){
    document.getElementById("results_download").style.display = "block";
    document.getElementById("results_download").innerHTML = "Do you want to download the results?"
    + "<br/> "
    + "<br/> "
    ;
    document.getElementById("downloadButton").style.display = "";
}

function downloadFunction(){
    post_data = {'ExcelFilename': excel }
    var csrfToken = readCookie("csrftoken")
    $.ajax({
        type: 'POST',
        headers: {
                'X-CSRFToken':csrfToken,
            },
        data: JSON.stringify(post_data),
        url: downloadFileUrl,
        success: function (response) {

            var jsonInfo = JSON.parse(response.InfoFile)
            var jsonFilename = JSON.parse(JSON.stringify(response.Filename))
            var jsonExcelFilename = JSON.parse(JSON.stringify(response.ExcelFilename))
            var createXLSLFormatObj = [];
            var xlsRows = [];
            var xlsHeader = [jsonFilename, "Network Impact Score"];


            for(var i=0; i<Object.keys(jsonInfo["Impact Score"]).length; i++){
                objRows = {
                        jsonFilename: jsonInfo[jsonFilename][i],
                        "Impact Score": jsonInfo["Impact Score"][i]
                        }
                xlsRows.push(objRows);
            }

            createXLSLFormatObj.push(xlsHeader);
            $.each(xlsRows, function(index, value) {
              var innerRowData = [];
              $("tbody").append('<tr><td>' + value.jsonFilename + '</td><td>' + value.ImpactScore + '</td></tr>');
              $.each(value, function(ind, val) {
                innerRowData.push(val);
              });
              createXLSLFormatObj.push(innerRowData);
            });

            var filename = jsonExcelFilename;
            var ws_name = "scores";

            if (typeof console !== 'undefined') console.log(new Date());
            var wb = XLSX.utils.book_new(),
              ws = XLSX.utils.aoa_to_sheet(createXLSLFormatObj);

            XLSX.utils.book_append_sheet(wb, ws, ws_name);

            if (typeof console !== 'undefined') console.log(new Date());
            XLSX.writeFile(wb, filename);
            if (typeof console !== 'undefined') console.log(new Date());
        },

    })
}

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}
