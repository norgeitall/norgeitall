import fetch from "node-fetch";
import { schedule } from "@netlify/functions";
const BUILD_HOOK =
  "https://api.netlify.com/build_hooks/67b9b0990ed4f0891dce7213";
const handler = schedule("35 4 * * *", async () => {
  await fetch(BUILD_HOOK, {
    method: "POST",
  }).then((response) => {
    console.log("Build hook response:", response);
  });

  return {
    statusCode: 200,
  };
});

export { handler };
