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
- Aim for a mix of short and long sentences.
- Vary sentence length and structure, and try to not repeat words or phrases.
- Ensure that the text is not uniform.
- Use original, never-seen-before utterances that are improvised on the spot entirely themed on the talking point.
- Use strong choice words to express your raw and candid emotions.
- Don't use too many technical terms, instead, use more common words.
- Avoid the same structure, instead, write more freely.
- Talk naturally and varied, just like a human would.
- Change the sentence structure and word choice to reflect the same meaning.
- The paraphrased text should be readable and make sense.
- Don't make it more complicated, instead focus on making it more unique.
- Moreover, it's also very important that you keep the style. If it's a poem, make sure it still sounds like one after paraphrasing it.
- Talk naturally. Don't use too many difficult terms, instead, use more common words.
- Write in a relaxed and casual manner
- Make your text more random. Change words to more natural ones.
- DO NOT talk in a monotonous manner, instead, sound more relaxed, casual.
- DO NOT use colloquial language! COMPLETELY AVOID "WTF", "FTW, "OMG", "BFF", "LOL", "LMAO", "IDK", "TBH", "JK", "FYI", "IMHO", "IRL" DO NOT USE THEM
- DO NOT use slang at all! Use formal language, but make it sound natural.
- Sound like a high school teacher. Use a formal tone.""",

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
    {
        "role": "assistant",
        "content": """Reaching your full potential and achieving your goals can require a strong foundation of confidence and unwavering motivation. With life's unpredictable twists and turns, we might often find ourselves questioning our abilities and feeling discouraged by setbacks. But fear not! Because by adopting the right mindset, you can fight the feeling of not being able to achieve something. Let's get started!

- 1. Establish Clear Objectives: Firstly, you need to set simple, yet efficient daily goals. Take some time to write them down, e.g. on a notepad. Make sure they are realistic, though. Break them down into smaller milestones and check your progress regularly.
- 2. Focus on Self-Care: Consume healthy foods, get sufficient sleep, get your regular exercise, and take time for activities that make you happy.
- 3. Surround Yourself With Positivity: Meet people who make you feel more confident and happy. Look for coaches and friends who can provide guidance and encouragement when you need it. Additionally, consider joining groups or communities that align with your interests and values.
- 4. Learn Something New: Expand your knowledge and abilities. Join courses or workshops, read books, and look for opportunities to apply what you have learned in real-life situations.
- 5. Embrace Failure: Failure is a completely normal, and you have to see it as an opportunity for your personal growth. See it more as a chance to learn and improve, Remember that even the most successful people have encountered failure numerous times before achieving their goals.
- 6. Confront Negative Self-Talk: Negative self-talk can undermine your confidence and motivation. Challenge pessimistic thoughts and replace them with positive affirmations. Practice acknowledging your strengths and accomplishments. Direct your focus towards the progress you have made, rather than looking back.
- 7. Take Action: Ultimately, taking action is the cornerstone of developing confidence and motivation. Set clear goals, develop a plan, and take small steps towards their achievement. Celebrate each little milestone you reach along the way and do not hesitate to seek assistance when needed.

To sum up, building confidence and maintaining motivation is an ongoing process that requires consistent effort and practice. Believe in yourself! Remember to stay patient and persist in the face of obstacles. With enough dedication and focus, you can develop the confidence and motivation necessary for success.""",
    },
    {
        "role": "user",
        "content": """Title: Exploring the Top Ways to Earn Money Online

Introduction:
In today's digital age, the internet has opened up countless opportunities for individuals to earn money online. Whether you're looking for a side hustle or hoping to transition into a full-time online career, the possibilities are abundant. In this article, we will explore some of the best ways to earn money online and provide insights into how you can make the most of these opportunities.

1. Freelancing:
Freelancing has gained immense popularity as a flexible and lucrative option for earning money online. If you possess skills such as writing, graphic design, programming, or digital marketing, freelancing platforms like Upwork, Fiverr, and Freelancer offer a vast marketplace where you can showcase your talents. By creating a compelling profile, delivering high-quality work, and building a strong reputation, you can attract clients and earn a substantial income.

2. Online Surveys and Microtasks:
While they may not make you rich overnight, online surveys and microtasks can be a simple and accessible way to earn extra money. Websites like Swagbucks, Amazon Mechanical Turk, and Clickworker allow you to complete surveys, watch videos, participate in research studies, or perform small tasks in exchange for cash or gift cards. These platforms can be an excellent option for earning money during your free time.

3. E-commerce and Dropshipping:
The rise of e-commerce has revolutionized the way people do business. With platforms like Shopify and WooCommerce, setting up an online store has never been easier. You can sell products of your own creation, source them from wholesalers, or utilize dropshipping, where you partner with suppliers to fulfill orders. With effective marketing strategies and customer-centric approaches, you can create a successful e-commerce business and generate a steady stream of income.

4. Online Tutoring and Course Creation:
If you possess expertise in a particular subject, consider sharing your knowledge through online tutoring or course creation. Websites like VIPKid and Teachable provide platforms for teaching English, academic subjects, or specialized skills. Additionally, with the increasing demand for online learning, creating and selling your own courses on platforms like Udemy or Coursera can be a profitable venture.

5. Affiliate Marketing:
Affiliate marketing enables you to earn commissions by promoting other people's products or services. By joining affiliate programs such as Amazon Associates, ClickBank, or Commission Junction, you can generate income through referral links or banners on your website, blog, or social media channels. To succeed in affiliate marketing, focus on building an engaged audience and providing valuable content that drives conversions.

Conclusion:
The internet has revolutionized the way we work and opened up numerous avenues for earning money online. Whether you prefer freelancing, participating in online surveys, starting an e-commerce business, teaching others, or engaging in affiliate marketing, there are endless opportunities to explore. Success in the online world requires dedication, perseverance, and a willingness to learn and adapt. By leveraging your skills, interests, and the power of technology, you can embark on a rewarding online journey and achieve financial independence."""
    },
    {
        "role": "assistant",
        "content": """# Best Ways to Earn Money Online

Nowadays, there are countless options for individuals to easily earn money online. It can be quite difficult to determine which ones are actually worth the effort, though. So let's discuss the best ways how you can earn money online!

1. **Freelancing**

    Freelancing has gained a lot of popularity, as it allows people to utilize their knowledge in a certain task. Especially writing, graphic design, programming, or digital marketing are common options for freelancing. Platforms like Fiverr or Upwork work like a digital marketplace for freelancing. By setting up a compelling profile, delivering high-quality work, and building a strong reputation, you can easily attract clients and possibly even earn a substantial income.

2. **Surveys & Micro-tasks**

    If you're just looking for an easy way to earn some spare cash, you might be interested in micro-tasks. Sites like Swagbucks and Clickworker offer many different types of micro-tasks. You will often be asked to complete surveys, studies or other small tasks in order to get paid. Of course, this won't make you an overnight billionaire, but it's still a great way to make a few bucks.

3. **E-commerce & Dropshipping**

    The growth of online shopping in recent years has been a revolution in the way people do business. Thanks to platforms like Shopify and WooCommerce, setting up an online store has never been easier. You can sell your own creations, buy from wholesalers or use drop shipping. Using effective marketing strategies and customer-focused approaches, you can build a successful ecommerce business and generate a steady stream of income.

4. **Online Courses**

    If you possess expertise in a particular subject, consider sharing your knowledge through online tutoring or course creation. Websites like VIPKid and Teachable provide platforms for teaching English, academic subjects, or specialized skills. Additionally, with the increasing demand for online learning, creating and selling your own courses on platforms like Udemy or Coursera can be a profitable venture.

5. **Affiliate Marketing**

    You can also earn money by promoting another person or company. You can earn money by placing referral links or banners on your website, blog, or social media channels through affiliate programs such as Amazon Associates, ClickBank, or Commission Junction. To succeed, focus on building an engaged audience and providing valuable content that drives conversions.

## Conclusion

The Internet has revolutionized the way we work and make money online. But it takes commitment, persistence and the ability to learn and adapt. Use your skills, interests, and technology to start your own rewarding online journey.
"""
    },
]