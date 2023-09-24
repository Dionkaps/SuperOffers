const cron = require("node-cron");

const monthlyTask = cron.schedule("0 0 1 * *", () => {
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

const weeklyTask = cron.schedule("45 15 * * *", () => {
  const { exec } = require("child_process");

  const phpScriptPath = "testCriteria.php";

  const command = `php ${phpScriptPath}`;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing PHP script: ${error}`);
      return;
    }
    console.log(stdout);
  });
});

// Start both tasks
monthlyTask.start();
weeklyTask.start();

// You can add more logic or functionality here if needed
console.log("Tasks have been started.");
