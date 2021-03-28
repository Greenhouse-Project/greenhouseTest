//This function is called when the "Plant It!" button is clicked
function planted() {
    // Saves the query string on the end of the URL 
    // (URL www.blah.com/form?bed=100)
    const queryString = window.location.search;
    // (urlParams = "?bed=100")
    const urlParams = new URLSearchParams(queryString);
    // Looks for key ('bed') in urlParams
    const bedNum = new Number(urlParams.get('bed'));
    // edits on html DOCUMENT, in MAIN form, specifically the BED text to be the VALUE of url parameter (this case, 100)
    document.main.bed.value = bedNum;
    // Retrieves the name inserted in the form
    var name = document.main.owner.value;
    checkPass()
    // Retrieves the plant name in the form
    var plant = document.main.plant_species.value;
    // Returns a personalized message
    alert("Thanks " + name + " for planting " + plant + " in bed " + bedNum);
}
// compare used password to db password
// function checkPass() {
//     var pass = document.main._password.value;
//     const db = process.env.DATABASE_URL

//     try {
        
    // } catch (err) {
    //     console.error(err);

    // }
// }
// const { Pool } = require('pg');
// const conn = new Pool({ connectionString: process.env.DATABASE_URL });

// // Not used
// async function displaytable(req, res) {
//     try {
//         const db = await conn.connect()
//         const result = await db.query('SELECT * FROM greenhouse')
//         const results = { greenhouse: (result) ? result.rows : null };
//         res.render('/form', results);
//         db.release();
//     } catch (err) {
//         console.error(err);
//         req.send("Error " + err);
//     }
    
// }