function LoadActivites() {
  
  var Control
  var Control1
  var Control2
  var Control3
  var UpdateControl
  var UpdateControl1
  var UpdateNum
  var UpdateNum1
  var UpdateNum2
  var Outputlist = "" 
  var Office
  var Agency
  var agenoff
  var offval
  var check = 0

  var updatelist1 = []
  var list = document.getElementsByName('TypeAct') 
  var updatelist = document.getElementsByName('Activity')


  var u = 0
    
  for(var j=0; j<updatelist.length;j++) {
      UpdateControl = updatelist[j].parentNode.innerHTML;
      UpdateControl1 = UpdateControl.split(">")[1];
      UpdateControl1 = String(UpdateControl1)
      UpdateControl1 = UpdateControl1.replace(/[\n\r]/g, '');
      UpdateControl1 = UpdateControl1.substr(1);
      updatelist1.push(UpdateControl1)
      val = 'id_Activity_' + (u)
      document.getElementById(val).style.display = "none";

      var offi = document.getElementById("id_Activity")
      offi.getElementsByTagName("li")[u].style.display="none";

      // document.getElementsByTagName("label")[t].style.display="none";
      u = u + 1
  }

 

  for(var i=0; i<list.length;i++) {
  
      if (list[i].checked) {
          Control = list[i].parentNode.innerHTML;
          Control1 = Control.split(">");
          Control2 = String(Control1[1])
          Control2 = Control2.replace(/[\n\r]/g, '');
          Control2 = Control2.substr(1);


          TypeActVal = Control2
          var u = 0

          for(var j=0; j<updatelist1.length;j++) {
              typact  = updatelist1[j];

              Control2 = typact.substr(typact.length - 21);
              typact = Control2.split("(")
              typact = typact[1]
              typact = typact.replace(")","")
              
              val = 'id_Activity_' + (u)
              if (typact == TypeActVal) {
                  document.getElementById(val).style.display = "inline-block";
                  var offi = document.getElementById("id_Activity")
                  offi.getElementsByTagName("li")[u].style.display = "inline-block";
              }

           
              u = u + 1
              check = 1
          }
      }else{
          Control = list[i].parentNode.innerHTML;
          Control1 = Control.split(">");
          Control2 = String(Control1[1])
          Control2 = Control2.replace(/[\n\r]/g, '');
          Control2 = Control2.substr(1);

          TypeActVal = Control2
          var u = 0
          for(var j=0; j<updatelist1.length;j++) {
              typact  = updatelist1[j];

              Control2 = typact.substr(typact.length - 21);
              typact = Control2.split("(")
              typact = typact[1]
              typact = typact.replace(")","")

              
              val = 'id_Activity_' + (u)

              if (typact == TypeActVal) {
                  document.getElementById(val).checked = false;
              }


              u = u + 1
          }

      }
  }

  if(check == 0){
    var selof = "*Select Activity Type(s) to view Activity Selections"
    var selofbold = selof.bold()
    document.getElementById('ActivityList').innerHTML = "Activities Selected: (Default All) " + selofbold
  }else{
    document.getElementById('ActivityList').innerHTML = "Activities Selected: (Default All)"
  }
} 

function LoadOffices() {

  var Control
  var Control1
  var Control2
  var Control3
  var UpdateControl
  var UpdateControl1
  var UpdateNum
  var UpdateNum1
  var UpdateNum2
  var Outputlist = "" 
  var Office
  var Agency
  var agenoff
  var offval
  var check = 0

  var updatelist1 = []
  var list = document.getElementsByName('Agency') 
  var updatelist = document.getElementsByName('Field_Office')


  var u = 0
    
  for(var j=0; j<updatelist.length;j++) {
      UpdateControl = updatelist[j].parentNode.innerHTML;
      UpdateControl1 = UpdateControl.split(">")[1];
      UpdateControl1 = UpdateControl1.replace(/[\n\r]/g, '');
      UpdateControl1 = UpdateControl1.substr(1);

      updatelist1.push(UpdateControl1)
      officeval = 'id_Field_Office_' + (u)
      document.getElementById(officeval).style.display = "none";

      var offi = document.getElementById("id_Field_Office")
      offi.getElementsByTagName("li")[u].style.display = "none";
      // document.getElementsByTagName("label")[t].style.display="none";

      u = u + 1
  }


  for(var i=0; i<list.length;i++) {

      if (list[i].checked) {
          Control = list[i].parentNode.innerHTML;
          Control1 = Control.split(">");
          Control2 = String(Control1[1])
          Control2 = Control2.replace(/[\n\r]/g, '');
          Control2 = Control2.substr(1);
          
          Agency = Control2

          var u = 0

          for(var j=0; j<updatelist1.length;j++) {
              agenoff  = updatelist1[j];
              Control3 = agenoff.split(", ");
              agenoff = Control3[2]
              
              offval = 'id_Field_Office_' + (u)

              if (agenoff == Agency) {
                  document.getElementById(offval).style.display = "inline-block";

                  var cnty = document.getElementById("id_Field_Office")
                  cnty.getElementsByTagName("li")[u].style.display = "inline-block";
              }

              u = u + 1
              check = 1
          }
      }else{
          Control = list[i].parentNode.innerHTML;
          Control1 = Control.split(">");
          Control2 = String(Control1[1])
          Control2 = Control2.replace(/[\n\r]/g, '');
          Control2 = Control2.substr(1);

          Agency = Control2
          var u = 0
          for(var j=0; j<updatelist1.length;j++) {
              agenoff  = updatelist1[j];
              Control3 = agenoff.split(", ");
              agenoff = Control3[2]
              
              offval = 'id_Field_Office_' + (u)

              if (agenoff == Agency) {

                  document.getElementById(offval).checked = false;
              }

              u = u + 1
          }

      }
  }

  if(check == 0){
    var selof = "*Select Agency(s) to view Field Office Selections"
    var selofbold = selof.bold()
    document.getElementById('FOList').innerHTML = "Offices Selected: (Default All) " + selofbold
  }else{
    document.getElementById('FOList').innerHTML = "Offices Selected: (Default All)"
  }
}   





function LoadSubActivites() {
  var Control
  var Control1
  var Control2
  var Control3
  var UpdateControl
  var UpdateControl1
  var UpdateNum
  var UpdateNum1
  var UpdateNum2
  var Outputlist = "" 
  var Office
  var Agency
  var agenoff
  var offval
  var check = 0

  var updatelist1 = []
  var list = document.getElementsByName('Activity') 
  var updatelist = document.getElementsByName('SubActivity')

  var u = 0
    
  for(var j=0; j<updatelist.length;j++) {
      UpdateControl = updatelist[j].parentNode.innerHTML;
      UpdateControl1 = UpdateControl.split("> ")[1];
      UpdateControl1 = UpdateControl.split(">")[1];
      UpdateControl1 = String(UpdateControl1)
      UpdateControl1 = UpdateControl1.replace(/[\n\r]/g, '');
      UpdateControl1 = UpdateControl1.substr(1);
      updatelist1.push(UpdateControl1)

      val = 'id_SubActivity_' + (u)
      document.getElementById(val).style.display = "none";
      var offi = document.getElementById("id_SubActivity")
      offi.getElementsByTagName("li")[u].style.display="none";

      u = u + 1
  }

  for(var i=0; i<list.length;i++) {
  
      if (list[i].checked) {
          Control = list[i].parentNode.innerHTML;
          Control1 = Control.split(">");
          Control2 = String(Control1[1])
          Control2 = Control2.replace(/[\n\r]/g, '');
          Control2 = Control2.substr(1);
          ActVal = Control2
           var u = 0

          for(var j=0; j<updatelist1.length;j++) {
              actsub  = updatelist1[j];

              if(actsub == 'Minimization  and Avoidance Strategies / BMPs (NON-REGULATORY MECHANISMS: (Plans, Strategies, BMPs))' || actsub == 'Non-regulatory Conservation Strategies (NON-REGULATORY MECHANISMS: (Plans, Strategies, BMPs))'){
                actsub = 'NON-REGULATORY CONSERVATION PLANS (Strategies, BMPs) (Non-Spatial Plan)'
              }else if(actsub == 'Compensatory Mitigation Plans (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Conservation Agreements (including but not limited to: CCAs, CCAAs, Farm Bill and other Incentive-based programs) (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Conservation Banking / Advanced Crediting Systems (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'County/Local Government Plan (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Federal Land Use Plan (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Fire Mutual Aid Agreement (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Fire Related Conservation Strategy (Pre-suppression Plans) (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Grazing and Rangeland Management Plans (Regulatory) (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Programmatic Candidate Conservation Agreement (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Programmatic Candidate Conservation Agreement with Assurances (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Reclamation Plan (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'State Conservation Plan (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))'){
                actsub = 'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders) (Non-Spatial Plan)'
              }else if(actsub == 'Conifer Removal (All Phases) (RESTORATION: Conifer Removal)'){
                  actsub = 'RESTORATION: Conifer Removal (Spatial Project)'
              }else if(actsub == 'Fence Marking (RESTORATION: Infrastructure Removal and Modification)' || actsub == 'Fence Modification (RESTORATION: Infrastructure Removal and Modification)' || actsub == 'Fence Removal (RESTORATION: Infrastructure Removal and Modification)' || actsub == 'Powerline Burial (RESTORATION: Infrastructure Removal and Modification)' || actsub == 'Powerline Retrofitting / Modification (RESTORATION: Infrastructure Removal and Modification)' || actsub == 'Structure Removal (RESTORATION: Infrastructure Removal and Modification)'){
                  actsub = 'RESTORATION: Infrastructure Removal and Modification (Non-Spatial Project)'
              }else if(actsub == 'Improved Grazing Practices (Rest, Rotation, Etc.) (RESTORATION: Livestock &amp; Rangeland Management)'){
                  actsub = 'RESTORATION: Livestock &amp; Rangeland Management (Non-Spatial Project)'
              }else if(actsub == 'Translocation (RESTORATION: Population Augmentation)'){
                  actsub = 'RESTORATION: Population Augmentation (Non-Spatial Project)'
              }else if(actsub == 'Rerouted Roads and/or Trails (RESTORATION: Travel Management)' || actsub == 'Road and Trail closure (RESTORATION: Travel Management)'){
                  actsub = 'RESTORATION: Travel Management (Non-Spatial Project)'
              }else if(actsub == 'Wild Equid Gather (RESTORATION: Wild Equid Management)' || actsub == 'Wild Equid Population Control (RESTORATION: Wild Equid Management)'){
                  actsub = 'RESTORATION: Wild Equid Management (Non-Spatial Project)'
              }else if(actsub == 'Annual Grass, Forb, or Noxious Weed Treatments (RESTORATION: Post-Disturbance and/or Habitat Enhancement)' || actsub == 'Area Closure (Area and/or Seasonal) (RESTORATION: Post-Disturbance and/or Habitat Enhancement)' || actsub == 'Fuels Management (RESTORATION: Post-Disturbance and/or Habitat Enhancement)' || actsub == 'Vegetation Management / Habitat Enhancement (RESTORATION: Post-Disturbance and/or Habitat Enhancement)' || actsub == 'Energy development reclamation with the goal of sagebrush restoration (RESTORATION: Post-Disturbance and/or Habitat Enhancement)'){
                  actsub = 'RESTORATION: Post-Disturbance and/or Habitat Enhancement (Spatial Project)'
              }else if(actsub == 'Conservation Easement (SAGEBRUSH PROTECTION)' || actsub == 'Fuel Breaks (SAGEBRUSH PROTECTION)' || actsub == 'Land Acquisition (SAGEBRUSH PROTECTION)'){
                  actsub = 'SAGEBRUSH PROTECTION (Spatial Project)'
              }

              val = 'id_SubActivity_' + (u)


              if (actsub == ActVal) {
                  document.getElementById(val).style.display = "inline-block";
                  var offi = document.getElementById("id_SubActivity")
                  offi.getElementsByTagName("li")[u].style.display="inline-block";
              }

      
              u = u + 1
              check = 1
          }
      }else{
          Control = list[i].parentNode.innerHTML;
          Control1 = Control.split(">");
          Control2 = String(Control1[1])
          Control2 = Control2.replace(/[\n\r]/g, '');
          Control2 = Control2.substr(1);
          ActVal = Control2

          var u = 0
          for(var j=0; j<updatelist1.length;j++) {
              actsub  = updatelist1[j];

              if(actsub == 'Minimization  and Avoidance Strategies / BMPs (NON-REGULATORY MECHANISMS: (Plans, Strategies, BMPs))' || actsub == 'Non-regulatory Conservation Strategies (NON-REGULATORY MECHANISMS: (Plans, Strategies, BMPs))'){
                actsub = 'NON-REGULATORY CONSERVATION PLANS (Strategies, BMPs) (Non-Spatial Plan)'
              }else if(actsub == 'Compensatory Mitigation Plans (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Conservation Agreements (including but not limited to: CCAs, CCAAs, Farm Bill and other Incentive-based programs) (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Conservation Banking / Advanced Crediting Systems (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'County/Local Government Plan (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Federal Land Use Plan (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Fire Mutual Aid Agreement (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Fire Related Conservation Strategy (Pre-suppression Plans) (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Grazing and Rangeland Management Plans (Regulatory) (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Programmatic Candidate Conservation Agreement (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Programmatic Candidate Conservation Agreement with Assurances (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'Reclamation Plan (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))' || actsub == 'State Conservation Plan (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))'){
                actsub = 'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders) (Non-Spatial Plan)'
              }else if(actsub == 'Conifer Removal (All Phases) (RESTORATION: Conifer Removal)'){
                  actsub = 'RESTORATION: Conifer Removal (Spatial Project)'
              }else if(actsub == 'Fence Marking (RESTORATION: Infrastructure Removal and Modification)' || actsub == 'Fence Modification (RESTORATION: Infrastructure Removal and Modification)' || actsub == 'Fence Removal (RESTORATION: Infrastructure Removal and Modification)' || actsub == 'Powerline Burial (RESTORATION: Infrastructure Removal and Modification)' || actsub == 'Powerline Retrofitting / Modification (RESTORATION: Infrastructure Removal and Modification)' || actsub == 'Structure Removal (RESTORATION: Infrastructure Removal and Modification)'){
                  actsub = 'RESTORATION: Infrastructure Removal and Modification (Non-Spatial Project)'
              }else if(actsub == 'Improved Grazing Practices (Rest, Rotation, Etc.) (RESTORATION: Livestock &amp; Rangeland Management)'){
                  actsub = 'RESTORATION: Livestock &amp; Rangeland Management (Non-Spatial Project)'
              }else if(actsub == 'Translocation (RESTORATION: Population Augmentation)'){
                  actsub = 'RESTORATION: Population Augmentation (Non-Spatial Project)'
              }else if(actsub == 'Rerouted Roads and/or Trails (RESTORATION: Travel Management)' || actsub == 'Road and Trail closure (RESTORATION: Travel Management)'){
                  actsub = 'RESTORATION: Travel Management (Non-Spatial Project)'
              }else if(actsub == 'Wild Equid Gather (RESTORATION: Wild Equid Management)' || actsub == 'Wild Equid Population Control (RESTORATION: Wild Equid Management)'){
                  actsub = 'RESTORATION: Wild Equid Management (Non-Spatial Project)'
              }else if(actsub == 'Annual Grass, Forb, or Noxious Weed Treatments (RESTORATION: Post-Disturbance and/or Habitat Enhancement)' || actsub == 'Area Closure (Area and/or Seasonal) (RESTORATION: Post-Disturbance and/or Habitat Enhancement)' || actsub == 'Fuels Management (RESTORATION: Post-Disturbance and/or Habitat Enhancement)' || actsub == 'Vegetation Management / Habitat Enhancement (RESTORATION: Post-Disturbance and/or Habitat Enhancement)' || actsub == 'Energy development reclamation with the goal of sagebrush restoration (RESTORATION: Post-Disturbance and/or Habitat Enhancement)'){
                  actsub = 'RESTORATION: Post-Disturbance and/or Habitat Enhancement (Spatial Project)'
              }else if(actsub == 'Conservation Easement (SAGEBRUSH PROTECTION)' || actsub == 'Fuel Breaks (SAGEBRUSH PROTECTION)' || actsub == 'Land Acquisition (SAGEBRUSH PROTECTION)'){
                  actsub = 'SAGEBRUSH PROTECTION (Spatial Project)'
              }
              
              val = 'id_SubActivity_' + (u)
              if (actsub == ActVal) {
                  document.getElementById(val).checked = false;
              }

              u = u + 1
          }

      }
  }

  if(check == 0){
    var selof = "*Select Activity(s) to view SubActivity Selections"
    var selofbold = selof.bold()
    document.getElementById('SubActivityList').innerHTML = "SubActivities Selected: (Default All) " + selofbold
  }else{
    document.getElementById('SubActivityList').innerHTML = "SubActivities Selected: (Default All)"
  }
}  


function LoadCounties() {
  var Control
  var Control1
  var Control2
  var Control3
  var UpdateControl
  var UpdateControl1
  var UpdateNum
  var UpdateNum1
  var UpdateNum2
  var Outputlist = "" 
  var cnty
  var State
  var agenoff
  var offval
  var check = 0

  var updatelist1 = []
  var list = document.getElementsByName('State') 
  var updatelist = document.getElementsByName('County')

  var u = 0
    
  for(var j=0; j<updatelist.length;j++) {
      UpdateControl = updatelist[j].parentNode.innerHTML;
      UpdateControl1 = UpdateControl.split(">")[1];
      UpdateControl1 = String(UpdateControl1)
      UpdateControl1 = UpdateControl1.replace(/[\n\r]/g, '');
      UpdateControl1 = UpdateControl1.substr(1);

      updatelist1.push(UpdateControl1)
      val = 'id_County_' + (u)
      document.getElementById(val).style.display = "none";
      var offi = document.getElementById("id_County")
      offi.getElementsByTagName("li")[u].style.display = "none";

      u = u + 1
  }

  for(var i=0; i<list.length;i++) {
      var t = 318
      if (list[i].checked) {
          Control = list[i].parentNode.innerHTML;
          Control1 = Control.split(">");
          Control2 = String(Control1[1])
          Control2 = Control2.replace(/[\n\r]/g, '');
          Control2 = Control2.substr(1);

          StateVal = Control2
          var u = 0
          for(var j=0; j<updatelist1.length;j++) {
              cnty  = updatelist1[j];
              Control2 = cnty.split(", ");
              cnty = Control2[1]
              
              val = 'id_County_' + (u)
              if (cnty == StateVal) {
                  document.getElementById(val).style.display = "inline-block";
                  var offi = document.getElementById("id_County")
                  offi.getElementsByTagName("li")[u].style.display="inline-block";
              }

              u = u + 1
              check = 1
          }
      }else{
          Control = list[i].parentNode.innerHTML;
          Control1 = Control.split(">");
          Control2 = String(Control1[1])
          Control2 = Control2.replace(/[\n\r]/g, '');
          Control2 = Control2.substr(1);

          StateVal = Control2
          var u = 0
          for(var j=0; j<updatelist1.length;j++) {
              cnty  = updatelist1[j];
              Control2 = cnty.split(", ");
              cnty = Control2[1]
              
              val = 'id_County_' + (u)

              if (cnty == StateVal) {
                  document.getElementById(val).checked = false;
              }

              u = u + 1
          }

      }
  }

  if(check == 0){
    var selof = "*Select County Type(s) to view Counties Selections"
    var selofbold = selof.bold()
    document.getElementById('CountyList').innerHTML = "Counties Selected: (Default All) " + selofbold
  }else{
    document.getElementById('CountyList').innerHTML = "Counties Selected: (Default All)"
  }
}   


function LoadLists(ListName, ListTitle, ListID) {

  var list  = document.getElementsByName(ListName)
  var Control;
  var Control1;
  var Control2;
  var Outputlist = ListTitle + '(Default All)'
  var cnt = 0
  var lstnm = String(ListName)
  var str = " OR ";
  var ORbold = str.bold();
  var listexist = 0

  if(ListName == "Start_Year"){
    var ss = document.getElementById('id_StartSelect')
    var ssnum = ss.options[ss.selectedIndex].innerHTML;
    if(ssnum == "----Choose an Equation----"){
      ssnum = "Equal To"
    }
  }

  

  if(ListName == "End_Year"){
    var es = document.getElementById('id_EndSelect')
    var ssnum = es.options[es.selectedIndex].innerHTML;
    
    if(ssnum == "----Choose an Equation----"){
      ssnum = "Equal To"
    }
  }

  
  

  for(var i=0; i<list.length;i++) {

      if (document.getElementsByName(ListName)[i].checked) {
          listexist = 1
          Control = document.getElementsByName(ListName)[i].parentNode.innerHTML
  
          Control1 = Control.split(">");
          
          Control2 = String(Control1[1])
          Control2 = Control2.replace(/[\n\r]/g, '');
          Control2 = Control2.substr(1);

          var listsplit = Outputlist.split(" <")[0];

          if (listsplit == ListTitle + '(Default All)'){
              if(ListName == "Start_Year" || ListName == "End_Year"){
                Outputlist =  ListTitle + ssnum + " " + Control2
              }else{
                Outputlist =  ListTitle + Control2
              }
          }else{
              Outputlist = Outputlist + ORbold + Control2
          }

      }else{

        if(ListName == 'Activity' & listexist == 0){
          var stract = "*Select Activity Type(s) to view Activity Selections"
          var Actbold = stract.bold()
          Outputlist = ListTitle + '(Default All) ' + Actbold
        }else if(ListName == 'Field_Office' & listexist == 0){
          var stroff = "*Select Agency(s) to view Field Office Selections"
          var Offbold = stroff.bold()
          Outputlist = ListTitle + '(Default All) ' + Offbold
        }else if(ListName == 'SubActivity' & listexist == 0){
          var strsact = "*Select Activity(s) to view SubActivity Selections"
          var Sactbold = strsact.bold();
          Outputlist = ListTitle + '(Default All) ' + Sactbold;
        }else if(ListName == 'County' & listexist == 0){
          var strcnty = "*Select State(s) to view County Selections"
          var Cntybold = strcnty.bold();
          Outputlist = ListTitle + '(Default All) ' + Cntybold;
        }
      }
  }

  document.getElementById(ListID).innerHTML = Outputlist

}

function DisplaySection(section, button){

  var sectiontype = section
  if (document.getElementById(sectiontype).style.display == "none"){
      document.getElementById(sectiontype).style.display = "inline-block"
      document.getElementById(button).value = "-"
  }
  else{
      document.getElementById(sectiontype).style.display = "none"
      document.getElementById(button).value = "+"
  }
  
}

function LoadKWText(){

    var str = " OR ";
    var ORbold = str.bold();
    var KW = document.getElementById('id_Key_Words').value;
    var KWlast = KW.slice(-1);
    var KWor = KW.replace(/,/g, ORbold)

    if(KWor.length > 0){
      KWT = 'Key Words Selected: ' + KWor
    }else{
      KWT = "Key Words Selected: (Default None)"
    }

    document.getElementById('KWList').innerHTML = KWT  
  }

function submitdata(){
    document.getElementById('viewresults').click();
}


function updatefields(){

    var wafwaval = document.getElementById('id_WAFWA_Zone');
    var strwa = wafwaval.options[wafwaval.selectedIndex].value;
    var showthr = 0
    
    if (document.getElementById("id_QueryType_0").checked == true){
      document.getElementById('statefws').style.display = "inline";
      document.getElementById('wafwafws').style.display = "inline";
      document.getElementById('dateeqfws').style.display = "inline";
      document.getElementById('sdfws').style.display = "inline";
      document.getElementById('fdfws').style.display = "inline";
      document.getElementById('fwsresponse').style.display = "none";
      if (strwa != ""){
        document.getElementById('showthr').style.display = "inline";
        document.getElementById('SelectWaf').style.display = "none";
      }
      else{
        document.getElementById('showthr').style.display = "none";
        document.getElementById('SelectWaf').style.display = "inline";
      }
      showthr = 1
      
    }
    if (document.getElementById("id_QueryType_1").checked == true){
      document.getElementById('statefws').style.display = "none";
      document.getElementById('wafwafws').style.display = "inline";
      document.getElementById('dateeqfws').style.display = "inline";
      document.getElementById('sdfws').style.display = "inline";
      document.getElementById('fdfws').style.display = "inline";
      document.getElementById('fwsresponse').style.display = "inline";

      document.getElementById("id_State").value = '';

      if (strwa != ""){
        document.getElementById('showthr').style.display = "inline";
        document.getElementById('SelectWaf').style.display = "none";
      }
      else{
        document.getElementById('showthr').style.display = "none";
        document.getElementById('SelectWaf').style.display = "inline";
      }
      showthr = 1
    }

    if (showthr == 0){
      document.getElementById('showthr').style.display = "none";
      document.getElementById('SelectWaf').style.display = "none";
    }
}

function updatethr(){
    var wafwaval = document.getElementById('id_WAFWA_Zone');
    var strwa = wafwaval.options[wafwaval.selectedIndex].value;
    var thrval = document.getElementById('id_Threat');
    var stval = document.getElementById('id_State');
    var strst = stval.options[stval.selectedIndex].value;

    if (strwa != ""){
      $('#id_Threat').empty();
      $('#id_State').empty();
      document.getElementById('showthr').style.display = "inline";
      document.getElementById('SelectWaf').style.display = "none";

      if (strwa == 1){
        var list = [['','---------'], ['1','Agricultural Conversion'], ['3','Energy Development'], ['7','Infrastructure'], ['10','Noxious Weeds / Annual Grasses']];
        var slist = [['','---------'], ['19433','AB'], ['4512','MT'], ['9826','NE'], ['9396','ND'], ['14797','SD'], ['19432','WY']];
      }

      if (strwa == 2){
        var list = [['','---------'], ['3','Energy Development'], ['7','Infrastructure'], ['9','Mining'], ['10','Noxious Weeds / Annual Grasses'], ['13','Urbanization']];
        var slist = [['','---------'], ['985','CO'], ['1992','ID'], ['4512','MT'], ['15561','UT'], ['19432','WY']];
      }

      if (strwa == 3){
        var list = [['','---------'], ['2','Conifer Encroachment'], ['4','Fire'], ['7','Infrastructure'], ['9','Mining'], ['10','Noxious Weeds / Annual Grasses'], ['13','Urbanization']];
        var slist = [['','---------'], ['1','AZ'], ['183','CA'], ['9901','NV'], ['15561','UT']];
      }

      if (strwa == 4){
        var list = [['','---------'], ['2','Conifer Encroachment'], ['4','Fire'], ['7','Infrastructure'], ['10','Noxious Weeds / Annual Grasses'], ['13','Urbanization']];
        var slist = [['','---------'], ['183','CA'], ['1992','ID'], ['4512','MT'], ['9901','NV'], ['12665','OR'], ['15561','UT'], ['19432','WY']];
      }

      if (strwa == 5){
        var list = [['','---------'], ['2','Conifer Encroachment'], ['4','Fire'], ['7','Infrastructure'], ['9','Mining'], ['10','Noxious Weeds / Annual Grasses'], ['13','Urbanization']];
        var slist = [['','---------'], ['183','CA'], ['9901','NV'], ['12665','OR']];
      }

      if (strwa == 6){
        var list = [['','---------'], ['1','Agricultural Conversion'], ['4','Fire'], ['7','Infrastructure'], ['8', 'Isolated  / Small Population Size'], ['10','Noxious Weeds / Annual Grasses']];
        var slist = [['','---------'], ['12665','OR'], ['18333','WA']];
      }

      if (strwa == 7){
        var list = [['','---------'], ['2','Conifer Encroachment'], ['3','Energy Development'], ['7','Infrastructure'], ['10','Noxious Weeds / Annual Grasses']];
        var slist = [['','---------'], ['1','AZ'], ['985','CO'], ['15561','UT']];
      }

      for (var j=0; j<list.length; j++){
          var option = document.createElement("option");
          option.text = list[j][1]; option.value = list[j][0];
          thrval.appendChild(option)
        }

        for (var k=0; k<slist.length; k++){
          var options = document.createElement("option");
          options.text = slist[k][1]; options.value = slist[k][0];
          stval.appendChild(options)
        }
    }
    else{
      document.getElementById('showthr').style.display = "none";
      document.getElementById('SelectWaf').style.display = "inline";

      $('#id_State').empty();
      var slist = [['','---------'], ['1','AZ'], ['183','CA'], ['985','CO'], ['1992','ID'], ['4512','MT'], ['9826','NE'], ['9396','ND'], ['9901','NV'], ['12665','OR'], ['14797','SD'], ['15561','UT'], ['18333','WA'], ['19432','WY'], ['19433','AB']];
      for (var k=0; k<slist.length; k++){
          var options = document.createElement("option");
          options.text = slist[k][1]; options.value = slist[k][0];
          stval.appendChild(options)
        }
    }

    if (strst != ""){
      document.getElementById("id_State").value = strst;
    }
}


function updatemz(){

    var stval = document.getElementById('id_State');
    var strst = stval.options[stval.selectedIndex].value;
    var wafwaval = document.getElementById('id_WAFWA_Zone');
    var strwa = wafwaval.options[wafwaval.selectedIndex].value;
    var thrval = document.getElementById('id_Threat');
    var showthr = 0;

    if (strst != ""){
      $('#id_WAFWA_Zone').empty();

      if (strst == 19433){
        var list = [['1','I']];
        var tlist = [['','---------'], ['1','Agricultural Conversion'], ['3','Energy Development'], ['7','Infrastructure'], ['10','Noxious Weeds / Annual Grasses']];
        showthr = 1;
      }

      if (strst == 1){
        var list = [['','---------'], ['3','III'], ['7','VII']];
      }

      if (strst == 183){
        var list = [['','---------'], ['5','V']];
      }
      if (strst == 985){
        var list = [['','---------'], ['2','II'], ['7','VII']];
      }

      if (strst == 1992){
        var list = [['','---------'], ['2','II'], ['4','IV']];  
      }


      if (strst == 4512){
        var list = [['','---------'], ['1','I'], ['2','II'], ['4','IV']]; 
      }


      if (strst == 9286){
        var list = [['1','I']];
        var tlist = [['','---------'], ['1','Agricultural Conversion'], ['3','Energy Development'], ['7','Infrastructure'], ['10','Noxious Weeds / Annual Grasses']];
        showthr = 1;
      }

      

      if (strst == 9901){
        var list = [['','---------'], ['3','III'], ['4','IV'], ['5','V']];
      }
      if (strst == 9396){
        var list = [['1','I']];
        var tlist = [['','---------'], ['1','Agricultural Conversion'], ['3','Energy Development'], ['7','Infrastructure'], ['10','Noxious Weeds / Annual Grasses']];
        showthr = 1
      }
      if (strst == 12665){
        var list = [['','---------'], ['4','IV'], ['5','V'], ['6','VI']];
      }
      if (strst == 14797){
        var list = [['1','I']];
        var tlist = [['','---------'], ['1','Agricultural Conversion'], ['3','Energy Development'], ['7','Infrastructure'], ['10','Noxious Weeds / Annual Grasses']];
        showthr = 1
      }
      if (strst == 15561){
        var list = [['','---------'], ['2','II'], ['3','III'], ['4','IV'], ['7','VII']];
      }
      if (strst == 18333){
        var list = [['6','VI']];
        var tlist = [['','---------'], ['1','Agricultural Conversion'], ['4','Fire'], ['7','Infrastructure'], ['10','Noxious Weeds / Annual Grasses']];
        showthr = 1
      }
      if (strst == 19432){
        var list = [['','---------'], ['1','I'], ['2','II'], ['4','IV']];
      }


      for (var j=0; j<list.length; j++){
          var option = document.createElement("option");
          option.text = list[j][1]; option.value = list[j][0];
          wafwaval.appendChild(option)
        }

        if (showthr == 1){
          $('#id_Threat').empty();
          document.getElementById('showthr').style.display = "inline";
        document.getElementById('SelectWaf').style.display = "none";
          for (var l=0; l<tlist.length; l++){
            var options = document.createElement("option");
            options.text = tlist[l][1]; options.value = tlist[l][0];
            thrval.appendChild(options)
          }
      }

    }
    else{
      
      $('#id_WAFWA_Zone').empty();
      var list = [['','---------'], ['1','I'], ['2','II'], ['3','III'], ['4','IV'], ['5','V'], ['6','VI'], ['7','VII']];
      for (var k=0; k<list.length; k++){
          var option = document.createElement("option");
          option.text = list[k][1]; option.value = list[k][0];
          wafwaval.appendChild(option)
        }

        document.getElementById('showthr').style.display = "none";
      document.getElementById('SelectWaf').style.display = "inline";
    }

    if (strwa != ""){
      document.getElementById("id_WAFWA_Zone").value = strwa;
    }
}