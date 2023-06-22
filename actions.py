import openai

def process_with_gpt(input_text):
        # Authenticate with the OpenAI API
        openai.api_key = "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"

        # Set the model and parameters
        model_engine = "text-davinci-002"
        prompt = input_text
        temperature = 0.5
        max_tokens = 60

        # Generate text using GPT-3
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )

        # Return the generated text
        return response.choices[0].text