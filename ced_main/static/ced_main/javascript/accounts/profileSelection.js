function LoadOffices() {

    optionlist = [];
    appofflist = [];

    var ag = document.getElementById('AgencyID');

    var strag = ag.options[ag.selectedIndex].text;

    var fld = document.getElementById('Field_OfficeID');
    var strfld = fld.options[fld.selectedIndex].value;

    var appoff = document.getElementById('id_Approving_Official');
    var strappoff = appoff.options[appoff.selectedIndex].value;

    if (strag !== "---------") {
        for (var i = 0; i < fld.length; i++) {
            var fldval = fld.options[i].value;
            var fldtext = fld.options[i].text;

            fullfldlist.push([fldval, fldtext]);
        }

        for (var i = 0; i < appoff.length; i++) {
            var appoffval = appoff.options[i].value;
            var appofftext = appoff.options[i].text;

            fullappofflist.push([appoffval, appofftext])
        }

        for (var i = 0; i < fld.length; i++) {
            var option = document.createElement("option");
            var fldtxt = fld.options[i].text;
            fldval = fld.options[i].value;
            fldtxt1 = fldtxt.split(", ")[2];

            if (fldval === "---Select an Office---") {
                optionlist.push([fldval, fldtxt]);
            }

            if (fldtxt1 === strag) {
                optionlist.push([fldval, fldtxt]);
            }

            if (fullfldlist[i][0] === "DEMONSTRATION USER ACCESS ONLY") {
                optionlist.push([fullfldlist[i][0], fullfldlist[i][1]]);
            }
        }

        for (var i = 0; i < appoff.length; i++) {
            var option = document.createElement("option");
            var appofftxt = appoff.options[i].text;
            appoffval = appoff.options[i].value;
            appofftxt1 = appofftxt.split(", ")[2];

            if (appofftxt === "---Select an Approving Official---") {
                appofflist.push([appoffval, appofftxt]);
            }

            if (appofftxt1 !== undefined) {
                appofftxt1 = appofftxt1.split(": ")[1];
            }

            if (appofftxt1 === strag) {
                appofflist.push([appoffval, appofftxt]);
            }


            if (strfld == 'Oregon Soil and Water Conservation District' & appoffval == 'Jeff_Everett'){
                appofflist = [];
                appofflist.push([appoffval, appofftxt]);
            }

            if (strfld == 'Oregon Department of Fish and Wildlife' & appoffval == 'LeeFosterODFW'){
                appofflist = [];
                appofflist.push([appoffval, appofftxt]);
            }

            if (strag === 'Bureau of Land Management' & appoffval == 'Vickiherren'){
                appofflist = [];
                appofflist.push([appoffval, appofftxt]);
            }

            if (strfld == 'Montana Department of Natural Resources and Conservation' & appoffval == 'jamie.mcfadden'){
                appofflist = [];
                appofflist.push([appoffval, appofftxt]);
            }

            if (strfld == 'Oregon Dept of State Lands' & appoffval == 'DSL'){
                appofflist = [];
                appofflist.push([appoffval, appofftxt]);
            }


        }
        if (strfld === "---Select an Approving Official---") {
            appofflist = [];
            for (var i = 0; i < fullappofflist.length; i++) {
                if (fullappofflist[i][1] === "---Select an Approving Official---") {
                    appofflist.push([fullappofflist[i][0], fullappofflist[i][1]]);
                }
                if (fullappofflist[i][0] === "Lief_Wiechman") {
                    appofflist.push([fullappofflist[i][0], fullappofflist[i][1]]);
                }
                appoffvelsel = "Lief_Wiechman";
            }

        }
    }


    if (strag === "---------") {
        for (var i = 0; i < fld.length; i++) {
            var fldval = fld.options[i].value;
            var fldtext = fld.options[i].text;
            fullfldlist.push([fldval, fldtext]);
        }

        for (var i = 0; i < appoff.length; i++) {
            var appoffval = appoff.options[i].value;
            var appofftext = appoff.options[i].text;
            fullappofflist.push([appoffval, appofftext]);
        }

        for (var i = 0; i < fld.length; i++) {
            var option = document.createElement("option");
            var fldtxt = fld.options[i].text;
            fldval = fld.options[i].value;
            fldtxt1 = fldtxt.split(", ")[2];

            if (fldtxt === "---Select an Agency---") {
                optionlist.push([fldval, fldtxt]);
            }
        }

        for (var i = 0; i < appoff.length; i++) {
            var option = document.createElement("option");
            var appofftxt = appoff.options[i].text;
            appoffval = appoff.options[i].value;
            appofftxt1 = appofftxt.split(", ")[2];

            if (appofftxt === "---Select an Agency---") {
                appofflist.push([appoffval, appofftxt]);
            }

        }

    }

    //Erase the current full list and build a new one//
    $('#Field_OfficeID').empty();
    for (var j = 0; j < optionlist.length; j++) {
        var option = document.createElement("option");
        option.text = optionlist[j][1];
        option.value = optionlist[j][0];
        fld.appendChild(option);
    }


    $('#id_Approving_Official').empty();
    for (var j = 0; j < appofflist.length; j++) {
        var option = document.createElement("option");

        option.text = appofflist[j][1];
        option.value = appofflist[j][0];

        appoff.appendChild(option);
    }

    if (strfld > "") {
        fld.value = strfld;
    }
    if (strappoff > "") {
        appoff.value = strappoff;
    }
}

function LoadAppOffs() {

    appofflist = [];

    var ag = document.getElementById('AgencyID');
    var strag = ag.options[ag.selectedIndex].text;
    var fld = document.getElementById('Field_OfficeID');
    var strfld = fld.options[fld.selectedIndex].value;

    var appoff = document.getElementById('id_Approving_Official');

    var strappoff = "Lief_Wiechman";

    if (appoff.selectedIndex > 0)
        strappoff = appoff.options[appoff.selectedIndex].value;


    var updatelist = 0;

    var applimit = fullappofflist.length;

    for (var k = 0; k < applimit; k++) {
        if (strfld === "DEMONSTRATION USER ACCESS ONLY" || strfld === "Congress" || appoff === "") {
            updatelist = 1;
            appofflist = [];
            for (var i = 0; i < fullappofflist.length; i++) {

                if (fullappofflist[i][1] === "---Select an Approving Official---") {
                    appofflist.push([fullappofflist[i][0], fullappofflist[i][1]]);
                }
                if (fullappofflist[i][0] === "Lief_Wiechman") {
                    appofflist.push([fullappofflist[i][0], fullappofflist[i][1]]);
                }
                appoffvelsel = "Lief_Wiechman";
            }
        }

        if (strag === "---------") {
            updatelist = 1;
            for (var j = 0; j < fld.length; j++) {
                var fldval = fld.options[j].value;
                var fldtext = fld.options[j].text;
                fullfldlist.push([fldval, fldtext]);
            }

            for (var jj = 0; jj < appoff.length; jj++) {
                var appoffval = appoff.options[jj].value;
                var appofftext = appoff.options[jj].text;
                fullappofflist.push([appoffval, appofftext]);
            }

            for (var jjj = 0; jjj < appoff.length; jjj++) {
                var option = document.createElement("option");
                var appofftxt = appoff.options[jjj].text;
                appoffval = appoff.options[jjj].value;

                if (appofftxt === "---Select an Agency---") {
                    appofflist.push([appoffval, appofftxt]);
                }
            }

        }
    }

    if (updatelist === 1) {
        $('#id_Approving_Official').empty();
        for (var j = 0; j < appofflist.length; j++) {
            var option = document.createElement("option");

            option.text = appofflist[j][1];
            option.value = appofflist[j][0];
            appoff.appendChild(option);
        }

        if (strappoff > "") {
            appoff.value = strappoff;
        }
    }
}

function UpdateOffices() {

    optionlist = [];
    appofflist = [];

    var ag = document.getElementById('AgencyID');
    var strag = ag.options[ag.selectedIndex].text;
    var fld = document.getElementById('Field_OfficeID');
    var strfld = fld.options[fld.selectedIndex].value;
    var appoff = document.getElementById('id_Approving_Official');

    var strappoff = "Lief_Wiechman";
    if (appoff.selectedIndex > 0)
        strappoff = appoff.options[appoff.selectedIndex].value;

    var offvelsel = "";
    var appoffvelsel = "";

    if (strag !== "---------") {
        for (var i = 0; i < fullfldlist.length; i++) {
            var option = document.createElement("option");
            var fldtxt = fullfldlist[i][1];
            var fldval = fullfldlist[i][0];
            var fldtxt1 = fldtxt.split(", ")[2];

            if (fldval === "---Select an Office---") {
                optionlist.push([fldval, fldtxt]);
            }

            if (fldtxt1 === strag) {
                optionlist.push([fldval, fldtxt]);
            }

            if (fullfldlist[i][0] === "DEMONSTRATION USER ACCESS ONLY") {
                optionlist.push([fullfldlist[i][0], fullfldlist[i][1]]);
            }

        }

        for (var i = 0; i < fullappofflist.length; i++) {
            var option = document.createElement("option");
            var appofftxt = fullappofflist[i][1];
            appoffval = fullappofflist[i][0];
            appofftxt1 = appofftxt.split(", ")[2];

            if (appofftxt === "---Select an Approving Official---") {
                appofflist.push([appoffval, appofftxt]);
            }

            if (appofftxt1 !== undefined & strag !== "State") {
                appofftxt1 = appofftxt1.split(": ")[1];
            }

            if (appofftxt1 === strag) {
                appofflist.push([appoffval, appofftxt]);
            }

        }

        if (appofflist.length === 1 & strag !== "State") {
            if (optionlist.length === 2) {
                offvelsel = "DEMONSTRATION USER ACCESS ONLY";
            }

            for (var i = 0; i < fullappofflist.length; i++) {
                if (fullappofflist[i][0] === "Lief_Wiechman") {
                    appofflist.push([fullappofflist[i][0], fullappofflist[i][1]]);
                }
                appoffvelsel = "Lief_Wiechman";
            }

        }
    }

    if (strag === "---------") {

        for (var i = 0; i < fullfldlist.length; i++) {
            var option = document.createElement("option");
            var fldtxt = fullfldlist[i][1];
            var fldval = fullfldlist[i][0];
            var fldtxt1 = fldtxt.split(", ")[2];

            if (fldtxt === "---Select an Agency---") {
                optionlist.push([fldval, fldtxt]);
            }

        }

        for (var i = 0; i < fullappofflist.length; i++) {
            var option = document.createElement("option");
            var appofftxt = fullappofflist[i][1];
            appoffval = fullappofflist[i][0];
            appofftxt1 = appofftxt.split(", ")[2];

            if (appofftxt === "---Select an Agency---") {
                appofflist.push([appoffval, appofftxt]);
            }

        }
    }


    //Erase the current full list and build a new one//
    $('#Field_OfficeID').empty();
    for (var j = 0; j < optionlist.length; j++) {
        var option = document.createElement("option");
        option.text = optionlist[j][1];
        option.value = optionlist[j][0];
        fld.appendChild(option);
    }

    $('#id_Approving_Official').empty();
    for (var j = 0; j < appofflist.length; j++) {
        var option = document.createElement("option");

        option.text = appofflist[j][1];
        option.value = appofflist[j][0];
        appoff.appendChild(option);
    }

    if (offvelsel > "") {
        fld.value = offvelsel;
    }

    if (appoffvelsel > "") {
        appoff.value = appoffvelsel;
    }

}

function UpdateAppOff() {

    optionlist = [];
    appofflist = [];

    var ag = document.getElementById('AgencyID');
    var strag = ag.options[ag.selectedIndex].text;
    var fld = document.getElementById('Field_OfficeID');
    var strfld = fld.options[fld.selectedIndex].value;
    var appoff = document.getElementById('id_Approving_Official');

    var strappoff = "Lief_Wiechman";
    if (appoff.selectedIndex > 0)
        strappoff = appoff.options[appoff.selectedIndex].value;

    var offvelsel = "";
    var appoffvelsel = "Lief_Wiechman";

    for (var i = 0; i < fullappofflist.length; i++) {
        var option = document.createElement("option");
        var appofftxt = fullappofflist[i][1];
        appoffval = fullappofflist[i][0];
        appofftxt1 = appofftxt.split(", ")[2];
        appofftxt2 = appofftxt.split(", ")[3];

        if (appofftxt === "---Select an Approving Official---" && i < 2) {
            appofflist.push([appoffval, appofftxt]);
        }

        if (appofftxt1 !== undefined) {
            appofftxt1 = appofftxt1.split(": ")[1];
        }

        if (appofftxt2 !== undefined) {
            appofftxt2 = appofftxt2.split(": ")[1];
        }

        if (strag === "State"||strag === "Private"||strag === "Conservation District"||strag === "Nongovernmental Organization") {
            if (appofftxt1 === strag && appofftxt2 === strfld) {
                appofflist.push([appoffval, appofftxt]);
            }
        } else {
            if (appofftxt1 === strag) {
                appofflist.push([appoffval, appofftxt]);
            }
        }
    }


    if (appofflist.length === 0) {
        if (strag === "Bureau of Land Management")
            appoffvelsel = "Vickiherren";
        else if (strfld === "Montana Department of Natural Resources and Conservation"){
            appoffvelsel = "jamie.mcfadden";
        }else if (strfld === "Oregon Soil and Water Conservation District"){
            appoffvelsel = "Jeff_Everett";
        }else if (strfld === "'Oregon Department of Fish and Wildlife"){
            appoffvelsel = 'LeeFosterODFW';
        }else if (strfld === "Oregon Dept of State Lands"){
            appoffvelsel = "DSL";
        }else{
            appoffvelsel = "Lief_Wiechman";
        }

        appofflist = [];

        for (var i = 0; i < fullappofflist.length; i++) {
            if (fullappofflist[i][1] === "---Select an Approving Official---") {
                appofflist.push([fullappofflist[i][0], fullappofflist[i][1]]);
            }
            if (fullappofflist[i][0] === appoffvelsel) {
                appofflist.push([fullappofflist[i][0], fullappofflist[i][1]]);
            }
        }
    }


    if (strfld === "DEMONSTRATION USER ACCESS ONLY" || strfld === "Congress") {
        appofflist = [];

        for (var i = 0; i < fullappofflist.length; i++) {
            if (fullappofflist[i][1] === "---Select an Approving Official---") {
                appofflist.push([fullappofflist[i][0], fullappofflist[i][1]]);
            }
            if (fullappofflist[i][0] === "Lief_Wiechman") {
                appofflist.push([fullappofflist[i][0], fullappofflist[i][1]]);
            }
            appoffvelsel = "Lief_Wiechman";
        }

    }

    $('#id_Approving_Official').empty();
    for (var j = 0; j < appofflist.length; j++) {
        var option = document.createElement("option");

        option.text = appofflist[j][1];
        option.value = appofflist[j][0];
        appoff.appendChild(option);
    }

    if (appoffvelsel > "") {
        appoff.value = appoffvelsel;
    }

}
