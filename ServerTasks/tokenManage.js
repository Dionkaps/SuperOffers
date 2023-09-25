const cron = require("node-cron");

const monthlyTask = cron.schedule("0 0 1 * *", () => {
  //Reset tokens before setting them
  let totalTokens = 0;
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

    //Code for splitting tokens between users
    const phpScriptPath1 = "splitTokens.php";

    const command1 = `php ${phpScriptPath1} ${totalTokens}`;

    exec(command1, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing PHP script: ${error}`);
        return;
      }
    });
  });
});

const weeklyTask = cron.schedule("0 0 * * 0", () => {
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

//Start both tasks
monthlyTask.start();
weeklyTask.start();

console.log("Tasks have been started.");
