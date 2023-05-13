# LingoSynth 
LingoSynth is a free tool for rephrasing & facts checking text. It is self-hostable.

## Development Progress
### Languages
- [x] English
- [ ] German
- [ ] ... (feel free to contribute!)

###  Text types
- [x] Blog articles
- [x] Book pages
- [ ] Homework & Essays

This is the current development progress of LingoSynth (higher = better):

| Website                                               | Blogs & Books | Homework & Essays |
| ----------------------------------------------------- | ------------- | --------------------- |
| [zerogpt.com](https://www.zerogpt.com/)               | 60%           | ?                     |
| [gptzero.me](https://gptzero.me/)                     | 50%           | ?                     |
| [writefull.com](https://x.writefull.com/gpt-detector) | ?             | ?                     |
| [gptcheck.net](https://gptcheck.net/en)               | ?             | ?                     |
| [gpt-detector.com](https://www.gpt-detector.com/)     | ?             | ?                     |

## Contributing
Re-writing text is a very time-consuming task. Therefore, we need your help!

You can even support us without having much knowledge of programming.
Adding new prompts to `lingosynth/app/prompts.py` is highly appreciated.
Thank you for your support!

The format works as follows:

```py
    ...
    {
        "role": "user",
        "content": """Input text here.""",
    },
    {
        "role": "assistant",
        "content": """Rephrased text here.""",
    }
    ...
```

Make sure to check if the rephrased text is detected as plagiarism on the websites mentioned above.

## Star History
[![Star History Chart](https://api.star-history.com/svg?repos=Luna-OSS/LingoSynth&type=Date)](https://star-history.com/#Luna-OSS/LingoSynth&Date)
