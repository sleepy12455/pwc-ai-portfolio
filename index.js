require("dotenv").config();

const Anthropic = require("@anthropic-ai/sdk");
const readline = require("readline");

const client = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
});

const messages = [];

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

async function askQuestion() {
    rl.question("질문 >", async (question) => {

    try {
        messages.push({
            role: "user",
            content: question,
        });
        const response = await client.messages.create({
            model: "claude-sonnet-4-6",
            max_tokens: 500,
            messages,
        });
        console.log("Claude >");
        console.log(response.content[0].text);
    } catch(error) {
        console.error("오류:", error.message);
    } finally {askQuestion();}
})};

askQuestion();
