"""This file contains the prompts for the app.
The prompts are stored as a list of dictionaries, where each dictionary contains the role of the speaker and the content of the message.
The roles are "system", "user", and "assistant". The content is a string.
"""

MESSAGES = [
    {
        "role": "system",
        "content": """Your task is to completely paraphrase text while still providing the same information and meaning.
Your main goal is to get a very high level of Perplexity and Burstiness (A document's perplexity is a measurement of the randomness of the text and A document's burstiness is a measurement of the variation in perplexity). 

You have to follow these rules:
        
- The most important thing is to make your text sound like it was written by a human!
- You can and should switch some sentences around, and you can also add or remove paragraphs.
- Add or remove sentences as needed.
- Vary sentence length and structure, and try to not repeat words or phrases.
- Ensure that the text is not uniform.
- Use original, never-seen-before utterances that are improvised on the spot entirely themed on the talking point.
- Use strong choice words to express your raw and candid emotions.
- DO NOT talk in a monotonous manner, instead, sound more relaxed, casual, and a bit humorous.
- Don't use too many technical terms, instead, use more common words.
- Avoid the same structure, instead, write more freely.
- Talk naturally, just like a human would.
- Change the sentence structure and word choice to reflect the same meaning.
- The paraphrased text should be readable and make sense.
- Don't make it more complicated, instead focus on making it more unique.
- Moreover, it's also very important that you keep the style. If it's a poem, make sure it still sounds like one after paraphrasing it.
- Talk naturally. Don't use too many difficult terms, instead, use more common words.
- Write in a relaxed and casual manner.
- Make your text more random. Change words to more natural ones.""",
    },
    {
        "role": "user",
        "content": """Gaining confidence and staying motivated can be challenging, especially when we face difficult situations or setbacks in our lives. However, with the right mindset and approach, you can build your confidence and motivation levels and achieve your goals. In this blog, I will share some tips and strategies that can help you boost your confidence and motivation.

    1. Set Clear Goals: Setting clear and achievable goals is the first step towards building confidence and motivation. Write down your goals and make sure they are specific, measurable, and time-bound. Break them down into smaller milestones and track your progress regularly. Celebrate your accomplishments and learn from your mistakes.
    
    2. Practice Self-Care: Taking care of yourself is essential for building confidence and motivation. Eat healthy foods, get enough sleep, exercise regularly, and make time for activities that you enjoy. Taking care of your physical and mental health will help you feel better about yourself and increase your motivation levels.
    
    3. Build a Support System: Surround yourself with positive and supportive people who believe in you and your abilities. Seek out mentors, coaches, or friends who can provide guidance and encouragement when you need it. Join groups or communities that share your interests and values.
    
    4. Learn New Skills: Learning new skills can help you gain confidence and motivation by expanding your knowledge and abilities. Take courses, read books, or attend workshops to improve your skills and knowledge. Look for opportunities to apply what you have learned in real-life situations.
    
    5. Embrace Failure: Failure is a natural part of the learning process, and it can help you grow and become more resilient. Embrace failure as an opportunity to learn and grow, and don't let it define your worth or abilities. Remember that even the most successful people have failed many times before achieving their goals.
    
    6. Challenge Negative Self-Talk: Negative self-talk can undermine your confidence and motivation. Challenge negative thoughts and replace them with positive ones. Practice self-affirmations, and remind yourself of your strengths and accomplishments. Focus on the progress you have made, rather than the setbacks you have faced.
    
    7. Take Action: Finally, taking action is the key to building confidence and motivation. Set clear goals, develop a plan, and take small steps towards achieving them. Celebrate your progress along the way, and don't be afraid to ask for help when you need it.
    
    In conclusion, building confidence and staying motivated is a lifelong journey that requires consistent effort and practice. By setting clear goals, practicing self-care, building a support system, learning new skills, embracing failure, challenging negative self-talk, and taking action, you can increase your confidence and motivation levels and achieve your goals. Remember to be patient with yourself, and don't give up when faced with obstacles. With persistence and dedication, you can build the confidence and motivation you need to succeed.""",
    },
    # {
    #     "role": "assistant",
    #     "content": """
    #     """,
    # },
]