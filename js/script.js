String.prototype.getFCE = function() {
    if (this.charAt(6) == "H") return 0.5;
    else if (this.charAt(6) == "Y") return 1.0;
    else console.log("Should not get here.");
}

String.prototype.getDesignator = function() {
    return this.substring(0, 3);
}

var ASSPE1689_ARRAY = {"Req1": ["0.5",  "CSC148H1", "CSC150H1"],
"Req2": ["1 Requirement", "from Req3, Req4"],
"Req3": ["1.0", "CSC165H1", "CSC236H1"],
"Req4": ["0.5",  "CSC240H1"],
"Req5": ["1.0", "MAT135H1", "MAT136H1", "MAT135Y1", "MAT137Y1", "MAT157Y1"],
"Req6": ["ALL", "CSC207H1", "CSC209H1", "CSC258H1"],
"Req7": ["0.5",  "CSC263H1", "CSC265H1"],
"Req8": ["0.5",  "MAT221H1", "MAT223H1", "MAT240H1"],
"Req9": ["0.5",  "STA247H1", "STA255H1", "STA257H1"],
"Req10": ["ALL", "CSC369H1"],
"Req11": ["0.5",  "CSC373H1", "CSC375H1"],
"Req12": ["1.5", "400 Level CSC Courses", "BCB410H1", "BCB420H1", "BCB430Y1", "ECE489H1"],
"Req13": ["3.5", "300+ Level CSC Courses ", "BCB410H1", "BCB420H1", "BCB430Y1", "ECE385H1", "ECE489H1", "MAT224H1", "MAT235Y1", "MAT237Y1", "MAT257Y1", "MAT 300/400+ excluding 329Y, 390H & 391H", "STA248H1", "STA261H1", "STA 300-level/ C-level courses, higher"],
"Req14": ["No more than 2.0", "MAT COURSES", "STA COURSES", "in Req12, Req13"],
"Req15": ["No more than 1.0", "CSC490H1", "CSC491H1", "CSC494H1", "CSC495H1", "BCB430Y1", "in Req12, Req13"],
"Req16": ["0.5",  "CSC318H1", "CSC404H1", "CSC411H1", "CSC418H1", "CSC420H1", "CSC428H1", "CSC454H1", "CSC485H1", "CSC490H1", "CSC491H1", "CSC494H1", "CSC495H1", "CSC301H1", "in Req12, Req13"],
"Req17": ["No more than 0.5", "CSC396Y0", "in Req13"]


}

var ASSPE1689 = "(Req1) At least 0.5 Credits from CSC148H1 or CSC150H1(Req2) At least 1 Requirement from Req3 or Req4(Req3) At least 1.0 Credit from CSC165H1 or CSC236H1(Req4) At least 0.5 Credits from CSC240H1(Req5) At least 1.0 Credit from MAT135H1 or MAT136H1 or MAT135Y1 or MAT137Y1 or MAT157Y1(Req6) All of CSC207H1 and CSC209H1 and CSC258H1	(Req7) At least 0.5 Credits from CSC263H1 or CSC265H1(Req8) At least 0.5 Credits from MAT221H1 or MAT223H1 or MAT240H1(Req9) At least 0.5 Credits from STA247H1 or STA255H1 or STA257H1	(Req10) All of CSC369H1(Req11) At least 0.5 Credits from CSC373H1 or CSC375H1(Req12) At least 1.5 Credits from '400 Level CSC Courses' or BCB410H1 or BCB420H1 or BCB430Y1 or ECE489H1(Req13) At least 3.5 Credits from '300+ Level CSC Courses ' or BCB410H1 or BCB420H1 or BCB430Y1 or ECE385H1 or ECE489H1 or MAT224H1 or MAT235Y1 or MAT237Y1 or MAT257Y1 or 'MAT 300/400+ excluding 329Y, 390H & 391H' or STA248H1 or STA261H1 or 'STA 300-level/ C-level courses and higher'(Req14) No more than 2.0 Credits from 'MAT COURSES' or 'STA COURSES' in Req12 or Req13(Req15) No more than 1.0 Credit from CSC490H1 or CSC491H1 or CSC494H1 or CSC495H1 or BCB430Y1 in Req12 or Req13(Req16) At least 0.5 Credits from CSC318H1 or CSC404H1 or CSC411H1 or CSC418H1 or CSC420H1 or CSC428H1 or CSC454H1 or CSC485H1 or CSC490H1 or CSC491H1 or CSC494H1 or CSC495H1 or CSC301H1 in Req12 or Req13(Req17) No more than 0.5 Credits from CSC396Y0 in Req13(Req18) Note: Last updated with the 2015-2016 Calendar."

window.onload = function() {
    // console.log("CSC148H1".getFCE());
    // console.log(ASSPE1689);
    var singleSubjectPost = ASSPE1689
    console.log(calculate(parser(singleSubjectPost)));
}

function parser(reqs) {

    function isAtLeastFrom(req_split) {
        /* At least ... credit(s) from ... */
        /* e.g. (Req1) At least 0.5 Credits from CSC148H1 or CSC150H1 */
        return req_split.splice(1, 2).join(" ") == "At least" && req_split.join("").indexOf("Req") == -1;
    }

    var req = reqs.split("(Req");
    var req_array = [];

    for (var i = 0; i < req.length; i ++) {
        if (req[i] != ""){
            req_split = req[i].split(" ");
            req_array.push(req_split);
        }
    }
    return req_array;
}

function calculate(reqs) {
    for (var i = 0; i < reqs.length; i ++) {
        console.log(reqs[i]);
    }
}
