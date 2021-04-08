//This function is called when the "Plant It!" button is clicked
function planted() {
    getBedNum()
    // edits on html DOCUMENT, in MAIN form, specifically the BED text to be the VALUE of url parameter (this case, 100)
    document.main.bed.value = bedNum;
    // Retrieves the name inserted in the form
    var name = document.main.owner.value;
    // Retrieves the plant name in the form
    var plant = document.main.plant_species.value;
    // Returns a personalized message
    alert("Thanks " + name + " for planting " + plant + " in bed " + bedNum);
}
function getBedNum() {
    // Saves the query string on the end of the URL 
    // (URL www.blah.com/form?bed=100)
    const queryString = window.location.search;
    // (urlParams = "?bed=100")
    const urlParams = new URLSearchParams(queryString);
    // Looks for key ('bed') in urlParams
    const bedNum = new Number(urlParams.get('bed'));
    window.location.href = "/form?bed=" + bedNum;
}