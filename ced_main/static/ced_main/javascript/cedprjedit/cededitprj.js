
function LoadLists(ListName, ListTitle, ListID) {

  var list
  var Control;
  var Control1;
  var Outputlist
  var cnt

  Outputlist = ListTitle

  cnt = 0
  list = document.getElementsByName(ListName)

  for(var i=0; i<list.length;i++) {
    if (document.getElementsByName(ListName)[i].checked) {
      
      Control = document.getElementsByName(ListName)[i].parentNode.innerHTML;
      Control1 = Control.split(">");
      Control2 = String(Control1[1])
      Control2 = Control2.replace(/[\n\r]/g, '');
      Control2 = Control2.substr(1);

      if (cnt == 0){
        Outputlist =  Outputlist + Control2
        cnt = cnt + 1
      }
      else {
        Outputlist = Outputlist + ", " + Control2
      }
    }
  }

  document.getElementById(ListID).innerHTML = Outputlist

}


 function SelectCounties(){
    
    var Control
    var Control1
    var UpdateControl
    var UpdateControl1
    var UpdateNum
    var UpdateNum1
    var UpdateNum2
    var Outputlist = "" 
    var CountState   
    var State
    var countyval
    var countyvallabel
    var innerhtm
    var list = document.getElementsByName('State_Value') 
    var updatelist = document.getElementsByName('County_Value') 
    var updatelist1 = []
    var labels

    var optionlist = []

    var u = 0

    

    for(var j=0; j<updatelist.length;j++) {
        UpdateControl = updatelist[j].parentNode.innerHTML;
        UpdateControl1 = UpdateControl.split(">")[1];
        UpdateControl1 = UpdateControl1.replace(/[\n\r]/g, '');
        UpdateControl1 = UpdateControl1.substr(1);

        updatelist1.push(UpdateControl1)
        countyval = 'id_County_Value_' + (u)
        document.getElementById(countyval).style.display = "none";
        var cnty = document.getElementById("county")
        cnty.getElementsByTagName("li")[u].style.display="none";
        u = u + 1
    }

    for(var i=0; i<list.length;i++) {
        if (list[i].checked) {

            Control = list[i].parentNode.innerHTML;
            Control1 = Control.split(">");
            Control2 = String(Control1[1])
            Control2 = Control2.replace(/[\n\r]/g, '');
            Control2 = Control2.substr(1);
            State = Control2
            State = State.substr(State.length - 2);

            var u = 0

            for(var j=0; j<updatelist1.length;j++) {
                CountState  = updatelist1[j].substr(updatelist1[j].length - 2);
                countyval = 'id_County_Value_' + (u)

                if (CountState == State) {
                    
                    document.getElementById(countyval).style.display = "inline-block";
                    var cnty = document.getElementById("county")
                    cnty.getElementsByTagName("li")[u].style.display="inline-block";

                }

                u = u + 1

            }

        }else{
            Control = list[i].parentNode.innerHTML;
            Control1 = Control.split(">");
            Control2 = String(Control1[1])
            Control2 = Control2.replace(/[\n\r]/g, '');
            Control2 = Control2.substr(1);
            State = Control2



            var u = 0

            for(var j=0; j<updatelist1.length;j++) {
                CountState  = updatelist1[j].substr(updatelist1[j].length - 2);
                countyval = 'id_County_Value_' + (u)
                if (CountState == State) {
                    document.getElementById(countyval).checked = false;
                }

                u = u + 1
            }
        }
    }

}

function SelectOtherRequired(){
  var list = document.getElementsByName('Method') 
  for(var i=0; i<list.length;i++) {
    if (list[i].checked) {

        Control = list[i].parentNode.innerHTML;
        Control1 = Control.split(">");
        Control2 = String(Control1[1])
        Control2 = Control2.replace(/[\n\r]/g, '');
        Control2 = Control2.substr(1);
        var Method = Control2

        if (Method == 'Other - Please specify in text box'){
          document.getElementById('methaster').style.display = "inline-block"
        }
    }else{
      Control = list[i].parentNode.innerHTML;
      Control1 = Control.split(">");
      Control2 = String(Control1[1])
      Control2 = Control2.replace(/[\n\r]/g, '');
      Control2 = Control2.substr(1);
      var Method = Control2

      if (Method == 'Other - Please specify in text box'){
          document.getElementById('methaster').style.display = "none"
      }
    }
  }
}

function SelectOtherRequiredEff(){
  var list = document.getElementsByName('Effectiveness_Statement') 
  for(var i=0; i<list.length;i++) {
    if (list[i].checked) {

        Control = list[i].parentNode.innerHTML;
        Control1 = Control.split(">");
        Control2 = String(Control1[1])
        Control2 = Control2.replace(/[\n\r]/g, '');
        Control2 = Control2.substr(1);
        var EffectivenessStatement = Control2

        if (EffectivenessStatement == 'Other - Please specify in text box'){
          document.getElementById('effreqlabel').style.display = "inline-block"
        }
    }else{
      Control = list[i].parentNode.innerHTML;
      Control1 = Control.split(">");
      Control2 = String(Control1[1])
      Control2 = Control2.replace(/[\n\r]/g, '');
      Control2 = Control2.substr(1);
      var Method = Control2

      if (Method == 'Other - Please specify in text box'){
          document.getElementById('effreqlabel').style.display = "none"
      }
    }
  }
}

function UpdateEndDateLabel(subact){

  var list = document.getElementsByName('Imp_Status') 
  var objlist = document.getElementsByName('Objective') 
  for(var i=0; i<list.length;i++) {
    if (list[i].checked) {
      var statusval = list[i].value
      if (statusval == 2){
        document.getElementById('endlabel').innerHTML = "Proposed End Date:"
        document.getElementById('id_Effective_Determined_0').style.display = "none";
        var efft = document.getElementById("EffectDeter")
        efft.getElementsByTagName("li")[0].style.display="none";
        document.getElementById('id_Effective_Determined_0').checked = false;

        if(subact == 'Conifer Removal (All Phases)' | subact == 'Fuels Management'){
          document.getElementById('id_Effective_Determined_1').style.display = "none";
          var efft = document.getElementById("EffectDeter")
          efft.getElementsByTagName("li")[1].style.display="none";
        }
      } else {
        if(subact == 'Vegetation Management / Habitat Enhancement' | subact == 'Riparian, Wet Meadow or Spring Restoration' | subact == 'Fuel Breaks' | subact == 'Annual Grass Treatments' | subact == 'Noxious Weed Treatments' | subact == 'Energy development reclamation with the goal of sagebrush restoration' | subact == 'Improved Grazing Practices (Rest, Rotation, Etc.)' | subact == 'Wild Equid Population Control' | subact == 'Wild Equid Gather' | subact == 'Translocation'){

          document.getElementById('endlabel').innerHTML = "End Date:"
          var listey = document.getElementsByName("End_Date_year")
          for(var k=0; k<listey.length;k++) {
            var ddl = document.getElementById("id_End_Date_year");
            var yearend = ddl.options[ddl.selectedIndex].value;
            timeelapsed = (new Date()).getFullYear() - yearend
            if (timeelapsed < 3){
              document.getElementById('id_Effective_Determined_0').style.display = "none";
              var efft = document.getElementById("EffectDeter")
              efft.getElementsByTagName("li")[0].style.display="none";
              document.getElementById('id_Effective_Determined_0').checked = false;
            } else {
              document.getElementById('id_Effective_Determined_0').style.display = "inline-block";
              var efft = document.getElementById("EffectDeter")
              efft.getElementsByTagName("li")[0].style.display="inline-block";
            }
          }
        } else if(subact == 'Conifer Removal (All Phases)' | subact == 'Fuels Management'){

          disp = 0
          for(var i=0; i<objlist.length;i++) {
            if (objlist[i].checked) {

                var Control = objlist[i].parentNode.innerHTML;
                var Control1 = Control.split(">");
                var Control2 = String(Control1[1])
                Control2 = Control2.replace(/[\n\r]/g, '');
                Control2 = Control2.substr(1);
                Objective = Control2

                var u = 0

                if (Objective == 'Reduce conifer cover (late Phase I, early Phase II) to prevent expansion and restore sagebrush habitat (local scale)' | Objective == 'Reduce woody fuels (slash) following conifer removal (local scale)'){
                  if (disp == 0){
                    disp = 1
                  } else {
                    disp = 2
                  }
                  document.getElementById('id_Effective_Determined_0').style.display = "inline-block";
                  var efft = document.getElementById("EffectDeter")
                  efft.getElementsByTagName("li")[0].style.display="inline-block";
                } else {
                  if (disp == 1){
                    disp = 2
                  } else {
                    disp = 3
                  }
                }
            }
          }

          if (disp == 0 | disp == 3){

            document.getElementById('id_Effective_Determined_0').style.display = "none";
            var efft = document.getElementById("EffectDeter")
            efft.getElementsByTagName("li")[0].style.display="none";
            document.getElementById('id_Effective_Determined_0').checked = false;

            document.getElementById('endlabel').innerHTML = "End Date:"
            var listey = document.getElementsByName("End_Date_year")
            for(var k=0; k<listey.length;k++) {
              var ddl = document.getElementById("id_End_Date_year");
              var yearend = ddl.options[ddl.selectedIndex].value;
              timeelapsed = (new Date()).getFullYear() - yearend
              if (timeelapsed < 3){
                document.getElementById('id_Effective_Determined_1').style.display = "none";
                var efft = document.getElementById("EffectDeter")
                efft.getElementsByTagName("li")[1].style.display="none";
                document.getElementById('id_Effective_Determined_1').checked = false;
              } else {
                document.getElementById('id_Effective_Determined_1').style.display = "inline-block";
                var efft = document.getElementById("EffectDeter")
                efft.getElementsByTagName("li")[1].style.display="inline-block";
              }
            }
          } else if (disp == 1 | disp == 2){
            document.getElementById('id_Effective_Determined_1').style.display = "none";
            var efft = document.getElementById("EffectDeter")
            efft.getElementsByTagName("li")[1].style.display="none";
            document.getElementById('id_Effective_Determined_1').checked = false;
          }
        } else {
          document.getElementById('id_Effective_Determined_0').style.display = "inline-block";
          var efft = document.getElementById("EffectDeter")
          efft.getElementsByTagName("li")[0].style.display="inline-block";
               
        }
      }
    }
  }
}

function SelectMethods(subact){
    
    if(subact == 'Vegetation Management / Habitat Enhancement' | subact == 'Fuels Management' | subact == 'Riparian, Wet Meadow or Spring Restoration'){

      var Control
      var Control1
      var UpdateControl
      var UpdateControl1
      var UpdateNum
      var UpdateNum1
      var UpdateNum2
      var Outputlist = "" 
      var CountState   
      var innerhtm
      var list = document.getElementsByName('Objective') 
      var updatelist = document.getElementsByName('Method') 
      var updatelist1 = []
      var labels

      var optionlist = []

      var u = 0
      for(var j=0; j<updatelist.length;j++) {
          UpdateControl = updatelist[j].parentNode.innerHTML;
          UpdateControl1 = UpdateControl.split(">")[1];
          UpdateControl1 = UpdateControl1.replace(/[\n\r]/g, '');
          UpdateControl1 = UpdateControl1.substr(1);

          updatelist1.push(UpdateControl1)
          methodval = 'id_Method_' + (u)
          document.getElementById(methodval).style.display = "none";
          var mthd = document.getElementById("methodbody")
          mthd.getElementsByTagName("li")[u].style.display="none";
          u = u + 1
      }

      for(var i=0; i<list.length;i++) {
          if (list[i].checked) {

              Control = list[i].parentNode.innerHTML;
              Control1 = Control.split(">");
              Control2 = String(Control1[1])
              Control2 = Control2.replace(/[\n\r]/g, '');
              Control2 = Control2.substr(1);
              Objective = Control2
              var u = 0

              // Set select boxes for subactivity Vegetation Management / Habitat Enhancement
              if(subact == 'Vegetation Management / Habitat Enhancement'){
                for(var j=0; j<updatelist1.length;j++) {
                  if (Objective == 'Increase native bunchgrass density and/or diversity (local scale)' | Objective == 'Improve and/or restore habitat quality through planting of sagebrush or other shrubs providing habitat (local scale)' | Objective == 'Increase forb density or diversity in understory (local scale)') {
                      for(var u=0; u<7; u++){
                        if(u == 0 | u == 1 | u == 5 | u == 6){
                          document.getElementById('id_Method_' + u).style.display = "inline-block";
                          var mthd = document.getElementById("methodbody")
                          mthd.getElementsByTagName("li")[u].style.display="inline-block";
                        }
                      }
                  }

                  if (Objective == 'Reduce or remove shrubs that may contribute to sagebrush habitat loss or degradation (local scale)'){
                      for(var u=0; u<7; u++){
                        if(u == 2 | u == 3 | u == 4){
                          document.getElementById('id_Method_' + u).style.display = "inline-block";
                          var mthd = document.getElementById("methodbody")
                          mthd.getElementsByTagName("li")[u].style.display="inline-block";
                        }
                      }
                  }

                  if (Objective == 'Other - Please specify in text box'){
                    for(var u=0; u<7; u++){
                        document.getElementById('id_Method_' + u).style.display = "inline-block";
                        var mthd = document.getElementById("methodbody")
                        mthd.getElementsByTagName("li")[u].style.display="inline-block";
                    }
                    document.getElementById('objaster').style.display = "inline-block"
                  }

                  document.getElementById('id_Method_7').style.display = "inline-block";
                  var mthd = document.getElementById("methodbody")
                  mthd.getElementsByTagName("li")[7].style.display="inline-block";

                  document.getElementById('id_Method_8').style.display = "inline-block";
                  var mthd = document.getElementById("methodbody")
                  mthd.getElementsByTagName("li")[8].style.display="inline-block";

                }
              }

              // Set select boxes for Fuels Management
              if(subact == 'Fuels Management'){
                for(var j=0; j<updatelist1.length;j++) {
                  if (Objective == 'Reduce woody fuels (slash) following conifer removal (local scale)') {
                      for(var u=0; u<5; u++){
                        if(u == 0 | u == 3 | u == 4){
                          document.getElementById('id_Method_' + u).style.display = "inline-block";
                          var mthd = document.getElementById("methodbody")
                          mthd.getElementsByTagName("li")[u].style.display="inline-block";
                        }
                      }
                  }

                  if (Objective == 'Reduce fuel continuity by thinning shrubs (local scale)') {
                      for(var u=0; u<5; u++){
                        if(u == 0 | u == 1 | u == 2){
                          document.getElementById('id_Method_' + u).style.display = "inline-block";
                          var mthd = document.getElementById("methodbody")
                          mthd.getElementsByTagName("li")[u].style.display="inline-block";
                        }
                      }
                  }

                  if (Objective == 'Other - Please specify in text box'){
                    for(var u=0; u<5; u++){
                        document.getElementById('id_Method_' + u).style.display = "inline-block";
                        var mthd = document.getElementById("methodbody")
                        mthd.getElementsByTagName("li")[u].style.display="inline-block";
                    }
                    document.getElementById('objaster').style.display = "inline-block"
                  }

                  document.getElementById('id_Method_5').style.display = "inline-block";
                  var mthd = document.getElementById("methodbody")
                  mthd.getElementsByTagName("li")[5].style.display="inline-block";

                  document.getElementById('id_Method_6').style.display = "inline-block";
                  var mthd = document.getElementById("methodbody")
                  mthd.getElementsByTagName("li")[6].style.display="inline-block";

                }
              }

              // Set select boxes for Riparian
              if(subact == 'Riparian, Wet Meadow or Spring Restoration'){
                for(var j=0; j<updatelist1.length;j++) {
                  if (Objective == 'Restore hydroligic function to floodplain/wet meadow (local scale)'){
                      for(var u=0; u<11; u++){
                        if(u == 0 | u == 2 | u == 3 | u == 4 | u == 6){
                          document.getElementById('id_Method_' + u).style.display = "inline-block";
                          var mthd = document.getElementById("methodbody")
                          mthd.getElementsByTagName("li")[u].style.display="inline-block";
                        }
                      }
                  }

                  if (Objective == 'Raise floodplain/wet meadow water table (local scale)'){
                      for(var u=0; u<11; u++){
                        if(u == 3 | u == 4 | u == 6){
                          document.getElementById('id_Method_' + u).style.display = "inline-block";
                          var mthd = document.getElementById("methodbody")
                          mthd.getElementsByTagName("li")[u].style.display="inline-block";
                        }
                      }
                  }

                  if (Objective == 'Restore riparian vegetation (local scale)'){
                      for(var u=0; u<11; u++){
                        if(u == 7 | u == 8 | u == 9 | u == 10){
                          document.getElementById('id_Method_' + u).style.display = "inline-block";
                          var mthd = document.getElementById("methodbody")
                          mthd.getElementsByTagName("li")[u].style.display="inline-block";
                        }
                      }
                  }

                  if (Objective == 'Reduce bank erosion to improve riparian function (local scale)'){
                      for(var u=0; u<11; u++){
                        if(u == 1 | u == 6 | u == 7 | u == 8 | u == 9 | u == 10){
                          document.getElementById('id_Method_' + u).style.display = "inline-block";
                          var mthd = document.getElementById("methodbody")
                          mthd.getElementsByTagName("li")[u].style.display="inline-block";
                        }
                      }
                  }

                  if (Objective == 'Spring enhancement (local scale)'){
                      for(var u=0; u<11; u++){
                        if(u == 7 | u == 8 | u == 9 | u == 10){
                          document.getElementById('id_Method_' + u).style.display = "inline-block";
                          var mthd = document.getElementById("methodbody")
                          mthd.getElementsByTagName("li")[u].style.display="inline-block";
                        }
                      }
                  }

                  if (Objective == 'Playa restoration (local scale)'){
                      for(var u=0; u<11; u++){
                        if(u == 5){
                          document.getElementById('id_Method_' + u).style.display = "inline-block";
                          var mthd = document.getElementById("methodbody")
                          mthd.getElementsByTagName("li")[u].style.display="inline-block";
                        }
                      }
                  }

                  if (Objective == 'Other - Please specify in text box'){
                    for(var u=0; u<11; u++){
                        document.getElementById('id_Method_' + u).style.display = "inline-block";
                        var mthd = document.getElementById("methodbody")
                        mthd.getElementsByTagName("li")[u].style.display="inline-block";
                    }
                    document.getElementById('objaster').style.display = "inline-block"
                  }

                  document.getElementById('id_Method_11').style.display = "inline-block";
                  var mthd = document.getElementById("methodbody")
                  mthd.getElementsByTagName("li")[11].style.display="inline-block";

                  document.getElementById('id_Method_12').style.display = "inline-block";
                  var mthd = document.getElementById("methodbody")
                  mthd.getElementsByTagName("li")[12].style.display="inline-block";

                }
              }

          }else{

              Control = list[i].parentNode.innerHTML;
              Control1 = Control.split(">");
              Control2 = String(Control1[1])
              Control2 = Control2.replace(/[\n\r]/g, '');
              Control2 = Control2.substr(1);
              Objective = Control2

              if (Objective == 'Other - Please specify in text box'){
                document.getElementById('objaster').style.display = "none"
              }

              // Unselect select boxes for subactivity Vegetation Management / Habitat Enhancement if objective is unchecked
              if(subact == 'Vegetation Management / Habitat Enhancement'){
                for(var j=0; j<updatelist1.length;j++) {
                  if (Objective == 'Increase native bunchgrass density and/or diversity (local scale)' | Objective == 'Improve and/or restore habitat quality through planting of sagebrush or other shrubs providing habitat (local scale)' | Objective == 'Increase forb density or diversity in understory (local scale)') {
                      for(var u=0; u<7; u++){
                        if(u == 0 | u == 1 | u == 5 | u == 6){
                          document.getElementById('id_Method_' + u).checked = false;
                        }
                      }
                  }

                  if (Objective == 'Reduce or remove shrubs that may contribute to sagebrush habitat loss or degradation (local scale)') {
                      for(var u=0; u<7; u++){
                        if(u == 2 | u == 3 | u == 4){
                          document.getElementById('id_Method_' + u).checked = false;
                        }
                      }
                  }

                  if (Objective == 'Other - Please specify in text box'){
                    document.getElementById('objaster').style.display = "none"
                  }

                }
              }

              // Set select boxes for Fuels Management
              if(subact == 'Fuels Management'){
                for(var j=0; j<updatelist1.length;j++) {
                  if (Objective == 'Reduce woody fuels (slash) following conifer removal (local scale)') {
                      for(var u=0; u<5; u++){
                        if(u == 0 | u == 3 | u == 4){
                          document.getElementById('id_Method_' + u).checked = false;
                        }
                      }
                  }

                  if (Objective == 'Reduce fuel continuity by thinning shrubs (local scale)') {
                      for(var u=0; u<5; u++){
                        if(u == 0 | u == 1 | u == 2){
                          document.getElementById('id_Method_' + u).checked = false;
                        }
                      }
                  }

                  if (Objective == 'Other - Please specify in text box'){
                    document.getElementById('objaster').style.display = "none"
                  }
                }
              }

              // Set select boxes for Riparian
              if(subact == 'Riparian, Wet Meadow or Spring Restoration'){
                for(var j=0; j<updatelist1.length;j++) {
                  if (Objective == 'Restore hydroligic function to floodplain/wet meadow (local scale)'){
                      for(var u=0; u<11; u++){
                        if(u == 0 | u == 2 | u == 3 | u == 4 | u == 6){
                          document.getElementById('id_Method_' + u).checked = false;
                        }
                      }
                  }

                  if (Objective == 'Raise floodplain/wet meadow water table (local scale)'){
                      for(var u=0; u<11; u++){
                        if(u == 3 | u == 4 | u == 6){
                          document.getElementById('id_Method_' + u).checked = false;
                        }
                      }
                  }

                  if (Objective == 'Restore riparian vegetation (local scale)'){
                      for(var u=0; u<11; u++){
                        if(u == 7 | u == 8 | u == 9 | u == 10){
                          document.getElementById('id_Method_' + u).checked = false;
                        }
                      }
                  }

                  if (Objective == 'Reduce bank erosion to improve riparian function (local scale)'){
                      for(var u=0; u<11; u++){
                        if(u == 1 | u == 6 | u == 7 | u == 8 | u == 9 | u == 10){
                          document.getElementById('id_Method_' + u).checked = false;
                        }
                      }
                  }

                  if (Objective == 'Spring enhancement (local scale)'){
                      for(var u=0; u<11; u++){
                        if(u == 7 | u == 8 | u == 9 | u == 10){
                          document.getElementById('id_Method_' + u).checked = false;
                        }
                      }
                  }

                  if (Objective == 'Playa restoration (local scale)'){
                      for(var u=0; u<11; u++){
                        if(u == 5){
                          document.getElementById('id_Method_' + u).checked = false;
                        }
                      }
                  }

                  if (Objective == 'Other - Please specify in text box'){
                      document.getElementById('objaster').style.display = "none"
                  }
                }
              }
          }
      }
    }

}


function SelectEffStat(subact){

  var Control
  var Control1
  var UpdateControl
  var UpdateControl1
  var UpdateNum
  var UpdateNum1
  var UpdateNum2
  var Outputlist = "" 
  var CountState   
  var innerhtm
  var list = document.getElementsByName('Effective_Determined') 
  var updatelist = document.getElementsByName('Effectiveness_Statement') 
  var updatelist1 = []
  var labels

  var optionlist = []

  var u = 0
  for(var j=0; j<updatelist.length;j++) {
      UpdateControl = updatelist[j].parentNode.innerHTML;
      UpdateControl1 = UpdateControl.split(">")[1];
      UpdateControl1 = UpdateControl1.replace(/[\n\r]/g, '');
      UpdateControl1 = UpdateControl1.substr(1);

      updatelist1.push(UpdateControl1)
      effstval = 'id_Effectiveness_Statement_' + (u)
      document.getElementById(effstval).style.display = "none";
      var mthd = document.getElementById("effstatbody")
      mthd.getElementsByTagName("li")[u].style.display="none";
      u = u + 1
  }

  for(var i=0; i<list.length;i++) {
    if (list[i].checked) {
      var EffectStat = list[i].value
      var u = 0

      // Set effectiveness statement select boxes for subactivity Conservation Easement
      if(subact == 'Conservation Easement'){
        for(var u=0; u<4; u++){
          if (EffectStat == 1 & (u == 0 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 2 & (u == 1 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 3 & (u == 2 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Land Acquisition
      if(subact == 'Land Acquisition'){
        for(var u=0; u<4; u++){
          if (EffectStat == 4 & (u == 0 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 5 & (u == 1 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 6 & (u == 2 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Fuel Breaks
      if(subact == 'Fuel Breaks'){
        for(var u=0; u<7; u++){
          if (EffectStat == 7 & (u == 0 | u == 6)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 8 & (u == 1 | u == 2 | u == 3 | u == 6)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 9 & (u == 4 | u == 5 | u == 6)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Conifer Removal (All Phases)
      if(subact == 'Conifer Removal (All Phases)'){
        for(var u=0; u<10; u++){
          if (EffectStat == 10 & (u == 1 | u == 9)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 11 & (u == 0 | u == 9)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 12 & (u == 2 | u == 3 | u == 4 | u == 5 | u == 6 | u == 9)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 13 & (u == 7 | u == 8 | u == 9)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Vegetation Management / Habitat Enhancement
      if(subact == 'Vegetation Management / Habitat Enhancement'){
        for(var u=0; u<10; u++){
          if (EffectStat == 14 & (u == 0 | u == 1 | u == 9)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 15 & (u == 2 | u == 3 | u == 4 | u == 5 | u == 9)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 16 & (u == 6 | u == 7 | u == 8 | u == 9)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Fuels Management
      if(subact == 'Fuels Management'){
        for(var u=0; u<10; u++){
          if (EffectStat == 17 & (u == 1 | u == 9)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 18 & (u == 0 | u == 9)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 19 & (u == 2 | u == 3 | u == 4 | u == 5 | u == 9)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 20 & (u == 6 | u == 7 | u == 8 | u == 9)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Annual Grass Treatments
      if(subact == 'Annual Grass Treatments'){
        for(var u=0; u<10; u++){
          if (EffectStat == 21 & (u == 0 | u == 1 | u == 9)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 22 & (u == 2 | u == 3 | u == 4 | u == 5 | u == 9)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 23 & (u == 6 | u == 7 | u == 8 | u == 9)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Noxious Weed Treatments
      if(subact == 'Noxious Weed Treatments'){
        for(var u=0; u<9; u++){
          if (EffectStat == 24 & (u == 0 | u == 8)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 25 & (u == 1 | u == 2 | u == 3 | u == 4 | u == 8)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 26 & (u == 5 | u == 6 | u == 7 | u == 8)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Riparian, Wet Meadow or Spring Restoration
      if(subact == 'Riparian, Wet Meadow or Spring Restoration'){
        for(var u=0; u<9; u++){
          if (EffectStat == 27 & (u == 0 | u == 8)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 28 & (u == 1 | u == 2 | u == 3 | u == 4 | u == 8)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 29 & (u == 5 | u == 6 | u == 7 | u == 8)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Energy development reclamation with the goal of sagebrush restoration
      if(subact == 'Energy development reclamation with the goal of sagebrush restoration'){
        for(var u=0; u<9; u++){
          if (EffectStat == 30 & (u == 0 | u == 1 | u == 8)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 31 & (u == 2 | u == 3 | u == 4 | u == 5 | u == 8)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 32 & (u == 6 | u == 7 | u == 8)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Area Closure
      if(subact == 'Area Closure'){
        for(var u=0; u<5; u++){
          if (EffectStat == 33 & (u == 0 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 34 & (u == 1 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 35 & (u == 2 | u == 3 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Improved Grazing Practices (Rest, Rotation, Etc.)
      if(subact == 'Improved Grazing Practices (Rest, Rotation, Etc.)'){
        for(var u=0; u<7; u++){
          if (EffectStat == 36 & (u == 0 | u == 6)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 37 & (u == 1 | u == 2 | u == 3 | u == 6)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 38 & (u == 4 | u == 5 | u == 6)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Road and Trail closure OR Rerouted Roads and/or Trails
      if(subact == 'Road and Trail closure' | subact == 'Rerouted Roads and/or Trails'){
        for(var u=0; u<5; u++){
          if ((EffectStat == 39 | EffectStat == 42) & (u == 0 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if ((EffectStat == 40 | EffectStat == 43) & (u == 1 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if ((EffectStat == 41 | EffectStat == 44) & (u == 2 | u == 3 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Powerline Retrofitting / Modification
      if(subact == 'Powerline Retrofitting / Modification'){
        for(var u=0; u<6; u++){
          if (EffectStat == 45 & (u == 0 | u == 5)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 46 & (u == 1 | u == 2 | u == 5)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 47 & (u == 3 | u == 4 | u == 5)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Powerline Burial OR Structure Removal
      if(subact == 'Powerline Burial' | subact == 'Structure Removal'){
        for(var u=0; u<4; u++){
          if ((EffectStat == 48 | EffectStat == 51) & (u == 0 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if ((EffectStat == 49 | EffectStat == 52) & (u == 1 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if ((EffectStat == 50 | EffectStat == 53) & (u == 2 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Fence Marking
      if(subact == 'Fence Marking'){
        for(var u=0; u<5; u++){
          if (EffectStat == 54 & (u == 0 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 55 & (u == 1 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 56 & (u == 2 | u == 3 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Fence Modification
      if(subact == 'Fence Modification'){
        for(var u=0; u<4; u++){
          if (EffectStat == 57 & (u == 0 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 58 & (u == 1 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 59 & (u == 2 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Fence Removal
      if(subact == 'Fence Removal'){
        for(var u=0; u<4; u++){
          if (EffectStat == 60 & (u == 0 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 61 & (u == 1 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 62 & (u == 2 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Wild Equid Population Control
      if(subact == 'Wild Equid Population Control'){
        for(var u=0; u<5; u++){
          if (EffectStat == 63 & (u == 0 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 64 & (u == 1 | u == 2 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 65 & (u == 3 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Wild Equid Gather
      if(subact == 'Wild Equid Gather'){
        for(var u=0; u<4; u++){
          if (EffectStat == 66 & (u == 0 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 67 & (u == 1 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 68 & (u == 2 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Translocation
      if(subact == 'Translocation'){
        for(var u=0; u<4; u++){
          if (EffectStat == 69 & (u == 0 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 70 & (u == 1 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }

          if (EffectStat == 71 & (u == 2 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).style.display = "inline-block";
              var effst = document.getElementById("effstatbody")
              effst.getElementsByTagName("li")[u].style.display="inline-block";
          }
        }
      }

    }else{
      var EffectStat = list[i].value
      // Set effectiveness statement select boxes for subactivity Conservation Easement
      if(subact == 'Conservation Easement'){
        for(var u=0; u<4; u++){
          if (EffectStat == 1 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 2 & (u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 3 & (u == 2)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Land Acquisition
      if(subact == 'Land Acquisition'){
        for(var u=0; u<4; u++){
          if (EffectStat == 4 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 5 & (u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 6 & (u == 2)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Fuel Breaks
      if(subact == 'Fuel Breaks'){
        for(var u=0; u<7; u++){
          if (EffectStat == 7 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 8 & (u == 1 | u == 2 | u == 3 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 9 & (u == 5)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Conifer Removal (All Phases)
      if(subact == 'Conifer Removal (All Phases)'){
        for(var u=0; u<10; u++){
          if (EffectStat == 10 & (u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 11 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 12 & (u == 2 | u == 3 | u == 4 | u == 5 | u == 6)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 13 & (u == 7 | u == 8)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Vegetation Management / Habitat Enhancement
      if(subact == 'Vegetation Management / Habitat Enhancement'){
        for(var u=0; u<10; u++){
          if (EffectStat == 14 & (u == 0 | u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 15 & (u == 2 | u == 3 | u == 4 | u == 5)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 16 & (u == 6 | u == 7 | u == 8)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Fuels Management
      if(subact == 'Fuels Management'){
        for(var u=0; u<10; u++){
          if (EffectStat == 17 & (u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 18 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 19 & (u == 2 | u == 3 | u == 4 | u == 5)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 20 & (u == 6 | u == 7 | u == 8)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Annual Grass Treatments
      if(subact == 'Annual Grass Treatments'){
        for(var u=0; u<10; u++){
          if (EffectStat == 21 & (u == 0 | u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 22 & (u == 2 | u == 3 | u == 4 | u == 5)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 23 & (u == 6 | u == 7 | u == 8)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Noxious Weed Treatments
      if(subact == 'Noxious Weed Treatments'){
        for(var u=0; u<9; u++){
          if (EffectStat == 24 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 25 & (u == 1 | u == 2 | u == 3 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 26 & (u == 5 | u == 6 | u == 7)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }
      
      // Set effectiveness statement select boxes for subactivity Riparian
      if(subact == 'Riparian, Wet Meadow or Spring Restoration'){
        for(var u=0; u<9; u++){
          if (EffectStat == 27 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 28 & (u == 1 | u == 2 | u == 3 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 29 & (u == 5 | u == 6 | u == 7)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Energy development reclamation with the goal of sagebrush restoration
      if(subact == 'Energy development reclamation with the goal of sagebrush restoration'){
        for(var u=0; u<9; u++){
          if (EffectStat == 30 & (u == 0 | u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 31 & (u == 2 | u == 3 | u == 4 | u == 5)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 32 & (u == 6 | u == 7)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Area Closure
      if(subact == 'Area Closure'){
        for(var u=0; u<5; u++){
          if (EffectStat == 33 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 34 & (u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 35 & (u == 2 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Improved Grazing Practices (Rest, Rotation, Etc.)
      if(subact == 'Improved Grazing Practices (Rest, Rotation, Etc.)'){
        for(var u=0; u<7; u++){
          if (EffectStat == 36 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 37 & (u == 1 | u == 2 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 38 & (u == 4 | u == 5)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Road and Trail closure OR Rerouted Roads and/or Trails
      if(subact == 'Road and Trail closure' | subact == 'Rerouted Roads and/or Trails'){
        for(var u=0; u<5; u++){
          if ((EffectStat == 39 | EffectStat == 42) & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if ((EffectStat == 40 | EffectStat == 43) & (u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if ((EffectStat == 41 | EffectStat == 44) & (u == 2 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Powerline Retrofitting / Modification
      if(subact == 'Powerline Retrofitting / Modification'){
        for(var u=0; u<6; u++){
          if (EffectStat == 45 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 46 & (u == 1 | u == 2)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 47 & (u == 3 | u == 4)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Powerline Burial OR Structure Removal
      if(subact == 'Powerline Burial' | subact == 'Structure Removal'){
        for(var u=0; u<4; u++){
          if ((EffectStat == 48 | EffectStat == 51) & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if ((EffectStat == 49 | EffectStat == 52) & (u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if ((EffectStat == 50 | EffectStat == 53) & (u == 2)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Fence Marking
      if(subact == 'Fence Marking'){
        for(var u=0; u<5; u++){
          if (EffectStat == 54 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 55 & (u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 56 & (u == 2 | u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Fence Modification
      if(subact == 'Fence Modification'){
        for(var u=0; u<4; u++){
          if (EffectStat == 57 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 58 & (u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 59 & (u == 2)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Fence Removal
      if(subact == 'Fence Removal'){
        for(var u=0; u<4; u++){
          if (EffectStat == 60 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 61 & (u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 62 & (u == 2)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Wild Equid Population Control
      if(subact == 'Wild Equid Population Control'){
        for(var u=0; u<5; u++){
          if (EffectStat == 63 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 64 & (u == 1 | u == 2)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 65 & (u == 3)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Wild Equid Gather
      if(subact == 'Wild Equid Gather'){
        for(var u=0; u<4; u++){
          if (EffectStat == 66 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 67 & (u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 68 & (u == 2)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }

      // Set effectiveness statement select boxes for subactivity Translocation
      if(subact == 'Translocation'){
        for(var u=0; u<4; u++){
          if (EffectStat == 69 & (u == 0)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 70 & (u == 1)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }

          if (EffectStat == 71 & (u == 2)) {
              document.getElementById('id_Effectiveness_Statement_' + u).checked = false;
          }
        }
      }
    }
  }

}

function ExpandNotes(notefield, notelabel) {
  var sign = document.getElementById(notelabel).innerHTML

  if (sign == '+'){
    document.getElementById(notefield).style.display = "inline-block";
    document.getElementById(notelabel).innerHTML = '-'
  } else {
    document.getElementById(notefield).style.display = "none";
    document.getElementById(notelabel).innerHTML = '+'
  }
  
}



function GoToEdit(Location) {
  var varloc = Location
  var loc = window.location.href
      document.body.scrollTop = document.documentElement.scrollTop = 0;
      
      document.getElementById('implementation').style.display = "none";
      document.getElementById('errorcheckdiv').style.display = "none";
      document.getElementById('dismaps').style.display = "none";
      document.getElementById('activityinfo').style.display = "none";

  if (varloc == "Activity"){
      document.getElementById('implementation').style.display = "none";
      document.getElementById('errorcheckdiv').style.display = "none";
      document.getElementById('dismaps').style.display = "none";
      document.getElementById('activityinfo').style.display = "inline-block";
      document.getElementById('sectype').innerHTML = "Step 3: Activity Information";

     window.history.pushState(loc,"CED Edit Effort", "?step=Activity");
  }


  if (varloc == 'Location'){
      document.getElementById('activityinfo').style.display = "none";
      document.getElementById('dismaps').style.display = "inline-block";
      document.getElementById('implementation').style.display = "none";
      document.getElementById('errorcheckdiv').style.display = "none";
      document.getElementById('sectype').innerHTML = "Step 2: Location Information";

      window.history.pushState(loc,"CED Edit Effort", "?step=Location");
  }

  if (varloc == 'Implementation'){
      document.getElementById('activityinfo').style.display = "none";
      document.getElementById('dismaps').style.display = "none";
      document.getElementById('implementation').style.display = "inline-block";
      document.getElementById('errorcheckdiv').style.display = "none";
      document.getElementById('sectype').innerHTML = "Step 4: Implementation Information";

      window.history.pushState(loc,"CED Edit Effort", "?step=Implementation");

      

        list = document.getElementsByName('Imp_Status')
        for(var i=0; i<list.length;i++) {
          if (document.getElementsByName('Imp_Status')[i].checked) {

            if (document.getElementsByName('Imp_Status')[i].value < 3){
                var str = "***REQUIRED*** For efforts not yet implemented, is there a high level of certainty that:";
                var result = str.fontcolor("red");
                document.getElementById('Part1Label').innerHTML = result;
                document.getElementById('Reas_Certain').style.display = "inline-block";
                document.getElementById('Legal_Authority').style.display = "inline-block";
                document.getElementById('Staff_Available').style.display = "inline-block";
                document.getElementById('Regulatory_Mech').style.display = "inline-block";
                document.getElementById('Compliance').style.display = "inline-block";
                document.getElementById('Vol_Incentives').style.display = "inline-block";

            }

            if (document.getElementsByName('Imp_Status')[i].value == 3){
                var str = "With your effort complete, no additional questions required for Part 1";
                document.getElementById('Part1Label').innerHTML = str;
                document.getElementById('Reas_Certain').style.display = "none";
                document.getElementById('Legal_Authority').style.display = "none";
                document.getElementById('Staff_Available').style.display = "none";
                document.getElementById('Regulatory_Mech').style.display = "none";
                document.getElementById('Compliance').style.display = "none";
                document.getElementById('Vol_Incentives').style.display = "none";

            }
          }
        }

        list = document.getElementsByName('Effective_Determined')
        var exists = 'No'
        for(var i=0; i<list.length;i++) {
          if (document.getElementsByName('Effective_Determined')[i].checked) {
            
            
            var effval = document.getElementsByName('Effective_Determined')[i].value
            if (effval == 1 | effval == 4 | effval == 10 | effval == 17 | effval == 33 | effval == 39 | effval == 42 | effval == 45 | effval == 48 | effval == 51 | effval == 54 | effval == 57 | effval == 60 | effval == 7 | effval == 11 | effval == 14 | effval == 18 | effval == 21 | effval == 24 | effval == 27 | effval == 30 | effval == 36 | effval == 63 | effval == 66 | effval == 69){
                exists = 'Yes'
              var str = "With your effort fully effective, no additional questions required for Part 2";
              document.getElementById('Part2Label').innerHTML = str;
              var str1 = 'Explain why the activity was deemed effective:';
              document.getElementById('Effect_Explained_Label').innerHTML = str1;
              document.getElementById('Part1Label').innerHTML = str;
              document.getElementById('Reduce_Threats').style.display = "none";
              document.getElementById('Incremental_Objectives').style.display = "none";
              document.getElementById('Quantifiable_Measures').style.display = "none";
              document.getElementById('AD_Strategy').style.display = "none";
            } else {
              exists = 'Yes'
              var str = "***REQUIRED*** For efforts not deemed effective (e.g. programs/actions only recently implemented), does the effort:";
              str = str.fontcolor("red");
              document.getElementById('Part2Label').innerHTML = str;
              var str1 = 'Explain why the activity is unlikely to be effective:';
              document.getElementById('Effect_Explained_Label').innerHTML = str1;
              document.getElementById('Reduce_Threats').style.display = "inline-block";
              document.getElementById('Incremental_Objectives').style.display = "inline-block";
              document.getElementById('Quantifiable_Measures').style.display = "inline-block";
              document.getElementById('AD_Strategy').style.display = "inline-block";
            }

            
          }
        }

        if (exists == 'No'){
          var str = "";
          document.getElementById('Part2Label').innerHTML = str;
          var str1 = 'Explain other effectiveness:';
          document.getElementById('Effect_Explained_Label').innerHTML = str1;
          document.getElementById('Reduce_Threats').style.display = "none";
          document.getElementById('Incremental_Objectives').style.display = "none";
          document.getElementById('Quantifiable_Measures').style.display = "none";
          document.getElementById('AD_Strategy').style.display = "none";
        }

  }

  if (varloc == 'Review'){
      window.history.pushState(loc,"CED Edit Effort", "?step=Review");
      document.getElementById('activityinfo').style.display = "none";
      // document.getElementById('disdocs').style.display = "none";
      document.getElementById('dismaps').style.display = "none";
      document.getElementById('implementation').style.display = "none";
      document.getElementById('errorcheckdiv').style.display = "inline-block";
      document.getElementById('sectype').innerHTML = "Step 5: Review/Error Check";
      
    // var loclists = [['WAFWA_Value', 'WAFWAs Selected: ', 'WAFWAList1'], ['Population_Value', 'Populations Selected: ', 'PopList1'], ['State_Value', 'States Selected: ', 'StateList1'], ['County_Value', 'Counties Selected: ', 'CountyList1']]

    var loclists = [['State_Value', 'States Selected: ', 'StateList1'], ['County_Value', 'Counties Selected: ', 'CountyList1']]
    
    var effnam = document.getElementById("id_Project_Name").value

    if(effnam == ''){
        document.getElementById('ActNameLab').style.color = "red"
        document.getElementById('effnamcolor').style.color = "red"
        document.getElementById('ActNameVal').value = ''
    }else{
        document.getElementById('ActNameLab').style.color = "black"
        document.getElementById('effnamcolor').style.color = "black"
        document.getElementById('ActNameVal').innerHTML = effnam
    }

    var stmnth = document.getElementById("id_Start_Date_month").value
    var stday = document.getElementById("id_Start_Date_day").value
    var styear = document.getElementById("id_Start_Date_year").value
    var strt = stmnth + "/" + stday + "/" + styear
    if(stmnth == 0 | stday == 0 | styear == 0){
        document.getElementById('StartDateLab').style.color = "red"
        document.getElementById('startcolor').style.color = "red"
    }else{
        document.getElementById('StartDateLab').style.color = "black"
        document.getElementById('startcolor').style.color = "black"
    }
    document.getElementById("StartSel").innerHTML = strt

    var fnmnth = document.getElementById("id_End_Date_month").value
    var fnday = document.getElementById("id_End_Date_day").value
    var fnyear = document.getElementById("id_End_Date_year").value
    var fnsh = fnmnth + "/" + fnday + "/" + fnyear

    if(fnmnth == 0 | fnday == 0 | fnyear == 0){
        document.getElementById('FinishDateLab').style.color = "red"
        document.getElementById('endcolor').style.color = "red"
    }else{
        document.getElementById('FinishDateLab').style.color = "black"
        document.getElementById('endcolor').style.color = "black"
    }

    document.getElementById('StartSel').innerHTML = strt
    document.getElementById('EndSel').innerHTML = fnsh

    if(subactiv == "Conservation Agreements (including but not limited to: CCAs, CCAAs, Farm Bill and other Incentive-based programs)" | subactiv == "Powerline Burial" | subactiv == "Fence Marking" | subactiv == "Fence Removal" | subactiv == "Improved Grazing Practices (Rest, Rotation, Etc.)" | subactiv == "Road and Trail closure"){

        if(document.getElementById('id_Metric_Value').value <= 0){
            document.getElementById('MetValLab').style.color = "red"
            document.getElementById('lab66').style.color = "red"
        }else{
            document.getElementById('MetValLab').style.color = "black"
            document.getElementById('lab66').style.color = "black"
        }

        document.getElementById('MetVal').innerHTML = document.getElementById('id_Metric_Value').value
    }

    if(tyacval == 'Spatial Project'){

        if(document.getElementById('id_Metric_Value').value <= 0){
            document.getElementById('MetValLab').style.color = "red"
            document.getElementById('lab66').style.color = "red"
        }else{
            document.getElementById('MetValLab').style.color = "black"
            document.getElementById('lab66').style.color = "black"
        }

        document.getElementById('MetVal').innerHTML = document.getElementById('id_Metric_Value').value

        if(document.getElementById('GISAC').innerHTML <= 0){
            document.getElementById('GISValLab').style.color = "red"
            document.getElementById('giscolor').style.color = "red"
        }else{
            document.getElementById('GISValLab').style.color = "black"
            document.getElementById('giscolor').style.color = "black"
        }

        var repAcre = document.getElementById('id_Metric_Value').value;
        repAcre = Math.round(repAcre)
        var GISAcre = document.getElementById('GISACVAL').innerHTML;
        GISAcre = Math.round(GISAcre)
        var AcreDiff = repAcre - GISAcre;
        if(GISAcre > 0){
          if(AcreDiff >= 0){
              var diffthan = "greater than"
          }else{
              var diffthan = "less than"
              AcreDiff = Math.abs(AcreDiff)
              var AcrePer = repAcre / GISAcre * 100;
              AcrePer = Math.round(AcrePer)
              AcrePer = AcrePer - 100
              AcrePer = Math.abs(AcrePer)
              if(AcrePer < 25 & AcrePer >= 1){
                a=1
              }else if(AcrePer >= 25){
                document.getElementById('GISValLab').style.color = "red"
                document.getElementById('giscolor').style.color = "red"
                document.getElementById('MetValLab').style.color = "red"
                document.getElementById('lab66').style.color = "red"
              }
              
          }
          

          
        }   

    }


    if(subactiv == "Vegetation Management / Habitat Enhancement" | subactiv == "Energy development reclamation with the goal of sagebrush restoration"){
        var stype = ""
        var st = document.getElementsByName('seeding_type')
        for(var i=0; i<st.length;i++) {
            if (document.getElementsByName("seeding_type")[i].checked) {
                stype = document.getElementsByName("seeding_type")[i].parentNode.innerHTML;
            }
        }
 
        if(stype == ""){
            stype2 = ""
        }else{
            stype1 = stype.split(">");
            stype2 = stype1[1]
            stype2 = String(stype2)
            stype2 = stype2.replace(/[\n\r]/g, '');
            stype2 = stype2.substr(1);
        }

        if(stype2 == ""){
            document.getElementById('SeedingTypeLab').style.color = "red"
            document.getElementById('seedtypelab').style.color = "red"
            
        }else{
            document.getElementById('SeedingTypeLab').style.color = "black"
            document.getElementById('seedtypelab').style.color = "black"
            
        }
        document.getElementById('SeedingTypeVal').innerHTML = stype2

        
    }

    // Mitigation validation
    var mittype = ""
    var mit = document.getElementsByName('mitigation')
    for(var i=0; i<mit.length;i++) {
        if (document.getElementsByName("mitigation")[i].checked) {
            mittype = document.getElementsByName("mitigation")[i].parentNode.innerHTML;
        }
    }

    if(mittype == ""){
          mittype2 = ""
      }else{
          mittype1 = mittype.split(">");
          mittype2 = mittype1[1]
          mittype2 = String(mittype2)
          mittype2 = mittype2.replace(/[\n\r]/g, '');
          mittype2 = mittype2.substr(1);
      }

    if(mittype2 == ""){
          document.getElementById('MitigationLab').style.color = "red"
          document.getElementById('pmitigationlab').style.color = "red"
      }else{
          document.getElementById('MitigationLab').style.color = "black"
          document.getElementById('pmitigationlab').style.color = "black"
      }

      document.getElementById('MitigationVal').innerHTML = mittype2

    if(activ == 'RESTORATION: Post-Disturbance and/or Habitat Enhancement'){
        var frtype = ""
        var fr = document.getElementsByName('post_fire')
        for(var i=0; i<fr.length;i++) {
            if (document.getElementsByName("post_fire")[i].checked) {
                frtype = document.getElementsByName("post_fire")[i].parentNode.innerHTML;
            }
        }

        if(frtype == ""){
            frtype2 = ""
        }else{
            frtype1 = frtype.split(">");
            frtype2 = frtype1[1]
            frtype2 = String(frtype2)
            frtype2 = frtype2.replace(/[\n\r]/g, '');
            frtype2 = frtype2.substr(1);
        }

        if(frtype2 > -1){
            document.getElementById('PostFireLab').style.color = "red"
            document.getElementById('pfirelab').style.color = "red"
        }else{
            document.getElementById('PostFireLab').style.color = "black"
            document.getElementById('pfirelab').style.color = "black"
        }

        document.getElementById('PostFireVal').innerHTML = frtype2

    }

    if(subactiv == "Powerline Burial"){
        var pl = document.getElementById('id_Type_of_Powerline')
        var plnum = pl.options[pl.selectedIndex].value;
        var pltypeval
        if(plnum == 'Distribution'){
            pltypeval = 'Distribution'
            document.getElementById('TypePowerLab').style.color = "black"
        }else if(plnum == 'Transmission'){
            pltypeval = 'Transmission'
            document.getElementById('TypePowerLab').style.color = "black"
        }else{
            pltypeval = ''
            document.getElementById('TypePowerLab').style.color = "red"
        }
        document.getElementById('TypePowerVal').innerHTML = pltypeval
    }

    if(subactiv == "Conservation Agreements (including but not limited to: CCAs, CCAAs, Farm Bill and other Incentive-based programs)"){
        
        var al = document.getElementById('id_Agreement_Length');
        var alval = al.options[al.selectedIndex].value;


        var agrlen = ""
        if(document.getElementById('id_Agreement_Length').value <= 0){
            document.getElementById('AgreeLenLab').style.color = "red"
            document.getElementById('agreelenlab').style.color = "red"

        }else{
            document.getElementById('AgreeLenLab').style.color = "black"
            document.getElementById('agreelenlab').style.color = "black"
            if(alval == 1){
                agrlen = '0-4 Years'
            }else if(alval == 2){
                agrlen = '5-9 Years'
            }else if(alval == 3){
                agrlen = '10-14 Years'
            }else if(alval == 4){
                agrlen = '15-19 Years'
            }else if(alval == 5){
                agrlen = '20-24 Years'
            }else if(alval == 6){
                agrlen = '25-29 Years'
            }else if(alval == 7){
                agrlen = '>=30 Years'
            }else if(alval == 8){
                agrlen = 'In Perpetuity'
            }
        }
        document.getElementById('AgreeLenVal').innerHTML = agrlen
 

        cnt = 0
        list = document.getElementsByName("Agreement_Penalty")
        var Outputlist = ""
        for(var i=0; i<list.length;i++) {
          if (document.getElementsByName("Agreement_Penalty")[i].checked) {
            Control = document.getElementsByName("Agreement_Penalty")[i].parentNode.innerHTML;
            Control1 = Control.split(">");
            Control2 = String(Control1[1])
            Control2 = Control2.replace(/[\n\r]/g, '');
            Control2 = Control2.substr(1);
            if (cnt == 0){
              Outputlist = Outputlist + Control2
              cnt = cnt + 1
            }
            else {
              Outputlist = Outputlist + ", " + Control2
            }
          }
        }

        if(Outputlist == ""){
            document.getElementById('AgreePenLab').style.color = "red"
            document.getElementById('agreepenlab').style.color = "red"
        }else{
            document.getElementById('AgreePenLab').style.color = "black"
            document.getElementById('agreepenlab').style.color = "black"
        }

        document.getElementById('AgreePenVal').innerHTML = Outputlist

        if(document.getElementById('id_CCAA_Num_Permit_Holders').value <= 0){
            document.getElementById('PerHoldLab').style.color = "red"
            document.getElementById('perholdcolor').style.color = "red"
        }else{
            document.getElementById('PerHoldLab').style.color = "black"
            document.getElementById('perholdcolor').style.color = "black"
        }
        document.getElementById('PerHoldVal').innerHTML = document.getElementById('id_CCAA_Num_Permit_Holders').value

    }

    if(tyacval != 'Non-Spatial Plan'){
        // Objective List
        var objlist = document.getElementsByName('Objective') 
        var objtxt = ""
        var cnt = 0
        var ObjectiveTextTest = 0
        for(var i=0; i<objlist.length;i++) {
            if (objlist[i].checked) {

                var Control = objlist[i].parentNode.innerHTML;
                var Control1 = Control.split(">");
                var Control2 = String(Control1[1])
                Control2 = Control2.replace(/[\n\r]/g, '');
                Control2 = Control2.substr(1);
                Objective = Control2
                if(cnt == 0){
                  objtxt = Objective
                  cnt = 1
                } else {
                  objtxt = objtxt + "; " + Objective
                }

                if(Objective == "Other - Please specify in text box"){
                  ObjectiveTextTest = 1
                }
            }

        }


        if (cnt == 0){
          document.getElementById('objreview').style.color = "red"
          document.getElementById('objcolor1').style.color = "red"
        } else {
          document.getElementById('ObjectiveList1').innerHTML = objtxt
          document.getElementById('objreview').style.color = "black"
          document.getElementById('objcolor1').style.color = "black"
        }

        var objexp = document.getElementById('id_Objectives_Desc').value;
        var objexplen = objexp.length;

        document.getElementById('ObjectiveSel1').innerHTML = ""

        if(ObjectiveTextTest == 1 | objexplen > 0){
            // Objective Description
            var objdesc = document.getElementById('id_Objectives_Desc').value
            document.getElementById('ObjectiveSel1').innerHTML = objdesc

              if(document.getElementById('id_Objectives_Desc').value == ""){
                 document.getElementById('ObjectiveLab').style.color = "red"
                 document.getElementById('objcolor').style.color = "red"
                 document.getElementById('objidsel').style.display = "inline-block";
              }else{

                  document.getElementById('ObjectiveLab').style.color = "black" 
                  document.getElementById('objcolor').style.color = "black" 
                  document.getElementById('objidsel').style.display = "inline-block";
              }
          }else{
            document.getElementById('ObjectiveLab').style.color = "black" 
            document.getElementById('objcolor').style.color = "black"
            document.getElementById('objidsel').style.display = "none";
          }

        
        // Method List
        var mthlist = document.getElementsByName('Method') 
        var mthtxt = ""
        var cnt = 0
        var mthTextTest = 0
        for(var i=0; i<mthlist.length;i++) {
            if (mthlist[i].checked) {

                var Control = mthlist[i].parentNode.innerHTML;
                var Control1 = Control.split(">");
                var Control2 = String(Control1[1])
                Control2 = Control2.replace(/[\n\r]/g, '');
                Control2 = Control2.substr(1);
                Method = Control2
                if(cnt == 0){
                  mthtxt = Method
                  cnt = 1
                } else {
                  mthtxt = mthtxt + "; " + Method
                }

                if(Method == "Other - Please specify in text box"){
                  mthTextTest = 1
                }
            }

        }

        if (cnt == 0){
          document.getElementById('mthreview').style.color = "red"
          document.getElementById('methodcolor').style.color = "red"
        } else {
          document.getElementById('MethodList1').innerHTML = mthtxt
          document.getElementById('mthreview').style.color = "black"
          document.getElementById('methodcolor').style.color = "black"
        }

        var metexp = document.getElementById('id_Methods_Explained').value;
        var metexplen = metexp.length;
        document.getElementById('MethodText1').innerHTML = ""
        if(mthTextTest == 1 | metexplen > 0){
          // Methods Description
          document.getElementById('MethodText1').innerHTML = document.getElementById('id_Methods_Explained').value

          if(document.getElementById('id_Methods_Explained').value == ""){
             document.getElementById('mthtxtreview').style.color = "red"
             document.getElementById('mtcolor').style.color = "red"
             document.getElementById('mthidsel1').style.display = "inline-block";
          }else{
              document.getElementById('mthtxtreview').style.color = "black" 
              document.getElementById('mtcolor').style.color = "black" 
              document.getElementById('mthidsel1').style.display = "inline-block";
          }
        } else {
          document.getElementById('mthtxtreview').style.color = "black" 
          document.getElementById('mtcolor').style.color = "black" 
          document.getElementById('mthidsel1').style.display = "none";
        }

        var checked = 0
        var ndereq = 0

        // Effectiveness Determination
        // If effectiveness determined is successful then hide and don't worry about 2nd set of PECE questions, otherwise show them
        var nyireq2nd = 0
        list = document.getElementsByName('Effective_Determined')
        var effval = 0
        var effexists = 0
        for(var i=0; i<list.length;i++) {
          if (document.getElementsByName('Effective_Determined')[i].checked) {
              try{
                effval = document.getElementsByName('Effective_Determined')[i].value
              } catch(err){
              }

              var selector = 'label[for=' + list[i].id + ']';
              var label = document.querySelector(selector);
              var text = label.innerHTML;
              var textsplit = text.split(">")[1]
              var Control2 = String(textsplit)
              Control2 = Control2.replace(/[\n\r]/g, '');
              Control2 = Control2.substr(1);

              if (effval == 1 | effval == 4 | effval == 10 | effval == 17 | effval == 33 | effval == 39 | effval == 42 | effval == 45 | effval == 48 | effval == 51 | effval == 54 | effval == 57 | effval == 60 | effval == 7 | effval == 11 | effval == 14 | effval == 18 | effval == 21 | effval == 24 | effval == 27 | effval == 30 | effval == 36 | effval == 63 | effval == 66 | effval == 69){
                document.getElementById('deemeffrev1').innerHTML = Control2
                document.getElementById('effstatcolor').style.color = "black"
                document.getElementById('deemeffrevlab').style.color = "black"
                effexists = 1
              } else if (effval > 0){
                nyireq2nd = 1
                document.getElementById('deemeffrev1').innerHTML = Control2
                document.getElementById('effstatcolor').style.color = "black"
                document.getElementById('deemeffrevlab').style.color = "black"
                effexists = 1
              } else {
                document.getElementById('deemeffrev1').innerHTML = ""
                document.getElementById('effstatcolor').style.color = "red"
                document.getElementById('deemeffrevlab').style.color = "red"
              }
          } 
        }

        if(effval == 0){
          document.getElementById('effstatcolor').style.color = "red"
          document.getElementById('deemeffrevlab').style.color = "red"
        }


        // Effectivenss Statements List
        var efflist = document.getElementsByName('Effectiveness_Statement') 
        var efftxt = ""
        var cnt = 0
        var effTextTest = 0
        for(var i=0; i<efflist.length;i++) {
            if (efflist[i].checked) {

                var Control = efflist[i].parentNode.innerHTML;
                var Control1 = Control.split(">");
                var Control2 = String(Control1[1])
                Control2 = Control2.replace(/[\n\r]/g, '');
                Control2 = Control2.substr(1);
                EffStat = Control2
                if(cnt == 0){
                  efftxt = EffStat
                  cnt = 1
                } else {
                  efftxt = efftxt + "; " + EffStat
                }

                if(EffStat == "Other - Please specify in text box"){
                  effTextTest = 1
                }
            }

        }

        if (cnt == 0){
          document.getElementById('effreview').style.color = "red"
          document.getElementById('effstatcolor').style.color = "red"
        } else {
          document.getElementById('EffectiveList1').innerHTML = efftxt
          document.getElementById('effreview').style.color = "black"
          document.getElementById('effstatcolor').style.color = "black"
        }

        var effexp = document.getElementById('id_Effective_Explained').value;
        var effexplen = effexp.length;
        document.getElementById('expeffrevrev').innerHTML = ""
        if(effTextTest == 1 | effexplen > 0){
          // Effectiveness Statement Description
          document.getElementById('expeffrevrev').innerHTML = document.getElementById('id_Effective_Explained').value

          if(document.getElementById('id_Effective_Explained').value == ""){
             document.getElementById('expeffrevlab').style.color = "red"
             document.getElementById('Effect_Explained_Label').style.color = "red"
             document.getElementById('effidsel1').style.display = "inline-block";
          }else{
              document.getElementById('expeffrevlab').style.color = "black" 
              document.getElementById('Effect_Explained_Label').style.color = "black" 
              document.getElementById('effidsel1').style.display = "inline-block";
          }
        } else {
          document.getElementById('expeffrevlab').style.color = "black" 
          document.getElementById('Effect_Explained_Label').style.color = "black" 
          document.getElementById('effidsel1').style.display = "none";
        }


    }



    document.getElementById('NotesSel').innerHTML = document.getElementById('id_Notes').value

    //Threats//
    cnt = 0
    list = document.getElementsByName("Threat")
    var Outputlist = ""
    for(var i=0; i<list.length;i++) {
      if (document.getElementsByName("Threat")[i].checked) {
        Control = document.getElementsByName("Threat")[i].parentNode.innerHTML;
        Control1 = Control.split(">");
        Control2 = String(Control1[1])
        Control2 = Control2.replace(/[\n\r]/g, '');
        Control2 = Control2.substr(1);
        if (cnt == 0){
          Outputlist = Outputlist + Control2
          cnt = cnt + 1
        }
        else {
          Outputlist = Outputlist + ", " + Control2
        }
      }
    }
   
    if(Outputlist == ""){
        document.getElementById('ThrCheckLab').style.color = "red"
        document.getElementById('thrtcolor').style.color = "red"
    }else{
        document.getElementById('ThrCheckLab').style.color = "black"
        document.getElementById('thrtcolor').style.color = "black"
    }


    document.getElementById('ThrCheckSel').innerHTML = Outputlist
    
    // document.getElementById('AgCon1').style.display = "none";
    // document.getElementById('ConEncr1').style.display = "none";
    // document.getElementById('OilGas1').style.display = "none";
    // document.getElementById('Fire1').style.display = "none";
    // document.getElementById('FeralEquids1').style.display = "none";
    // document.getElementById('ImpropGraze1').style.display = "none";
    // document.getElementById('Infra1').style.display = "none";
    // document.getElementById('Isolate1').style.display = "none";
    // document.getElementById('Mining1').style.display = "none";
    // document.getElementById('Invasive1').style.display = "none";
    // document.getElementById('Rec1').style.display = "none";
    // document.getElementById('SageLoss1').style.display = "none";
    // document.getElementById('UrbDevel1').style.display = "none";

    // var list = document.getElementsByName('Threat')
    // for(var i=0; i<list.length;i++) {
    //   if (list[i].checked) {
    //     Control = list[i].parentNode.innerHTML;
    //     Control1 = Control.split(">");
    //     Control2 = String(Control1[1])
    //     Control2 = Control2.replace(/[\n\r]/g, '');
    //     Control2 = Control2.substr(1);

    //     if (Control2 == "AGRICULTURAL CONVERSION (Tillage Risk)"){
    //         document.getElementById('AgCon1').style.display = "block";
    //         if(document.getElementById('id_Ag_Conversion_Explain').value > ""){
    //             document.getElementById('AgConLab').style.color = "black"
    //             document.getElementById('agcolor').style.color = "black"
    //         }else{
    //             document.getElementById('AgConLab').style.color = "red"
    //             document.getElementById('agcolor').style.color = "red"
    //         }
    //         document.getElementById('AgConSel').innerHTML = document.getElementById('id_Ag_Conversion_Explain').value
    //     }

    //     if (Control2 == "CONIFER ENCROACHMENT"){
    //         document.getElementById('ConEncr1').style.display = "block";
    //         if(document.getElementById('id_Conifer_Encroach_Explain').value > ""){
    //             document.getElementById('ConEncrLab').style.color = "black"
    //             document.getElementById('concolor').style.color = "black"
    //         }else{
    //             document.getElementById('ConEncrLab').style.color = "red"
    //             document.getElementById('concolor').style.color = "red" 
    //         }
    //         document.getElementById('AgConSel').innerHTML = document.getElementById('id_Conifer_Encroach_Explain').value
    //     }

    //     if (Control2 == "OIL &amp; GAS DEVELOPMENT"){
    //         document.getElementById('OilGas1').style.display = "block";
    //         if(document.getElementById('id_Oil_Gas_Explain').value > ""){
    //             document.getElementById('OilGasLab').style.color = "black"
    //             document.getElementById('oilcolor').style.color = "black"
    //         }else{
    //             document.getElementById('OilGasLab').style.color = "red" 
    //             document.getElementById('oilcolor').style.color = "red"
    //         }
    //         document.getElementById('OilGasSel').innerHTML = document.getElementById('id_Oil_Gas_Explain').value
    //     }

    //     if (Control2 == "FIRE"){
    //         document.getElementById('Fire1').style.display = "block";
    //         if(document.getElementById('id_Fire_Explain').value > ""){
    //             document.getElementById('FireLab').style.color = "black"
    //             document.getElementById('firecolor').style.color = "black"
    //         }else{
    //             document.getElementById('FireLab').style.color = "red" 
    //             document.getElementById('firecolor').style.color = "red"
    //         }
    //         document.getElementById('FireSel').innerHTML = document.getElementById('id_Fire_Explain').value  
    //     }

    //     if (Control2 == "FERAL EQUIDS"){
    //         document.getElementById('FeralEquids1').style.display = "block";
    //         if(document.getElementById('id_Feral_Equids_Explain').value > ""){
    //             document.getElementById('FeralEquidsLab').style.color = "black"
    //             document.getElementById('equcolor').style.color = "black"
    //         }else{
    //             document.getElementById('FeralEquidsLab').style.color = "red" 
    //             document.getElementById('equcolor').style.color = "red"
    //         }
    //         document.getElementById('FeralEquidsSel').innerHTML = document.getElementById('id_Feral_Equids_Explain').value
    //     }

    //     if (Control2 == "IMPROPER GRAZING / RANGE MANAGEMENT"){
    //         document.getElementById('ImpropGraze1').style.display = "block";
    //         if(document.getElementById('id_Improper_Grazing_Explain').value > ""){
    //             document.getElementById('ImpropGrazeLab').style.color = "black"
    //             document.getElementById('grazcolor').style.color = "black"
    //         }else{
    //             document.getElementById('ImpropGrazeLab').style.color = "red" 
    //             document.getElementById('grazcolor').style.color = "red"
    //         }
    //         document.getElementById('ImpropGrazeSel').innerHTML = document.getElementById('id_Improper_Grazing_Explain').value
    //     }

    //     if (Control2 == "INFRASTRUCTURE (Roads, Powerlines, Renewable Energy)"){
    //         document.getElementById('Infra1').style.display = "block";
    //         if(document.getElementById('id_Infrastructure_Explain').value > ""){
    //             document.getElementById('InfraLab').style.color = "black"
    //             document.getElementById('infracolor').style.color = "black"
    //         }else{
    //             document.getElementById('InfraLab').style.color = "red"
    //             document.getElementById('infracolor').style.color = "red" 
    //         }
    //         document.getElementById('InfraSel').innerHTML = document.getElementById('id_Infrastructure_Explain').value
    //     }

    //     if (Control2 == "ISOLATED / SMALL POPULATION SIZE"){
    //         document.getElementById('Isolate1').style.display = "block";
    //         if(document.getElementById('id_Isolated_Explain').value > ""){
    //             document.getElementById('IsolateLab').style.color = "black"
    //             document.getElementById('ipecolor').style.color = "black"
    //         }else{
    //             document.getElementById('IsolateLab').style.color = "red" 
    //             document.getElementById('ipecolor').style.color = "red"
    //         }
    //         document.getElementById('IsolateSel').innerHTML = document.getElementById('id_Isolated_Explain').value
    //     }

    //     if (Control2 == "MINING"){
    //         document.getElementById('Mining1').style.display = "block";
    //         if(document.getElementById('id_Mining_Explain').value > ""){
    //             document.getElementById('MiningLab').style.color = "black"
    //             document.getElementById('mincolor').style.color = "black"
    //         }else{
    //             document.getElementById('MiningLab').style.color = "red" 
    //             document.getElementById('mincolor').style.color = "red"
    //         }
    //         document.getElementById('MiningSel').innerHTML = document.getElementById('id_Mining_Explain').value
    //     }

    //     if (Control2 == "INVASIVES (Annual Grasses and Noxious Weeds)"){
    //         document.getElementById('Invasive1').style.display = "block"; 
    //         if(document.getElementById('id_Invasives_Explained').value > ""){
    //             document.getElementById('invascolor').style.color = "black"
    //             document.getElementById('InvasiveLab').style.color = "black"
    //         }else{
    //             document.getElementById('InvasiveLab').style.color = "red" 
    //             document.getElementById('invascolor').style.color = "red"
    //         }
    //         document.getElementById('InvasiveSel').innerHTML = document.getElementById('id_Invasives_Explained').value
    //     }

    //     if (Control2 == "RECREATION"){
    //         document.getElementById('Rec1').style.display = "block";
    //         if(document.getElementById('id_Recreation_Explain').value > ""){
    //             document.getElementById('RecLab').style.color = "black"
    //             document.getElementById('reccolor').style.color = "black"
    //         }else{
    //             document.getElementById('RecLab').style.color = "red" 
    //             document.getElementById('reccolor').style.color = "red"
    //         }
    //         document.getElementById('RecSel').innerHTML = document.getElementById('id_Recreation_Explain').value
    //     }

    //     if (Control2 == "SAGEBRUSH LOSS or DEGRADATION"){
    //         document.getElementById('SageLoss1').style.display = "block";
    //         if(document.getElementById('id_Sagebrush_Loss_Explain').value > ""){
    //             document.getElementById('SageLossLab').style.color = "black"
    //             document.getElementById('sagecolor').style.color = "black"
    //         }else{
    //             document.getElementById('SageLossLab').style.color = "red" 
    //             document.getElementById('sagecolor').style.color = "red"
    //         }
    //         document.getElementById('SageLossSel').innerHTML = document.getElementById('id_Sagebrush_Loss_Explain').value
    //     }
        
    //     if (Control2 == "URBAN DEVELOPMENT"){
    //         document.getElementById('UrbDevel1').style.display = "block"; 
    //         if(document.getElementById('id_Urban_Devel_Explain').value > ""){
    //             document.getElementById('UrbDevelLab').style.color = "black"
    //             document.getElementById('urbcolor').style.color = "black"
    //         }else{
    //             document.getElementById('UrbDevelLab').style.color = "red" 
    //             document.getElementById('urbcolor').style.color = "red"
    //         } 
    //         document.getElementById('UrbDevelSel').innerHTML = document.getElementById('id_Urban_Devel_Explain').value
    //     }
    //   }
    // }


    //Collaborators//
    cnt = 0
    list = document.getElementsByName("Collab_Party")
    var Outputlist = ""
    for(var i=0; i<list.length;i++) {
      if (document.getElementsByName("Collab_Party")[i].checked) {
        Control = document.getElementsByName("Collab_Party")[i].parentNode.innerHTML;
        Control1 = Control.split(">");
        Control2 = String(Control1[1])
        Control2 = Control2.replace(/[\n\r]/g, '');
        Control2 = Control2.substr(1);
        if (cnt == 0){
          Outputlist = Outputlist + Control2
          cnt = cnt + 1
        }
        else {
          Outputlist = Outputlist + ", " + Control2
        }
      }
    }


    if(Outputlist == ""){
        document.getElementById('ColCheckLab').style.color = "red"
        document.getElementById('colabcolor').style.color = "red"
    }else{
        document.getElementById('ColCheckLab').style.color = "black"
        document.getElementById('colabcolor').style.color = "black"
    }

    document.getElementById('ColCheckSel').innerHTML = Outputlist


    //Documentation//

    try{

        var myTableDiv = document.getElementById("docreview")

        try{
            myTableDiv.removeChild(myTableDiv.childNodes[0]);
        }catch(err){
        }
        var table = document.createElement('TABLE')
        var tableBody = document.createElement('TBODY')
        table.border = '1'
        table.appendChild(tableBody);
        var heading = new Array();
        heading[0] = "File Type"
        heading[1] = "Document Description"
        heading[2] = "Document Name"

        var docs = new Array()

        for (i = 0; i < 100; i++) {
            try{
                var ft = document.getElementById("id_form-" + i + "-File_Type")
                var ftsel = ft.options[ft.selectedIndex].value;
                var dd = document.getElementById("id_form-" + i + "-Document_Description").value
                var dn = document.getElementById("id_form-" + i + "-Document_Name").value
                docs[i] = new Array(ftsel, dd, dn)
            }catch(err){
                break;
            }
        }

        //TABLE COLUMNS
        var tr = document.createElement('TR');
        tableBody.appendChild(tr);
        for (i = 0; i < heading.length; i++) {
                var th = document.createElement('TH')
                th.width = '300';
                th.appendChild(document.createTextNode(heading[i]));
                tr.appendChild(th);
        }

        //TABLE ROWS
        for (i = 0; i < docs.length; i++) {
            var tr = document.createElement('TR');
            for (j = 0; j < docs[i].length; j++) {
                var td = document.createElement('TD')
                td.appendChild(document.createTextNode(docs[i][j]));
                tr.appendChild(td)
            }
            tableBody.appendChild(tr);
        }

        myTableDiv.appendChild(table);

        var myTableCells = table
        for (var i = 0, row; row = table.rows[i]; i++) {
            for (var j = 0, col; col = row.cells[j]; j++) {
                if(j == 0 & myTableCells.rows[i].cells[j].innerHTML != "File Type"){
                    if(myTableCells.rows[i].cells[j].innerHTML == "---Select/Update File Type---"){
                        myTableCells.rows[i].cells[j].style.color = "red" 
                        myTableCells.rows[i].cells[j].style.fontWeight="bold";
                    }else{
                        myTableCells.rows[i].cells[j].style.color = "black" 
                        myTableCells.rows[i].cells[j].style.fontWeight="normal";
                    }
                }

                if(j == 1 & myTableCells.rows[i].cells[j].innerHTML != "Document Description"){
                    if(myTableCells.rows[i].cells[j].innerHTML == ""){
                        myTableCells.rows[i].cells[j].style.color = "red" 
                        myTableCells.rows[i].cells[j].style.fontWeight="bold";
                        myTableCells.rows[i].cells[j].innerHTML = '"REQUIRED"'
                    }else{
                        myTableCells.rows[i].cells[j].style.color = "black" 
                        myTableCells.rows[i].cells[j].style.fontWeight="normal";
                    }
                }
            }
        }

        // if(i > 1){
        //     document.getElementById('docreviewlab').style.color = "black"
        //     document.getElementById('doccolor').style.color = "black"
        //     document.getElementById('docreviewcnt').innerHTML = i-1
        // }else{
        //     document.getElementById('docreviewlab').style.color = "red"
        //     document.getElementById('doccolor').style.color = "red"
        //     document.getElementById('docreviewcnt').innerHTML = i-1
        // }
    }catch(err){

        a = 1
    }


    var stalst = document.getElementById('StatesList').innerHTML
    var stalst1 = stalst.split(":")[1]
    if(stalst1 > "" & stalst1 != " "){
        document.getElementById('sts').style.color = "black"
        document.getElementById('statcolor').style.color = "black"
    }else{
        document.getElementById('sts').style.color = "red" 
        document.getElementById('statcolor').style.color = "red" 
    } 
    document.getElementById('StateList1').innerHTML = stalst1
    var coulst = document.getElementById('CntsList').innerHTML
    var coulst1 = coulst.split(":")[1]
    if(coulst1 > "" & coulst1 != " "){
        document.getElementById('cnties').style.color = "black"
        document.getElementById('cntycolor').style.color = "black"
    }else{
        document.getElementById('cnties').style.color = "red" 
        document.getElementById('cntycolor').style.color = "red"
    } 
    document.getElementById('CountyList1').innerHTML = coulst1

    if(tyacval != 'Non-Spatial Plan'){
        var ownlst = document.getElementById('OwnerList').innerHTML
        var ownlst1 = ownlst.split(":")[1]
        // if(ownlst1 > "" & ownlst1 != " "){
        //     document.getElementById('ownlab').style.color = "black"
        // }else{
        //     document.getElementById('ownlab').style.color = "red" 
        // } 
        document.getElementById('OwnerList1').innerHTML = ownlst1
    }
    

    var nyireq = 1
    list = document.getElementsByName('Imp_Status')
        for(var i=0; i<list.length;i++) {
          if (document.getElementsByName('Imp_Status')[i].checked) {

            if (document.getElementsByName('Imp_Status')[i].value == 2){
                document.getElementById('impstatrev').innerHTML = "In Progress"
                document.getElementById('impstatrevlab').style.color = "black"
                document.getElementById('impcolor').style.color = "black"
                nyireq = 0
            }else if(document.getElementsByName('Imp_Status')[i].value == 3){
                document.getElementById('impstatrev').innerHTML = "Completed"
                document.getElementById('impstatrevlab').style.color = "black"
                document.getElementById('impcolor').style.color = "black"
                nyireq = 1
            }else{
                document.getElementById('impstatrev').innerHTML = ""
                document.getElementById('impstatrevlab').style.color = "red" 
                document.getElementById('impcolor').style.color = "red"
            }
        }
   
    }    
    

    if(nyireq == 0){
        document.getElementById('DisNotImp').style.display = "inline-block"

        var checked = 0
        list = document.getElementsByName('Reas_Certain')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Reas_Certain')[i].checked) {
                checked = 1
                if(i == 0){
                    document.getElementById('wbirev').innerHTML = "Yes"
                    document.getElementById('wbirevlab').style.color = "black"
                    document.getElementById('<label for="id_Reas_Certain_0">a. The activity will be implemented:</label>_color').style.color = "black"
                }else if(i == 1){
                    document.getElementById('wbirev').innerHTML = "No"
                    document.getElementById('wbirevlab').style.color = "black"
                    document.getElementById('<label for="id_Reas_Certain_0">a. The activity will be implemented:</label>_color').style.color = "black"
                }else{
                    if(nyireq = 0){
                        document.getElementById('wbirev').innerHTML = ""
                        document.getElementById('wbirevlab').style.color = "red" 
                        document.getElementById('<label for="id_Reas_Certain_0">a. The activity will be implemented:</label>_color').style.color = "red"
                    }
                }
            }
        }

        if(checked == 0){
            document.getElementById('wbirev').innerHTML = ""
            document.getElementById('wbirevlab').style.color = "red"
            document.getElementById('<label for="id_Reas_Certain_0">a. The activity will be implemented:</label>_color').style.color = "red"
        }else{
            document.getElementById('<label for="id_Reas_Certain_0">a. The activity will be implemented:</label>_color').style.color = "black"
        }

        var checked = 0
        list = document.getElementsByName('Legal_Authority')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Legal_Authority')[i].checked) {
                checked = 1
                if(i == 0){
                    document.getElementById('larev').innerHTML = "Yes"
                    document.getElementById('larevlab').style.color = "black"
                    document.getElementById('<label for="id_Legal_Authority_0">b. The implementing party has the legal authority to conduct the activity:</label>_color').style.color = "black"
                }else if(i == 1){
                    document.getElementById('larev').innerHTML = "No"
                    document.getElementById('larevlab').style.color = "black"
                    document.getElementById('<label for="id_Legal_Authority_0">b. The implementing party has the legal authority to conduct the activity:</label>_color').style.color = "black"
                }else{
                    if(nyireq = 0){
                        document.getElementById('larev').innerHTML = ""
                        document.getElementById('larevlab').style.color = "red" 
                        document.getElementById('<label for="id_Legal_Authority_0">b. The implementing party has the legal authority to conduct the activity:</label>_color').style.color = "red"
                    }
                }
            }
        }

        if(checked == 0){
            document.getElementById('larev').innerHTML = ""
            document.getElementById('larevlab').style.color = "red"
            document.getElementById('<label for="id_Legal_Authority_0">b. The implementing party has the legal authority to conduct the activity:</label>_color').style.color = "red"
        }else{
            document.getElementById('<label for="id_Legal_Authority_0">b. The implementing party has the legal authority to conduct the activity:</label>_color').style.color = "black"
        }

        var checked = 0
        list = document.getElementsByName('Staff_Available')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Staff_Available')[i].checked) {
                checked = 1
                if(i == 0){
                    document.getElementById('rarev').innerHTML = "Yes"
                    document.getElementById('rarevlab').style.color = "black"
                    document.getElementById('<label for="id_Staff_Available_0">c. Financial, staffing, and administrative resources necessary to carry out the conservation effort are available:</label>_color').style.color = "black"
                }else if(i == 1){
                    document.getElementById('rarev').innerHTML = "No"
                    document.getElementById('rarevlab').style.color = "black"
                    document.getElementById('<label for="id_Staff_Available_0">c. Financial, staffing, and administrative resources necessary to carry out the conservation effort are available:</label>_color').style.color = "black"
                }else{
                    if(nyireq = 0){
                        document.getElementById('rarev').innerHTML = ""
                        document.getElementById('rarevlab').style.color = "red" 
                        document.getElementById('<label for="id_Staff_Available_0">c. Financial, staffing, and administrative resources necessary to carry out the conservation effort are available:</label>_color').style.color = "red"
                    }
                }
            }
        }

        if(checked == 0){
            document.getElementById('rarev').innerHTML = ""
            document.getElementById('rarevlab').style.color = "red"
            document.getElementById('<label for="id_Staff_Available_0">c. Financial, staffing, and administrative resources necessary to carry out the conservation effort are available:</label>_color').style.color = "red"
        }else{
            document.getElementById('<label for="id_Staff_Available_0">c. Financial, staffing, and administrative resources necessary to carry out the conservation effort are available:</label>_color').style.color = "black"
        }

        var checked = 0
        list = document.getElementsByName('Regulatory_Mech')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Regulatory_Mech')[i].checked) {
                checked = 1
                if(i == 0){
                    document.getElementById('miprev').innerHTML = "Yes"
                    document.getElementById('miprevlab').style.color = "black"
                    document.getElementById('<label for="id_Regulatory_Mech_0">d. Regulatory and/or procedural mechanisms are in place to carry out the efforts:</label>_color').style.color = "black"
                }else if(i == 1){
                    document.getElementById('miprev').innerHTML = "No"
                    document.getElementById('miprevlab').style.color = "black"
                    document.getElementById('<label for="id_Regulatory_Mech_0">d. Regulatory and/or procedural mechanisms are in place to carry out the efforts:</label>_color').style.color = "black"
                }else{
                    if(nyireq = 0){
                        document.getElementById('miprev').innerHTML = ""
                        document.getElementById('miprevlab').style.color = "red" 
                        document.getElementById('<label for="id_Regulatory_Mech_0">d. Regulatory and/or procedural mechanisms are in place to carry out the efforts:</label>_color').style.color = "red"
                    }
                }
            }
        }

        if(checked == 0){
            document.getElementById('miprev').innerHTML = ""
            document.getElementById('miprevlab').style.color = "red"
            document.getElementById('<label for="id_Regulatory_Mech_0">d. Regulatory and/or procedural mechanisms are in place to carry out the efforts:</label>_color').style.color = "red"
        }else{
            document.getElementById('<label for="id_Regulatory_Mech_0">d. Regulatory and/or procedural mechanisms are in place to carry out the efforts:</label>_color').style.color = "black"
        }

        var checked = 0
        list = document.getElementsByName('Compliance')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Compliance')[i].checked) {
                checked = 1
                if(i == 0){
                    document.getElementById('crrev').innerHTML = "Yes"
                    document.getElementById('crrevlab').style.color = "black"
                    document.getElementById('<label for="id_Compliance_0">e. All Federal/State/Local legal project compliance requirements have been met or are reasonably certain to be met:</label>_color').style.color = "black"
                }else if(i == 1){
                    document.getElementById('crrev').innerHTML = "No"
                    document.getElementById('crrevlab').style.color = "black"
                    document.getElementById('<label for="id_Compliance_0">e. All Federal/State/Local legal project compliance requirements have been met or are reasonably certain to be met:</label>_color').style.color = "black"
                }else{
                    if(nyireq = 0){
                        document.getElementById('crrev').innerHTML = ""
                        document.getElementById('crrevlab').style.color = "red" 
                        document.getElementById('<label for="id_Compliance_0">e. All Federal/State/Local legal project compliance requirements have been met or are reasonably certain to be met:</label>_color').style.color = "red"
                    }
                }
            }
        }

        if(checked == 0){
            document.getElementById('crrev').innerHTML = ""
            document.getElementById('crrevlab').style.color = "red"
            document.getElementById('<label for="id_Compliance_0">e. All Federal/State/Local legal project compliance requirements have been met or are reasonably certain to be met:</label>_color').style.color = "red"
        }else{
            document.getElementById('<label for="id_Compliance_0">e. All Federal/State/Local legal project compliance requirements have been met or are reasonably certain to be met:</label>_color').style.color = "black"
        }

        var checked = 0
        list = document.getElementsByName('Vol_Incentives')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Vol_Incentives')[i].checked) {
                checked = 1
                if(i == 0){
                    document.getElementById('vprev').innerHTML = "Yes"
                    document.getElementById('vprevlab').style.color = "black"
                    document.getElementById('<label for="id_Vol_Incentives_0">f. If voluntary participation is needed, are incentives adequate to ensure the level of participation necessary to carry out the conservation effort:</label>_color').style.color = "black"
                }else if(i == 1){
                    document.getElementById('vprev').innerHTML = "No"
                    document.getElementById('vprevlab').style.color = "black"
                    document.getElementById('<label for="id_Vol_Incentives_0">f. If voluntary participation is needed, are incentives adequate to ensure the level of participation necessary to carry out the conservation effort:</label>_color').style.color = "black"
                }else if(i == 2){
                    document.getElementById('vprev').innerHTML = "N/A"
                    document.getElementById('vprevlab').style.color = "black"
                    document.getElementById('<label for="id_Vol_Incentives_0">f. If voluntary participation is needed, are incentives adequate to ensure the level of participation necessary to carry out the conservation effort:</label>_color').style.color = "black"
                }else{
                    if(nyireq = 0){
                        document.getElementById('vprev').innerHTML = ""
                        document.getElementById('vprevlab').style.color = "red" 
                        document.getElementById('<label for="id_Vol_Incentives_0">f. If voluntary participation is needed, are incentives adequate to ensure the level of participation necessary to carry out the conservation effort:</label>_color').style.color = "red"
                    }
                }
            }
        }

        if(checked == 0){
            document.getElementById('vprev').innerHTML = ""
            document.getElementById('vprevlab').style.color = "red"
            document.getElementById('<label for="id_Vol_Incentives_0">f. If voluntary participation is needed, are incentives adequate to ensure the level of participation necessary to carry out the conservation effort:</label>_color').style.color = "red"
        }else{
            document.getElementById('<label for="id_Vol_Incentives_0">f. If voluntary participation is needed, are incentives adequate to ensure the level of participation necessary to carry out the conservation effort:</label>_color').style.color = "black"
        }

    }else{
        document.getElementById('DisNotImp').style.display = "none"
    }


    if(nyireq2nd == 1){

        var checked = 0
        list = document.getElementsByName('Reduce_Threats')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Reduce_Threats')[i].checked) {
                checked = 1
                if(i == 0){
                    document.getElementById('dtrrev').innerHTML = "Yes"
                    document.getElementById('dtrrevlab').style.color = "black"
                    document.getElementById('<label for="id_Reduce_Threats_0">a. Describe how the conservation effort reduces the threats:</label>_color').style.color = "black"
                }else if(i == 1){
                    document.getElementById('dtrrev').innerHTML = "No"
                    document.getElementById('dtrrevlab').style.color = "black"
                    document.getElementById('<label for="id_Reduce_Threats_0">a. Describe how the conservation effort reduces the threats:</label>_color').style.color = "black"
                }else{
                    if(ndereq = 0){
                        document.getElementById('dtrrev').innerHTML = ""
                        document.getElementById('dtrrevlab').style.color = "red"
                        document.getElementById('<label for="id_Reduce_Threats_0">a. Describe how the conservation effort reduces the threats:</label>_color').style.color = "red" 
                    }
                }
            }
        }
        if(checked == 0){
            document.getElementById('dtrrev').innerHTML = ""
            document.getElementById('dtrrevlab').style.color = "red"
            document.getElementById('<label for="id_Reduce_Threats_0">a. Describe how the conservation effort reduces the threats:</label>_color').style.color = "red"
        }else{
            document.getElementById('<label for="id_Reduce_Threats_0">a. Describe how the conservation effort reduces the threats:</label>_color').style.color = "black"
        }

    
        var checked = 0
        document.getElementById('DisNotEff').style.display = "inline-block"
        list = document.getElementsByName('Incremental_Objectives')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Incremental_Objectives')[i].checked) {
                checked = 1
                if(i == 0){
                    document.getElementById('iorev').innerHTML = "Yes"
                    document.getElementById('iorevlab').style.color = "black"
                    document.getElementById('<label for="id_Incremental_Objectives_0">b. Provide incremental objectives and dates for achieving them:</label>_color').style.color = "black"
                }else if(i == 1){
                    document.getElementById('iorev').innerHTML = "No"
                    document.getElementById('iorevlab').style.color = "black"
                    document.getElementById('<label for="id_Incremental_Objectives_0">b. Provide incremental objectives and dates for achieving them:</label>_color').style.color = "black"
                }else{
                    if(ndereq = 0){
                        document.getElementById('iorev').innerHTML = ""
                        document.getElementById('iorevlab').style.color = "red" 
                        document.getElementById('<label for="id_Incremental_Objectives_0">b. Provide incremental objectives and dates for achieving them:</label>_color').style.color = "red"
                    }
                }
            }
        }

        if(checked == 0){
            document.getElementById('iorev').innerHTML = ""
            document.getElementById('iorevlab').style.color = "red"
            document.getElementById('<label for="id_Incremental_Objectives_0">b. Provide incremental objectives and dates for achieving them:</label>_color').style.color = "red"
        }else{
            document.getElementById('<label for="id_Incremental_Objectives_0">b. Provide incremental objectives and dates for achieving them:</label>_color').style.color = "black"
        }

        var checked = 0
        list = document.getElementsByName('Quantifiable_Measures')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Quantifiable_Measures')[i].checked) {
                checked = 1
                if(i == 0){
                    document.getElementById('iemrev').innerHTML = "Yes"
                    document.getElementById('iemrevlab').style.color = "black"
                    document.getElementById('<label for="id_Quantifiable_Measures_0">c. Provide quantifiable performance measures to monitor both implementation and effectiveness:</label>_color').style.color = "black"
                }else if(i == 1){
                    document.getElementById('iemrev').innerHTML = "No"
                    document.getElementById('iemrevlab').style.color = "black"
                    document.getElementById('<label for="id_Quantifiable_Measures_0">c. Provide quantifiable performance measures to monitor both implementation and effectiveness:</label>_color').style.color = "black"
                }else{
                    if(ndereq = 0){
                        document.getElementById('iemrev').innerHTML = ""
                        document.getElementById('iemrevlab').style.color = "red" 
                        document.getElementById('<label for="id_Quantifiable_Measures_0">c. Provide quantifiable performance measures to monitor both implementation and effectiveness:</label>_color').style.color = "red"
                    }
                }
            }
        }

        if(checked == 0){
            document.getElementById('iemrev').innerHTML = ""
            document.getElementById('iemrevlab').style.color = "red"
            document.getElementById('<label for="id_Quantifiable_Measures_0">c. Provide quantifiable performance measures to monitor both implementation and effectiveness:</label>_color').style.color = "red"
        }else{
            document.getElementById('<label for="id_Quantifiable_Measures_0">c. Provide quantifiable performance measures to monitor both implementation and effectiveness:</label>_color').style.color = "black"
        }

        var checked = 0
        list = document.getElementsByName('AD_Strategy')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('AD_Strategy')[i].checked) {
                checked = 1
                if(i == 0){
                    document.getElementById('amrev').innerHTML = "Yes"
                    document.getElementById('amrevlab').style.color = "black"
                    document.getElementById('<label for="id_AD_Strategy_0">d.  Incorporate principles of adaptive management (e.g. a corrective management strategy):</label>_color').style.color = "black"
                }else if(i == 1){
                    document.getElementById('amrev').innerHTML = "No"
                    document.getElementById('amrevlab').style.color = "black"
                    document.getElementById('<label for="id_AD_Strategy_0">d.  Incorporate principles of adaptive management (e.g. a corrective management strategy):</label>_color').style.color = "black"
                }else{
                    if(ndereq = 0){
                        document.getElementById('amrev').innerHTML = ""
                        document.getElementById('amrevlab').style.color = "red" 
                        document.getElementById('<label for="id_AD_Strategy_0">d.  Incorporate principles of adaptive management (e.g. a corrective management strategy):</label>_color').style.color = "red"
                    }
                }
            }
        }
        if(checked == 0){
            document.getElementById('amrev').innerHTML = ""
            document.getElementById('amrevlab').style.color = "red"
            document.getElementById('<label for="id_AD_Strategy_0">d.  Incorporate principles of adaptive management (e.g. a corrective management strategy):</label>_color').style.color = "red"
        }else{
            document.getElementById('<label for="id_AD_Strategy_0">d.  Incorporate principles of adaptive management (e.g. a corrective management strategy):</label>_color').style.color = "black"
        }
    }else{
        document.getElementById('DisNotEff').style.display = "none"
    }

    

    

}

}


function UpdateStat(){
    list = document.getElementsByName('Imp_Status')
    for(var i=0; i<list.length;i++) {
      if (document.getElementsByName('Imp_Status')[i].checked) {
        if (document.getElementsByName('Imp_Status')[i].value < 3){
            var str = "***REQUIRED*** For efforts not yet implemented, is there a high level of certainty that:";
            var result = str.fontcolor("red");
            document.getElementById('Part1Label').innerHTML = result;
            document.getElementById('Reas_Certain').style.display = "inline-block";
            document.getElementById('Legal_Authority').style.display = "inline-block";
            document.getElementById('Staff_Available').style.display = "inline-block";
            document.getElementById('Regulatory_Mech').style.display = "inline-block";
            document.getElementById('Compliance').style.display = "inline-block";
            document.getElementById('Vol_Incentives').style.display = "inline-block";

        }

        if (document.getElementsByName('Imp_Status')[i].value == 3){
            var str = "With your effort complete, no additional questions required for Part 1";
            document.getElementById('Part1Label').innerHTML = str;
            document.getElementById('Reas_Certain').style.display = "none";
            document.getElementById('Legal_Authority').style.display = "none";
            document.getElementById('Staff_Available').style.display = "none";
            document.getElementById('Regulatory_Mech').style.display = "none";
            document.getElementById('Compliance').style.display = "none";
            document.getElementById('Vol_Incentives').style.display = "none";

        }
      }
    }
}


function UpdateEffect(){
  list = document.getElementsByName('Effective_Determined')
  for(var i=0; i<list.length;i++) {
    if (document.getElementsByName('Effective_Determined')[i].checked) {
      var effval = document.getElementsByName('Effective_Determined')[i].value
      if (effval == 1 | effval == 4 | effval == 10 | effval == 17 | effval == 33 | effval == 39 | effval == 42 | effval == 45 | effval == 48 | effval == 51 | effval == 54 | effval == 57 | effval == 60 | effval == 7 | effval == 11 | effval == 14 | effval == 18 | effval == 21 | effval == 24 | effval == 27 | effval == 30 | effval == 36 | effval == 63 | effval == 66 | effval == 69){

        var str = "With your effort fully effective, no additional questions required for Part 2";
        var str1 = 'Explain why the activity was deemed effective:';
        document.getElementById('Effect_Explained_Label').innerHTML = str1;
        document.getElementById('Part2Label').innerHTML = str;
        document.getElementById('Reduce_Threats').style.display = "none";
        document.getElementById('Incremental_Objectives').style.display = "none";
        document.getElementById('Quantifiable_Measures').style.display = "none";
        document.getElementById('AD_Strategy').style.display = "none";
      } else {
        var str = "***REQUIRED*** For efforts not deemed effective (e.g. programs/actions only recently implemented), does the effort:";
        str = str.fontcolor("red");
        document.getElementById('Part2Label').innerHTML = str;
        var str1 = 'Explain why the activity is highly likely to be effective:';
        document.getElementById('Effect_Explained_Label').innerHTML = str1;
        document.getElementById('Reduce_Threats').style.display = "inline-block";
        document.getElementById('Incremental_Objectives').style.display = "inline-block";
        document.getElementById('Quantifiable_Measures').style.display = "inline-block";
        document.getElementById('AD_Strategy').style.display = "inline-block";
      }
    }
  }
}


function KeyUpObjDesc(){
    var objwrdcntval = document.getElementById('id_Objectives_Desc').value
    var objchacntval1 = objwrdcntval.length
    var objwrdcntval1 = objwrdcntval.split(' ').length
    if(objchacntval1 == 0){
        objwrdcntval1 = 0
    }
    if(objchacntval1 > 5000){
        var string = objwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Objectives_Desc').value = trimmedString
        objwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        objchacntval1 = 5000
    }

    var objwrdval = "Words: " + objwrdcntval1 + "; Characters: " + objchacntval1 + " out of 5000"
    document.getElementById("objwrdcnt").innerHTML = objwrdval 
}

function KeyUpMthDesc(){
    var mthwrdcntval = document.getElementById('id_Methods_Explained').value
    var mthchacntval1 = mthwrdcntval.length
    var mthwrdcntval1 = mthwrdcntval.split(' ').length
    if(mthchacntval1 == 0){
        mthwrdcntval1 = 0
    }
    if(mthchacntval1 > 5000){
        var string = mthwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Methods_Explained').value = trimmedString
        mthwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        objchacntval1 = 5000
    }

    var mthwrdval = "Words: " + mthwrdcntval1 + "; Characters: " + mthchacntval1 + " out of 5000"
    document.getElementById("mthwrdcnt").innerHTML = mthwrdval 
}


function KeyUpEffectExplain(){
    var effexpwrdcntval = document.getElementById('id_Effective_Explained').value
    var effchacntval1 = effexpwrdcntval.length
    var effexpwrdcntval1 = effexpwrdcntval.split(' ').length
    if(effchacntval1 == 0){
        effexpwrdcntval1 = 0
    }

    if(effchacntval1 > 5000){
        var string = effexpwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Effective_Explained').value = trimmedString
        effexpwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        effchacntval1 = 5000
    }

    var effexpwrdval = "Words: " + effexpwrdcntval1 + "; Characters: " + effchacntval1 + " out of 5000"
    document.getElementById("effexpwrdcnt").innerHTML = effexpwrdval 
}

function KeyUpAgConv(){
    var acwrdcntval = document.getElementById('id_Ag_Conversion_Explain').value
    var acchacntval1 = acwrdcntval.length
    var acwrdcntval1 = acwrdcntval.split(' ').length
    if(acchacntval1 == 0){
        acwrdcntval1 = 0
    }
    if(acchacntval1 > 5000){
        var string = acwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Ag_Conversion_Explain').value = trimmedString
        acwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        acchacntval1 = 5000
    }

    var acwrdval = "Words: " + acwrdcntval1 + "; Characters: " + acchacntval1 + " out of 5000"
    document.getElementById("acwrdcnt").innerHTML = acwrdval 
}

function KeyUpCon(){
    var acwrdcntval = document.getElementById('id_Conifer_Encroach_Explain').value
    var acchacntval1 = acwrdcntval.length
    var acwrdcntval1 = acwrdcntval.split(' ').length
    if(acchacntval1 == 0){
        acwrdcntval1 = 0
    }
    if(acchacntval1 > 5000){
        var string = acwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Conifer_Encroach_Explain').value = trimmedString
        acwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        acchacntval1 = 5000
    }

    var acwrdval = "Words: " + acwrdcntval1 + "; Characters: " + acchacntval1 + " out of 5000"
    document.getElementById("cwrdcnt").innerHTML = acwrdval 
}

function KeyUpOilGas(){
    var acwrdcntval = document.getElementById('id_Oil_Gas_Explain').value
    var acchacntval1 = acwrdcntval.length
    var acwrdcntval1 = acwrdcntval.split(' ').length
    if(acchacntval1 == 0){
        acwrdcntval1 = 0
    }
    if(acchacntval1 > 5000){
        var string = acwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Oil_Gas_Explain').value = trimmedString
        acwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        acchacntval1 = 5000
    }

    var acwrdval = "Words: " + acwrdcntval1 + "; Characters: " + acchacntval1 + " out of 5000"
    document.getElementById("ogwrdcnt").innerHTML = acwrdval 
}

function KeyUpFire(){
    var acwrdcntval = document.getElementById('id_Fire_Explain').value
    var acchacntval1 = acwrdcntval.length
    var acwrdcntval1 = acwrdcntval.split(' ').length
    if(acchacntval1 == 0){
        acwrdcntval1 = 0
    }
    if(acchacntval1 > 5000){
        var string = acwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Fire_Explain').value = trimmedString
        acwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        acchacntval1 = 5000
    }

    var acwrdval = "Words: " + acwrdcntval1 + "; Characters: " + acchacntval1 + " out of 5000"
    document.getElementById("fwrdcnt").innerHTML = acwrdval 
}

function KeyUpFerEquid(){
    var acwrdcntval = document.getElementById('id_Feral_Equids_Explain').value
    var acchacntval1 = acwrdcntval.length
    var acwrdcntval1 = acwrdcntval.split(' ').length
    if(acchacntval1 == 0){
        acwrdcntval1 = 0
    }
    if(acchacntval1 > 5000){
        var string = acwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Feral_Equids_Explain').value = trimmedString
        acwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        acchacntval1 = 5000
    }

    var acwrdval = "Words: " + acwrdcntval1 + "; Characters: " + acchacntval1 + " out of 5000"
    document.getElementById("fewrdcnt").innerHTML = acwrdval 
}

function KeyUpImGraze(){
    var acwrdcntval = document.getElementById('id_Improper_Grazing_Explain').value
    var acchacntval1 = acwrdcntval.length
    var acwrdcntval1 = acwrdcntval.split(' ').length
    if(acchacntval1 == 0){
        acwrdcntval1 = 0
    }
    if(acchacntval1 > 5000){
        var string = acwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Improper_Grazing_Explain').value = trimmedString
        acwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        acchacntval1 = 5000
    }

    var acwrdval = "Words: " + acwrdcntval1 + "; Characters: " + acchacntval1 + " out of 5000"
    document.getElementById("igwrdcnt").innerHTML = acwrdval 
}

function KeyUpInfra(){
    var acwrdcntval = document.getElementById('id_Infrastructure_Explain').value
    var acchacntval1 = acwrdcntval.length
    var acwrdcntval1 = acwrdcntval.split(' ').length
    if(acchacntval1 == 0){
        acwrdcntval1 = 0
    }
    if(acchacntval1 > 5000){
        var string = acwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Infrastructure_Explain').value = trimmedString
        acwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        acchacntval1 = 5000
    }

    var acwrdval = "Words: " + acwrdcntval1 + "; Characters: " + acchacntval1 + " out of 5000"
    document.getElementById("infwrdcnt").innerHTML = acwrdval 
}

function KeyUpIsoPos(){
    var acwrdcntval = document.getElementById('id_Isolated_Explain').value
    var acchacntval1 = acwrdcntval.length
    var acwrdcntval1 = acwrdcntval.split(' ').length
    if(acchacntval1 == 0){
        acwrdcntval1 = 0
    }
    if(acchacntval1 > 5000){
        var string = acwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Isolated_Explain').value = trimmedString
        acwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        acchacntval1 = 5000
    }

    var acwrdval = "Words: " + acwrdcntval1 + "; Characters: " + acchacntval1 + " out of 5000"
    document.getElementById("ipwrdcnt").innerHTML = acwrdval 
}


function KeyUpMining(){
    var acwrdcntval = document.getElementById('id_Mining_Explain').value
    var acchacntval1 = acwrdcntval.length
    var acwrdcntval1 = acwrdcntval.split(' ').length
    if(acchacntval1 == 0){
        acwrdcntval1 = 0
    }
    if(acchacntval1 > 5000){
        var string = acwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Mining_Explain').value = trimmedString
        acwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        acchacntval1 = 5000
    }

    var acwrdval = "Words: " + acwrdcntval1 + "; Characters: " + acchacntval1 + " out of 5000"
    document.getElementById("mwrdcnt").innerHTML = acwrdval 
}

function KeyUpInvasives(){
    var acwrdcntval = document.getElementById('id_Invasives_Explained').value
    var acchacntval1 = acwrdcntval.length
    var acwrdcntval1 = acwrdcntval.split(' ').length
    if(acchacntval1 == 0){
        acwrdcntval1 = 0
    }
    if(acchacntval1 > 5000){
        var string = acwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Invasives_Explained').value = trimmedString
        acwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        acchacntval1 = 5000
    }

    var acwrdval = "Words: " + acwrdcntval1 + "; Characters: " + acchacntval1 + " out of 5000"
    document.getElementById("invwrdcnt").innerHTML = acwrdval 
}

function KeyUpRec(){
    var acwrdcntval = document.getElementById('id_Recreation_Explain').value
    var acchacntval1 = acwrdcntval.length
    var acwrdcntval1 = acwrdcntval.split(' ').length
    if(acchacntval1 == 0){
        acwrdcntval1 = 0
    }
    if(acchacntval1 > 5000){
        var string = acwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Recreation_Explain').value = trimmedString
        acwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        acchacntval1 = 5000
    }

    var acwrdval = "Words: " + acwrdcntval1 + "; Characters: " + acchacntval1 + " out of 5000"
    document.getElementById("rwrdcnt").innerHTML = acwrdval 
}

function KeyUpSageLoss(){
    var acwrdcntval = document.getElementById('id_Sagebrush_Loss_Explain').value
    var acchacntval1 = acwrdcntval.length
    var acwrdcntval1 = acwrdcntval.split(' ').length
    if(acchacntval1 == 0){
        acwrdcntval1 = 0
    }
    if(acchacntval1 > 5000){
        var string = acwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Sagebrush_Loss_Explain').value = trimmedString
        acwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        acchacntval1 = 5000
    }

    var acwrdval = "Words: " + acwrdcntval1 + "; Characters: " + acchacntval1 + " out of 5000"
    document.getElementById("slwrdcnt").innerHTML = acwrdval 
}

function KeyUpUrbDev(){
    var acwrdcntval = document.getElementById('id_Urban_Devel_Explain').value
    var acchacntval1 = acwrdcntval.length
    var acwrdcntval1 = acwrdcntval.split(' ').length
    if(acchacntval1 == 0){
        acwrdcntval1 = 0
    }
    if(acchacntval1 > 5000){
        var string = acwrdcntval;
        var length = 5000;
        var trimmedString = string.substring(0, length);
        document.getElementById('id_Urban_Devel_Explain').value = trimmedString
        acwrdcntval1 = trimmedString.split(' ').length
        alert('Maximum character limit reached, please reduce text or upload additional documentation')
        acchacntval1 = 5000
    }

    var acwrdval = "Words: " + acwrdcntval1 + "; Characters: " + acchacntval1 + " out of 5000"
    document.getElementById("udwrdcnt").innerHTML = acwrdval 
}

function CheckAcDiff(){

    var repAcre = document.getElementById('id_Metric_Value').value;
    repAcre = Math.round(repAcre)
    var GISAcre = document.getElementById('GISACVAL').innerHTML;
    GISAcre = Math.round(GISAcre)
    var AcreDiff = repAcre - GISAcre;

    if(GISAcre > 0){
      if(AcreDiff >= 0){
          var diffthan = "greater than"
          AcreDiff = Math.abs(AcreDiff)
          var AcrePer = repAcre / GISAcre * 100;
          AcrePer = Math.round(AcrePer)
          AcrePer = AcrePer - 100
          AcrePer = Math.abs(AcrePer)
          if(AcrePer >= 1){
            document.getElementById('GISAcres').innerHTML = "ATTENTION: *Reported acreage (User Defined -' Metric Value')  is " + AcreDiff + "ac (" + AcrePer +"%) " + diffthan + " aathe GIS-calculated acreage (represented by your spatial input).  Please ensure these values represent the correct area where the conservation action was implemented. We caution including adjacent acres that may receive indirect benefit, if they are not included in the project/treatment area.";
          }else{
            document.getElementById('GISAcres').innerHTML = ""
          }
      }else{
          var diffthan = "less than"
          AcreDiff = Math.abs(AcreDiff)
          var AcrePer = repAcre / GISAcre * 100;
          AcrePer = Math.round(AcrePer)
          AcrePer = AcrePer - 100
          AcrePer = Math.abs(AcrePer)
          if(AcrePer < 25 & AcrePer >= 1){
            document.getElementById('GISAcres').innerHTML = "ATTENTION: *Reported acreage (User Defined -' Metric Value')  is " + AcreDiff + "ac (" + AcrePer +"%) " + diffthan + " the GIS-calculated acreage (represented by your spatial input).  Please ensure these values represent the correct area where the conservation action was implemented. We caution including adjacent acres that may receive indirect benefit, if they are not included in the project/treatment area.";
          }else if(AcrePer >= 25){
            document.getElementById('GISAcres').innerHTML = "ATTENTION: *Reported acreage (User Defined -' Metric Value') is less than 75% of the “GIS-Calculated” acreage (represented by your spatial input). Please adjust your spatial input to accurately represent the area(s) treated.";
          }else{
            document.getElementById('GISAcres').innerHTML = ""
          }
          
      }
      

      
    }
}

function showsubmit(){
 
  var docs = ""
  var docs = document.getElementsByName('myfiles');
  var docsexist = 0
  for(var i=0; i<docs.length;i++) {
      if(docs[i].value > ""){
          docsexist = 1
      }
  }

  if(docsexist == 1){
      document.getElementById("subbutton").style.display = "inline-block";
  }else{
      document.getElementById("subbutton").style.display = "none";
  }
}


// function ShowThreatExplain(){
  
//   var Control
//   var Control1
//   var Outputlist = ""    
//   document.getElementById('threatdivac').style.display = "none";
//   document.getElementById('threatdivce').style.display = "none";
//   document.getElementById('threatdivog').style.display = "none";
//   document.getElementById('threatdivfi').style.display = "none";
//   document.getElementById('threatdivfe').style.display = "none";
//   document.getElementById('threatdivig').style.display = "none";
//   document.getElementById('threatdivin').style.display = "none";
//   document.getElementById('threatdivip').style.display = "none";
//   document.getElementById('threatdivmi').style.display = "none";
//   document.getElementById('threatdiviv').style.display = "none";
//   document.getElementById('threatdivre').style.display = "none";
//   document.getElementById('threatdivsl').style.display = "none";
//   document.getElementById('threatdivud').style.display = "none";
//   var list = document.getElementsByName('Threat')
//   for(var i=0; i<list.length;i++) {
//     if (list[i].checked) {
//       Control = list[i].parentNode.innerHTML;
//       Control1 = Control.split(">");
//       var Control2 = String(Control1[1])
//       Control2 = Control2.replace(/[\n\r]/g, '');
//       Control2 = Control2.substr(1);

//       if (Control2 == "AGRICULTURAL CONVERSION (Tillage Risk)"){
//         document.getElementById('threatdivac').style.display = "block";
//       }

//       if (Control2 == "CONIFER ENCROACHMENT"){
//         document.getElementById('threatdivce').style.display = "block";
//       }

//       if (Control2 == "OIL &amp; GAS DEVELOPMENT"){
//           document.getElementById('threatdivog').style.display = "block";
//       }

//       if (Control2 == "FIRE"){
//           document.getElementById('threatdivfi').style.display = "block";
//       }

//       if (Control2 == "FERAL EQUIDS"){
//           document.getElementById('threatdivfe').style.display = "block";
//       }

//       if (Control2 == "IMPROPER GRAZING / RANGE MANAGEMENT"){
//           document.getElementById('threatdivig').style.display = "block";
//       }

//       if (Control2 == "INFRASTRUCTURE (Roads, Powerlines, Renewable Energy)"){
//           document.getElementById('threatdivin').style.display = "block";
//       }

//       if (Control2 == "ISOLATED / SMALL POPULATION SIZE"){
//         document.getElementById('threatdivip').style.display = "block";
//       }

//       if (Control2 == "MINING"){
//         document.getElementById('threatdivmi').style.display = "block";
//       }

//       if (Control2 == "INVASIVES (Annual Grasses and Noxious Weeds)"){
//         document.getElementById('threatdiviv').style.display = "block"; 
//       }

//       if (Control2 == "RECREATION"){
//         document.getElementById('threatdivre').style.display = "block";
//       }

//       if (Control2 == "SAGEBRUSH LOSS or DEGRADATION"){
//         document.getElementById('threatdivsl').style.display = "block";
//       }
      
//       if (Control2 == "URBAN DEVELOPMENT"){
//         document.getElementById('threatdivud').style.display = "block";  
//       }
//     }
//   }
// }

function DisplayEC() {

    var errorlist = []
    var cnt = 1

    // var loclists = [['WAFWA_Value', 'WAFWAs Selected: ', 'WAFWAList1'], ['Population_Value', 'Populations Selected: ', 'PopList1'], ['State_Value', 'States Selected: ', 'StateList1'], ['County_Value', 'Counties Selected: ', 'CountyList1']]
    var loclists = [['State_Value', 'States Selected: ', 'StateList1'], ['County_Value', 'Counties Selected: ', 'CountyList1']]

    var stmnth = document.getElementById("id_Start_Date_month").value
    var stday = document.getElementById("id_Start_Date_day").value
    var styear = document.getElementById("id_Start_Date_year").value
    var strt = stmnth + "/" + stday + "/" + styear
    if(stmnth == 0 | stday == 0 | styear == 0){
        errorlist.push(" Start Date is required")
    }

    var fnmnth = document.getElementById("id_End_Date_month").value
    var fnday = document.getElementById("id_End_Date_day").value
    var fnyear = document.getElementById("id_End_Date_year").value
    var fnsh = fnmnth + "/" + fnday + "/" + fnyear

    if(fnmnth == 0 | fnday == 0 | fnyear == 0){
        errorlist.push(" End Date is required")
    }

    if(subactiv == "Conservation Agreements (including but not limited to: CCAs, CCAAs, Farm Bill and other Incentive-based programs)" | subactiv == "Powerline Burial" | subactiv == "Fence Marking" | subactiv == "Fence Removal" | subactiv == "Improved Grazing Practices (Rest, Rotation, Etc.)" | subactiv == "Road and Trail closure"){

        if(document.getElementById('id_Metric_Value').value <= 0){
            errorlist.push(" Metric Value is required")
        }

    }

    if(tyacval == 'Spatial Project'){

        if(document.getElementById('id_Metric_Value').value <= 0){
            errorlist.push(" Metric Value is required")
        }


        if(document.getElementById('GISAC').innerHTML <= 0){
            errorlist.push(" Spatial Data is required")
        }
    }


    var repAcre = document.getElementById('id_Metric_Value').value;
    repAcre = Math.round(repAcre)
    var GISAcre = document.getElementById('GISACVAL').innerHTML;
    GISAcre = Math.round(GISAcre)
    var AcreDiff = repAcre - GISAcre;

    if(GISAcre > 0){
      if(AcreDiff >= 0){
          var diffthan = "greater than"
      }else{
          var diffthan = "less than"
          AcreDiff = Math.abs(AcreDiff)
          var AcrePer = repAcre / GISAcre * 100;
          AcrePer = Math.round(AcrePer)
          AcrePer = AcrePer - 100
          AcrePer = Math.abs(AcrePer)
          if(AcrePer < 25 & AcrePer >= 1){
            var a = 1
          }else if(AcrePer >= 25){
            errorlist.push(" ATTENTION: *Reported acreage (User Defined -' Metric Value') is less than 75% of the “GIS-Calculated” acreage (represented by your spatial input). Please adjust your spatial input to accurately represent the area(s) treated.")
          }
          
      }
      

      
    }


    if(subact == "Vegetation Management / Habitat Enhancement" | subact == "Energy development reclamation with the goal of sagebrush restoration"){
        var stype = ""
        var st = document.getElementsByName('seeding_type')
        for(var i=0; i<st.length;i++) {
            if (document.getElementsByName("seeding_type")[i].checked) {
                stype = document.getElementsByName("seeding_type")[i].parentNode.innerHTML;
            }
        }

        if(stype == ""){
            stype2 = ""
        }else{
            stype1 = stype.split(">");
            var stype2 = stype1[1]
            stype2 = String(stype2)
            stype2 = stype2.replace(/[\n\r]/g, '');
            stype2 = stype2.substr(1);
        }
        if(stype2 == ""){
            errorlist.push(" Seeding Type is required")    
        }
    }

    // Mitigation validation
    var mittype = ""
    var mit = document.getElementsByName('mitigation')
    for(var i=0; i<mit.length;i++) {
        if (document.getElementsByName("mitigation")[i].checked) {
            mittype = document.getElementsByName("mitigation")[i].parentNode.innerHTML;
        }
    }

    if(mittype == ""){
          mittype2 = ""
      }else{
          mittype1 = mittype.split(">");
          mittype2 = mittype1[1]
          mittype2 = String(mittype2)
          mittype2 = mittype2.replace(/[\n\r]/g, '');
          mittype2 = mittype2.substr(1);
      }

    if(mittype2 == ""){
          errorlist.push(" Mitigation Treatment status is required")
      }



    if(activ == 'RESTORATION: Post-Disturbance and/or Habitat Enhancement'){
        var frtype = ""

        var fr = document.getElementsByName('post_fire')
        for(var i=0; i<fr.length;i++) {
            if (document.getElementsByName("post_fire")[i].checked) {
                frtype = document.getElementsByName("post_fire")[i].parentNode.innerHTML;
            }
        }


        if(frtype == ""){
            frtype2 = ""
        }else{
            frtype1 = frtype.split(">");
            frtype2 = frtype1[1]
            frtype2 = String(frtype2)
            frtype2 = frtype2.replace(/[\n\r]/g, '');
            frtype2 = frtype2.substr(1);
        }

        if(frtype2 > -1){
            errorlist.push(" Post Wildfire status is required")
        }
    }


    if(subactiv == "Powerline Burial"){
        var pl = document.getElementById('id_Type_of_Powerline')
        var plnum = pl.options[pl.selectedIndex].value;
        var pltypeval
        if(plnum == '-------'){
            errorlist.push(" Powerline Type is required")
        }
    }

    if(subactiv == "Conservation Agreements (including but not limited to: CCAs, CCAAs, Farm Bill and other Incentive-based programs)"){

        if(document.getElementById('id_Agreement_Length').value <= 0){
            errorlist.push(" Agreement Length is required")
        }

        if(document.getElementById('id_Agreement_Penalty').value <= 0){
            errorlist.push(" Agreement Penalty is required")
        }

        if(document.getElementById('id_CCAA_Num_Permit_Holders').value <= 0){
            errorlist.push(" Number of Permit Holders is required")
        }

    }


    
    if(tyacval != 'Non-Spatial Plan'){
        // Objective List
        var objlist = document.getElementsByName('Objective') 
        var objtxt = ""
        var cnt = 0
        var ObjectiveTextTest = 0
        for(var i=0; i<objlist.length;i++) {
            if (objlist[i].checked) {

                var Control = objlist[i].parentNode.innerHTML;
                var Control1 = Control.split(">");
                var Control2 = String(Control1[1])
                Control2 = Control2.replace(/[\n\r]/g, '');
                Control2 = Control2.substr(1);
                Objective = Control2
                if(cnt == 0){
                  objtxt = Objective
                  cnt = 1
                } else {
                  objtxt = objtxt + "; " + Objective
                }

                if(Objective == "Other - Please specify in text box"){
                  ObjectiveTextTest = 1
                }
            }

        }


        if (cnt == 0){
          errorlist.push(" At least one selected objective is required")
        } 

        if(ObjectiveTextTest == 1){
              if(document.getElementById('id_Objectives_Desc').value == ""){
                 errorlist.push(" Other Objectives text description is required since you selected 'Other' ")
              }
          }

        
        // Method List
        var mthlist = document.getElementsByName('Method') 
        var mthtxt = ""
        var cnt = 0
        var mthTextTest = 0
        for(var i=0; i<mthlist.length;i++) {
            if (mthlist[i].checked) {

                var Control = mthlist[i].parentNode.innerHTML;
                var Control1 = Control.split(">");
                var Control2 = String(Control1[1])
                Control2 = Control2.replace(/[\n\r]/g, '');
                Control2 = Control2.substr(1);
                Method = Control2
                if(cnt == 0){
                  mthtxt = Method
                  cnt = 1
                } else {
                  mthtxt = mthtxt + "; " + Method
                }

                if(Method == "Other - Please specify in text box"){
                  mthTextTest = 1
                }
            }

        }

        if (cnt == 0){
          errorlist.push(" At least one selected method is required")
        }

        if(mthTextTest == 1){

          if(document.getElementById('id_Methods_Explained').value == ""){
             errorlist.push(" Other Methods text description is required since you selected 'Other' ")
          }
        }

        var checked = 0
        var ndereq = 0

        // Effectiveness Determination
        // If effectiveness determined is successful then hide and don't worry about 2nd set of PECE questions, otherwise show them
        var nyireq2nd = 0
        list = document.getElementsByName('Effective_Determined')
        var effval = 0
        for(var i=0; i<list.length;i++) {
          if (document.getElementsByName('Effective_Determined')[i].checked) {
              try{
                effval = document.getElementsByName('Effective_Determined')[i].value
              } catch(err){
              }
              var selector = 'label[for=' + list[i].id + ']';
              var label = document.querySelector(selector);
              var text = label.innerHTML;
              var textsplit = text.split(">")[1]
              var Control2 = String(textsplit)
              Control2 = Control2.replace(/[\n\r]/g, '');
              Control2 = Control2.substr(1);
              if (effval == 1 | effval == 4 | effval == 10 | effval == 17 | effval == 33 | effval == 39 | effval == 42 | effval == 45 | effval == 48 | effval == 51 | effval == 54 | effval == 57 | effval == 60 | effval == 7 | effval == 11 | effval == 14 | effval == 18 | effval == 21 | effval == 24 | effval == 27 | effval == 30 | effval == 36 | effval == 63 | effval == 66 | effval == 69){
                var nothing = ""
              } else if (effval > 0){
                nyireq2nd = 1
              } else {
                errorlist.push(" Please select an effectiveness determination")
              }
          }
        }


        // Effectivenss Statements List
        var efflist = document.getElementsByName('Effectiveness_Statement') 
        var efftxt = ""
        var cnt = 0
        var effTextTest = 0
        for(var i=0; i<efflist.length;i++) {
            if (efflist[i].checked) {

                var Control = efflist[i].parentNode.innerHTML;
                var Control1 = Control.split(">");
                var Control2 = String(Control1[1])
                Control2 = Control2.replace(/[\n\r]/g, '');
                Control2 = Control2.substr(1);
                EffStat = Control2
                if(cnt == 0){
                  efftxt = EffStat
                  cnt = 1
                } else {
                  efftxt = efftxt + "; " + EffStat
                }

                if(EffStat == "Other - Please specify in text box"){
                  effTextTest = 1
                }
            }

        }

        if (cnt == 0){
          errorlist.push(" At least one selected effectiveness statement is required")
        } else {
          document.getElementById('EffectiveList1').innerHTML = mthtxt
          document.getElementById('effreview').style.color = "black"
          document.getElementById('effstatcolor').style.color = "black"
        }

        if(effTextTest == 1){

          if(document.getElementById('id_Effective_Explained').value == ""){
             errorlist.push(" Other Effectiveness Description Statement text is required since you selected 'Other' ")
          }
        }


    }







    //Threats//
    cnt = 0
    list = document.getElementsByName("Threat")
    var Outputlist = ""
    for(var i=0; i<list.length;i++) {
      if (document.getElementsByName("Threat")[i].checked) {
        Control = document.getElementsByName("Threat")[i].parentNode.innerHTML;
        Control1 = Control.split(">");
        var Control2 = String(Control1[1])
        Control2 = Control2.replace(/[\n\r]/g, '');
        Control2 = Control2.substr(1);

        if (cnt == 0){
          Outputlist = Outputlist + Control2
          cnt = cnt + 1
        }
        else {
          Outputlist = Outputlist + ", " + Control2
        }
      }
    }

    if(Outputlist == ""){
        errorlist.push(" At least 1 threat is required")
    }

    


    // var list = document.getElementsByName('Threat')
    // for(var i=0; i<list.length;i++) {
    //   if (list[i].checked) {
    //     Control = list[i].parentNode.innerHTML;
    //     Control1 = Control.split(">");
    //     var Control2 = String(Control1[1])
    //     Control2 = Control2.replace(/[\n\r]/g, '');
    //     Control2 = Control2.substr(1);

    //     if (Control2 == "AGRICULTURAL CONVERSION (Tillage Risk)"){
    //         if(document.getElementById('id_Ag_Conversion_Explain').value > ""){
    //         }else{
    //             errorlist.push(" Explain Agricultural Conversion Threat Reduction Effectiveness") 
    //         }
    //     }

    //     if (Control2 == "CONIFER ENCROACHMENT"){
    //         if(document.getElementById('id_Conifer_Encroach_Explain').value > ""){
    //         }else{
    //             errorlist.push(" Explain Conifer Encroachment Threat Reduction Effectiveness") 
    //         }
    //     }

    //     if (Control2 == "OIL &amp; GAS DEVELOPMENT"){
    //         if(document.getElementById('id_Oil_Gas_Explain').value > ""){
    //         }else{
    //             errorlist.push(" Explain Oil and Gas Threat Reduction Effectiveness") 
    //         }
    //     }

    //     if (Control2 == "FIRE"){
    //         document.getElementById('Fire1').style.display = "block";
    //         if(document.getElementById('id_Fire_Explain').value > ""){
    //         }else{
    //             errorlist.push(" Explain Fire Threat Reduction Effectiveness") 
    //         }  
    //     }

    //     if (Control2 == "FERAL EQUIDS"){
    //         if(document.getElementById('id_Feral_Equids_Explain').value > ""){
    //         }else{
    //             errorlist.push(" Explain Feral Equids Threat Reduction Effectiveness") 
    //         }
    //     }

    //     if (Control2 == "IMPROPER GRAZING / RANGE MANAGEMENT"){
    //         if(document.getElementById('id_Improper_Grazing_Explain').value > ""){
    //         }else{
    //             errorlist.push(" Explain Improper Grazing / Range Management Threat Reduction Effectiveness")
    //         }
    //     }

    //     if (Control2 == "INFRASTRUCTURE (Roads, Powerlines, Renewable Energy)"){
    //         if(document.getElementById('id_Infrastructure_Explain').value > ""){
    //         }else{
    //             errorlist.push(" Explain Infrastructure Threat Reduction Effectiveness")
    //         }
    //     }

    //     if (Control2 == "ISOLATED / SMALL POPULATION SIZE"){
    //         if(document.getElementById('id_Isolated_Explain').value > ""){
    //         }else{
    //             errorlist.push(" Explain Isolated / Small Population Size Threat Reduction Effectiveness")
    //         }
    //     }

    //     if (Control2 == "MINING"){
    //         if(document.getElementById('id_Mining_Explain').value > ""){
    //         }else{
    //             errorlist.push(" Explain Mining Threat Reduction Effectiveness") 
    //         }
    //     }

    //     if (Control2 == "INVASIVES (Annual Grasses and Noxious Weeds)"){
    //         if(document.getElementById('id_Invasives_Explained').value > ""){
    //         }else{
    //             errorlist.push(" Explain Invasives Threat Reduction Effectiveness")
    //         }
    //     }

    //     if (Control2 == "RECREATION"){
    //         if(document.getElementById('id_Recreation_Explain').value > ""){
    //         }else{
    //             errorlist.push(" Explain Recreation Threat Reduction Effectiveness")
    //         }
    //     }

    //     if (Control2 == "SAGEBRUSH LOSS or DEGRADATION"){
    //         if(document.getElementById('id_Sagebrush_Loss_Explain').value > ""){
    //         }else{
    //             errorlist.push(" Explain Sagebrush Loss or Degradation Threat Reduction Effectiveness")
    //         }
    //     }
        
    //     if (Control2 == "URBAN DEVELOPMENT"){
    //         if(document.getElementById('id_Urban_Devel_Explain').value > ""){
    //         }else{
    //             errorlist.push(" Explain Urban Development Threat Reduction Effectiveness")
    //         } 
    //     }
    //   }
    // }

    //Documentation//
    
    try{
        var myTableDiv = document.getElementById("docreview")
        try{
            myTableDiv.removeChild(myTableDiv.childNodes[0]);
        }catch(err){

        }
        
        var table = document.createElement('TABLE')
        var tableBody = document.createElement('TBODY')

        table.border = '1'
        table.appendChild(tableBody);

        var heading = new Array();
        heading[0] = "File Type"
        heading[1] = "Document Description"
        heading[2] = "Document Name"

        var docs = new Array()

        for (i = 0; i < 100; i++) {
            try{
                var ft = document.getElementById("id_form-" + i + "-File_Type")
                var ftsel = ft.options[ft.selectedIndex].value;
                var dd = document.getElementById("id_form-" + i + "-Document_Description").value
                var dn = document.getElementById("id_form-" + i + "-Document_Name").value
                docs[i] = new Array(ftsel, dd, dn)
            }catch(err){
                break;
            }
        }

        //TABLE COLUMNS
        var tr = document.createElement('TR');
        tableBody.appendChild(tr);
        for (i = 0; i < heading.length; i++) {
            var th = document.createElement('TH')
            th.width = '300';
            th.appendChild(document.createTextNode(heading[i]));
            tr.appendChild(th);
        }

        //TABLE ROWS
        for (i = 0; i < docs.length; i++) {
            var tr = document.createElement('TR');
            for (j = 0; j < docs[i].length; j++) {
                var td = document.createElement('TD')
                td.appendChild(document.createTextNode(docs[i][j]));
                tr.appendChild(td)
            }
            tableBody.appendChild(tr);
        }

        myTableDiv.appendChild(table);

        

        var myTableCells = table
        for (var i = 0, row; row = table.rows[i]; i++) {
            for (var j = 0, col; col = row.cells[j]; j++) {
                if(j == 0 & myTableCells.rows[i].cells[j].innerHTML != "File Type"){
                    if(myTableCells.rows[i].cells[j].innerHTML == "---Select/Update File Type---"){
                        errorlist.push(" At least 1 File Type is missing")
                        break;
                    }
                }

                if(j == 1 & myTableCells.rows[i].cells[j].innerHTML != "Document Description"){
                    if(myTableCells.rows[i].cells[j].innerHTML == ""){
                        errorlist.push(" At least one File Description missing")
                        break;
                    }
                }
            }
        }

        var myTableCells = table
        for (var i = 0, row; row = table.rows[i]; i++) {
            for (var j = 0, col; col = row.cells[j]; j++) {
                if(j == 0 & myTableCells.rows[i].cells[j].innerHTML != "File Type"){
                    if(myTableCells.rows[i].cells[j].innerHTML == "---Select/Update File Type---"){
                        myTableCells.rows[i].cells[j].style.color = "red" 
                        myTableCells.rows[i].cells[j].style.fontWeight="bold";
                    }else{
                        myTableCells.rows[i].cells[j].style.color = "black" 
                        myTableCells.rows[i].cells[j].style.fontWeight="normal";
                    }
                }

                if(j == 1 & myTableCells.rows[i].cells[j].innerHTML != "Document Description"){
                    if(myTableCells.rows[i].cells[j].innerHTML == ""){
                        myTableCells.rows[i].cells[j].style.color = "red" 
                        myTableCells.rows[i].cells[j].style.fontWeight="bold";
                        myTableCells.rows[i].cells[j].innerHTML = '"REQUIRED"'
                    }else{
                        myTableCells.rows[i].cells[j].style.color = "black" 
                        myTableCells.rows[i].cells[j].style.fontWeight="normal";
                    }
                }
            }
        }

    // if(i > 1){
    //     }else{
    //         errorlist.push(" At least 1 document is required")
    //     }
    }catch(err){
        a = 1
    }


    var stalst = document.getElementById('StatesList').innerHTML
    var stalst1 = stalst.split(":")[1]
    if(stalst1 > "" & stalst1 != " "){
    }else{
        errorlist.push(" At least 1 state is required")
    } 

    var coulst = document.getElementById('CntsList').innerHTML
    var coulst1 = coulst.split(":")[1]
    if(coulst1 > "" & coulst1 != " "){
    }else{
        errorlist.push(" At least 1 county is required")
    } 

    //Collaborators//
    cnt = 0
    list = document.getElementsByName("Collab_Party")
    var Outputlist = ""
    for(var i=0; i<list.length;i++) {
      if (document.getElementsByName("Collab_Party")[i].checked) {
        Control = document.getElementsByName("Collab_Party")[i].parentNode.innerHTML;
        Control1 = Control.split(">");
        var Control2 = String(Control1[1])
        Control2 = Control2.replace(/[\n\r]/g, '');
        Control2 = Control2.substr(1);

        if (cnt == 0){
          Outputlist = Outputlist + Control2
          cnt = cnt + 1
        }
        else {
          Outputlist = Outputlist + ", " + Control2
        }
      }
    }


    if(Outputlist == ""){
        errorlist.push(" At least 1 Collaborator is required select None if no collaborators exist")
    }

    var nyireq = 1
    list = document.getElementsByName('Imp_Status')
    for(var i=0; i<list.length;i++) {
        if (document.getElementsByName('Imp_Status')[i].checked) {
            if(document.getElementsByName('Imp_Status')[i].value > 0){   
            }else{
                errorlist.push(" Implementation status is required") 
            }
            if(document.getElementsByName('Imp_Status')[i].value == 3){   
                nyireq = 0
            }
        }
    }


    if(nyireq == 1){

        var checked = 0
        list = document.getElementsByName('Reas_Certain')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Reas_Certain')[i].checked) {
                checked = 1
            }
        }
        if(checked == 0){
            errorlist.push(" Reasonable Certainty is required")
        }
    
        var checked = 0
        list = document.getElementsByName('Legal_Authority')
 
        for(var i=0; i<list.length;i++){
            if (document.getElementsByName('Legal_Authority')[i].checked) {
                checked = 1
            }
        }
        if(checked == 0){
            errorlist.push(" Legal Authority is required")
        }
        
        var checked = 0
        list = document.getElementsByName('Staff_Available')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Staff_Available')[i].checked) {
                checked = 1
            }
        }
        if(checked == 0){
            errorlist.push(" Staff Available is required")
        }

        var checked = 0
        list = document.getElementsByName('Regulatory_Mech')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Regulatory_Mech')[i].checked) {
                checked = 1
            }
        }
        if(checked == 0){
            errorlist.push(" Regulatory Mechanisms is required")
        }

        var checked = 0
        list = document.getElementsByName('Compliance')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Compliance')[i].checked) {
                checked = 1
            }
        }
        if(checked == 0){
            errorlist.push(" Compliance is required")
        }

        var checked = 0
        list = document.getElementsByName('Vol_Incentives')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Vol_Incentives')[i].checked) {
                checked = 1
            }
        }
        if(checked == 0){
            errorlist.push(" Voluntary Incentives is required")
        }
    }

    // var checked = 0
    // var ndereq = 0
    // list = document.getElementsByName('Effective_Determined')
    // for(var i=0; i<list.length;i++) {
    //     if (document.getElementsByName('Effective_Determined')[i].checked) {
    //         checked = 1
    //         if(document.getElementsByName('Effective_Determined')[i].value > 0){
    //         }else{
    //             errorlist.push(" The effectiveness status is required")
    //         }
    //         if(document.getElementsByName('Effective_Determined')[i].value == 1){   
    //             ndereq = 1
    //         }
    //     }
    // }

    // if(checked == 0){
    //     errorlist.push(" The effectiveness status is required")
    // }

    // var exptext = document.getElementById('id_Effective_Explained').value;
    // exptext = exptext.toString();
    // var n = exptext.length;

    // if(n > 0){
    // }else{
    //     errorlist.push(" Explain effectiveness is required")
    // }

    if(nyireq2nd == 1){
        

        var checked = 0
        list = document.getElementsByName('Reduce_Threats')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Reduce_Threats')[i].checked) {
                checked = 1
            }
        }
        if(checked == 0){
            errorlist.push(" Reduce Threats is required")
        }

        var checked = 0
        list = document.getElementsByName('Incremental_Objectives')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Incremental_Objectives')[i].checked) {
                checked = 1
            }
        }

        var checked = 0
        list = document.getElementsByName('Quantifiable_Measures')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('Quantifiable_Measures')[i].checked) {
                checked = 1
            }
        }
        if(checked == 0){
            errorlist.push(" Quantifiable Measures is required")
        }

        var checked = 0
        list = document.getElementsByName('AD_Strategy')
        for(var i=0; i<list.length;i++) {
            if (document.getElementsByName('AD_Strategy')[i].checked) {
                checked = 1
            }
        }
        if(checked == 0){
            errorlist.push(" Adaptive Management Strategy is required")
        }
    }

    var errorlist1 = "The following fields are required before you can submit this effort for approval: " + errorlist.toString();

    if(errorlist.length > 0){
        alert(errorlist1)
        event.preventDefault();
    }
}

function checklink(filepath) {
   var filep = filepath;
   var filp = filepath.substring(0,4);
   if (filp == "http"){
    window.open(filep);
    stopdoc = "Stop";
    event.preventDefault();
   }
}

function DeleteProject() {
  document.getElementById("deleteprj").name = "deleteapp";
  needToConfirm = false 
  confirmExit()

}

function showDiv() {
   document.getElementById('processingDiv1').style.display = "block";
   document.getElementById('DocText').style.display = "block";
}

function showDiv1() {
  if (stopdoc != "Stop"){
    document.getElementById('processingDiv1').style.display = "block";
    document.getElementById('DocText1').style.display = "block";
  }
}

function showDiv2() {
   document.getElementById('processingDiv1').style.display = "block";
   document.getElementById('DocText2').style.display = "block";
}

function checknull(){

    list = document.getElementsByName('Collab_Party');
    var removerest = 0
    for(var i=0; i<list.length;i++) {
        if(i == 10){
          if(document.getElementsByName('Collab_Party')[i].checked == true){
            removerest = 1
            alert("Collaborator value 'None' checked, any other existing collaborators will be unchecked")
            
          }
        }
    }


    if(removerest == 1){
      for(var i=0; i<list.length;i++) {
          if(i == 10){
            document.getElementsByName('Collab_Party')[i].checked = true
          }else{
            document.getElementsByName('Collab_Party')[i].checked = false
          }
      }
    }
}