const schedule = require("node-schedule");

//Runs every 1st of the month at 00:00
const job = schedule.scheduleJob("0 0 1 * *", function () {
  //DO CODE GIA 31 TOU PROIGOUMENOU MHNA PRIN TO RESET

  //Reset tokens before setting them
  var totalTokens = 0;
  const { exec } = require("child_process");

  const phpScriptPath = "getAmountOfUsers.php";

  const command = `php ${phpScriptPath}`;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing PHP script: ${error}`);
      return;
    }
    //Calculate total amount of tokens
    totalTokens = stdout * 100;
    console.log("Total tokens: " + totalTokens);
  });
});