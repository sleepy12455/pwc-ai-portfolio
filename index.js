require("dotenv").config();

const Anthropic = require("@anthropic-ai/sdk");
const readline = require("readline");

const client = new Anthropic({
    apikey: process.env.Anthropic_API_KEY,
});

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.question("질문 > ", async (question) => {
    try {
        const response = await client.messages.create({
            model: "claude-sonnet-4-6",
            max_tokens: 500,
            messages: [
                {
                    role: "user",
                    content: question,
                },
            ],
        });
        console.log("Claude >");
        console.log(response.content[0].text);
    } catch(error) {
        console.error("오류:", error.message);
    } finally {
        rl.close();
    }
});