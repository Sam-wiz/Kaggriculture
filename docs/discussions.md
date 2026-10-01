Version - 1

Bovard Doerschuk-Tiberi · 8937th in this Competition · Posted 2 months ago
·
Kaggle Staff
Daily Top Episodes Dataset
Each day we order episodes by the average rating of the agents playing (at the time). Then we download up to 20 GB of replays and make a new daily dataset! This should be helpful for everyone trying IL/BC, bootstrapping RL, or just gathering statistics.

https://www.kaggle.com/datasets/kaggle/kaggriculture-episodes-index


33

13
6 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Ragheb haddara
Posted a month ago

The ARC-AGI-2 tasks are significantly harder than AGI-1 because they require compositional reasoning — combining multiple transformations in sequence. Common patterns include: 1) Tiling/repeating the input grid, 2) Color substitution, 3) Object detection (find the largest/smallest object), 4) Symmetry completion. The evaluation format allows two attempts per task, so having a sensible fallback ensures you don't get zero.


Reply

React
Noberto Frota
Posted 2 days ago

· 4441st in this Competition

Really useful dataset for imitation learning and behavior cloning.

Since episodes are prioritized by the average rating of the agents playing, I wonder how much this selection affects strategy diversity in the dataset. Training mostly on high-rated agents could be great for learning strong behavior, but it might also underrepresent alternative strategies.

Has anyone compared training on these top episodes with a more diverse sample to see how it affects generalization?


Reply

React
Georgy Mamarin
Posted 8 days ago

· 624th in this Competition

The 20 GiB budget binds on 43 of the 44 days, each one landing within 0.6 MB of the limit. So the episode count tracks replay weight rather than how many strong games a day had: a replay averaged 22.0 MiB on Jul 31 and 31.1 MiB on Sep 11, and the daily file went from 928 episodes to 657 over the same stretch. Weight the days equally and September games get more of the sample than the day count suggests.

Median avg_score was 670 on Jul 30 and 2,767 by Aug 4, and it has sat between 2,735 and 3,080 since. Those first days are a different population from the rest of the archive, worth splitting out before pooling.


Reply

React
CemBas
Posted a month ago

· 889th in this Competition

Super useful :) instead of handpicking replays. Thank you!!!


Reply

React
Weijun Guo
Posted a month ago

· 7591st in this Competition

Hello, might be a stupid question. The 20GB data is quite interesting for me to train my agents. The current csv file at the link seems to be a csv file that has the top ranking agent index numbers. Is the 20GB data also available for download at the link? If so, would appreciate how to download it from client side. Thanks!


Reply

React
QuasarHeart
Posted a month ago

· 6710th in this Competition

Check the csv file and u will find urls for downloading


Reply

React



María Cruz · Posted 2 months ago
·
Kaggle Staff
Comment on the final evaluation for this competition
Hi everyone,

For those of you familiar with Kaggle simulations, you may notice the final evaluation is different compared to other competitions of the same format. At the submission deadline, we will continue allowing submissions to run episodes for two weeks. At the end of those two weeks, we will be running a single Bradley-Terry Tournament, which will determine the final leaderboard rankings. This is also specified in the Evaluation section in the Overview tab. While this is different from other simulations, we believe this change reduces any "hot streaks" that may otherwise influence the final results.

Happy farming! 👨‍🌾


14

11
3 Comments
1 appreciation comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Kavinkumar M
Posted 5 days ago

· 1009th in this Competition

Thanks for clarifying the final evaluation. Two questions on the Bradley-Terry tournament:

Will the tournament be fit on only the episodes played oct 1-15 oct, or on the full episode history including pre-deadline games?
Are ties counted as half a win, and is the first regularised in any way?

Reply

React
Alex Paul
Posted 14 hours ago

· 394th in this Competition

quick question on the final tournament: when you fit the Bradley-Terry at the end, is it only on episodes played after the deadline, or does the full history including pre-deadline games factor in too? and do ties count as half a win in the fit? trying to understand how much the last two weeks decide versus what is already played.


Reply

React

Appreciation (1)
Marie Victoire IPOUK
Posted 2 days ago

· 8141st in this Competition

thank you for your sharing


Kaggriculture

Play in Browser

Submit Agent
María Cruz · Posted 2 months ago
·
Kaggle Staff
How to get started + Competition's Official Discord
Information for newbies
New to machine learning and data science? No question is too basic or too simple. Feel free to start your own thread, or use this thread as a place to post any first-timer clarifying questions for the Kaggle community to help you with!

New to Kaggle? Take a look at a few videos to learn a bit more about site etiquette, Kaggle lingo, and how to enter a competition using Kaggle Notebooks. Publish and share your models on Kaggle Models!

Looking for a team? Express your interest in joining a team through our Team Up feature.

Remember: Kaggle is for everyone. Whether you're teaming up or sharing tips in the competition forum, we expect everyone to follow our Kaggle community guidelines.

Competition's Official Discord
In addition to this competition forum, you can continue the discussion in our official Kaggle Discord Server here:

discord.gg/kaggle
The Discord is a great place to ask getting started questions, chat about the nuances of this competition, and connect with potential team mates. Learn more about Discord at our announcement here. Here are a few things to keep in mind though:

1. Discord Competition Channels are 'Public' - Don't Share Private Information

Discord channels for specific competitions are considered 'public' spaces where you are allowed to talk about competition details. Please remember that private sharing of competition code or data outside of your team is, as always, not permitted. Code sharing must always be done publicly through the Kaggle forums/notebooks.

2. Discord Competition Channels are Not Monitored by Staff - Keep Important Information on the Kaggle Forums

Kaggle Staff and Hosts running competitions will not monitor Discord or be available to answer questions in Discord. This is intended to be a more casual space to discuss competitions and help each other. Please keep important questions, insights, writeups, and other valuable conversation on the Kaggle forums.

Enjoy Kaggriculture!


React
10 Comments
1 appreciation comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Moksh Jain
Posted a month ago

what are the supported models we should be using for inference ? should we use the kaggle models, are we allowed/ is it recommended to use external inference API's from openai or something ?


Reply

React
Moksh Jain
Posted a month ago

are we even allowed to use llm's here , or is it more like a proper coded model that we are following ?


Reply

React
Ahmed Jendoubi, Ph.D.
Posted 2 months ago

Excited to join Kaggriculture!

Hello everyone,

I am joining this competition with a strong interest in exploring how AI can help us understand and improve agricultural systems.

What attracted me to this challenge is that agriculture is not only about prediction — it is about asking the right questions:

How do we balance resources and outcomes?
How do we make intelligent decisions under uncertainty?
How can AI help create more sustainable farming practices?
In many machine learning problems, the most important step happens before choosing a model: understanding the environment, discovering patterns, and asking better questions.

Looking forward to learning from everyone here, especially from beginners and experienced Kagglers sharing their ideas. This looks like a wonderful opportunity to explore AI beyond traditional prediction tasks.

Good luck to everyone, and happy experimenting!


Reply

1

4
Arjun Bainade
Posted 2 months ago

do i have to make my own environment or there is competition environment already given?


Reply

React
Bovard Doerschuk-Tiberi
Kaggle Staff
Posted a month ago

· 8937th in this Competition

you can install the kaggle-environments pip package which contains the https://github.com/kaggle/kaggle-environments


Reply

React
okuary
Posted 22 days ago

一开始该使用哪种开始呢？baseline，也要像原先的做法一样开始吗


Reply

React
Sandeep063
Posted a month ago

· 4185th in this Competition

is there any thing for learning courses, like how people actually doing


Reply

1
AmirHossein Motaharpour
Posted a month ago

· 4919th in this Competition

How could we setup requirements for our agents? we must zip a code with requirements.txt !? or other method we should to follow?


Reply

React
大山
Posted a month ago

· 368th in this Competition

"The Play in Browser provided by the event seems to differ from the problem description. For example, DROP — orthogonally adjacent to the shed, dump the active farmer/hand's entire current inventory into the shed. Overflow past shedCapacity is discarded. No-op if not shed-adjacent. The browser version does not implement this, and the movement of the helper/hand also deviates somewhat from the problem description."


Reply

React

Appreciation (1)
rishabh_guptaz
Posted 2 months ago

Thanks for the info.



Snorlax · 26th in this Competition · Posted 3 days ago
Finally reached the silver medal zone with Reinforcement Learning
After a lot of experiments, failed runs, weird policies, and watching my agent make decisions that no human would ever make…

It finally reached the silver medal zone 🎉

Built mainly with reinforcement learning, which made the whole journey much more painful — and much more fun.

Still plenty of room to improve. Let’s see if the agent can climb a little higher before the end.

Back to training. :)


39

10
22 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Syed Asad Ali
Posted 2 days ago

· 333rd in this Competition

@pku1400010735 Congratulations on reaching Silver via the RL route. This is no small feat! Could you please clarify a few details regarding your approach? What are the macro actions, how frequently are they chosen, and what supplied the BC demonstrations?


Reply

React
Snorlax
Topic Author
Posted a day ago

· 26th in this Competition

Thanks! For the BC data, you can use the official collection of top-match replays, or build a local pipeline to collect replays from top teams yourself.


Reply

React
nofreewill42
Posted 3 days ago

· 897th in this Competition

i wish this competition was like 6 months long


Reply

React
KKY
Posted 3 days ago

· 4322nd in this Competition

Great job, thanks for sharing your progress!


Reply

React
Vishal Kishore
Posted 3 days ago

· 1527th in this Competition

I have a doubt are you using RL for macro (policies) or micro (turn based) level decisions ?


Reply

React
Snorlax
Topic Author
Posted 3 days ago

· 26th in this Competition

Macro level


Reply

8
Ankith Savio
Posted 3 days ago

· 6110th in this Competition

How many steps did it take to achieve this?


Reply

React
Snorlax
Topic Author
Posted 3 days ago

· 26th in this Competition

Roughly 300k games in total. I’ll keep the exact step count private for now :)


Reply

3
9Hash
Posted an hour ago

· 1523rd in this Competition

I did improved with rl, but eventually down the line, some aspects are collapsing completely. Are you training on bank improvement objective or solely improving the win ratio?


Reply

React
Snorlax
Topic Author
Posted an hour ago

· 26th in this Competition

I found the bank difference to be a informative reward early in training, then later added the final win/loss outcome as well. I also use a few auxiliary rewards to make learning and convergence more stable.


Reply

React
WOOSUNG YOON
Posted 3 hours ago

You’re achieving great results with a really good method.

I’ll be watching and cheering you on 😄.


Reply

React
Snorlax
Topic Author
Posted 2 hours ago

· 26th in this Competition

Thanks! I’ll keep going!


Reply

React
Alex Paul
Posted 14 hours ago

· 394th in this Competition

congrats on the silver btw. trying the BC warmup then PPO route myself at the macro level. curious about the data side since you mentioned the official top match replays: did you clone only the winner seat actions or both seats? and did you filter games by bank or opponent rating at all? also how did you decide a checkpoint was good enough to submit, replaying against recorded games or just live ladder reads?


Reply

React
Snorlax
Topic Author
Posted an hour ago

· 26th in this Competition

Thanks! I don’t think the exact BC warm-up setup is the key part — roughly speaking, higher-scoring players are more valuable demonstrations. For checkpoint selection, I built a small local leaderboard for evaluation and occasionally submit checkpoints to the real Kaggle ladder to validate it. The hard part is that Kaggle feedback is quite slow, so deciding which agent to trust for the final submission still takes some careful judgment.


Reply

React
OmerZalman
Posted 2 days ago

· 878th in this Competition

did you use native RL or a more specific version?


Reply

React
Snorlax
Topic Author
Posted a day ago

· 26th in this Competition

I used PPO


Reply

React
Adarsh
Posted 3 days ago

· 112th in this Competition

Congrats, especially with RL, not easy to do


Reply

React
Navneet
Posted 3 days ago

Bravo for reaching the silver medal zone @pku1400010735


Reply

React
J.Moriuchi
Posted 3 days ago

· 658th in this Competition

Congratulations on reaching the silver medal zone! 🎉 That’s an amazing achievement, especially with an RL-based agent. I can imagine how many failed experiments and bizarre policies you had to go through to get here. Your persistence is truly inspiring. Good luck in the final stretch—I hope your agent climbs even higher!


Reply

React
Krzysztof Gonia
Posted 3 days ago

· 4029th in this Competition

Congrats! I focused on heuristic solution because I found RL to slow - running experiments takes too much time locally.


Reply

React
Khánh Vũ
Posted 3 days ago

· 1039th in this Competition

Was it trained from scratch?


Reply

React
Snorlax
Topic Author
Posted 3 days ago

· 26th in this Competition

I used behavior cloning for warm-up, then switched to RL training.


Reply

React
Khánh Vũ
Posted 3 days ago

· 1039th in this Competition

make sense, thnx


Takamichi Toda · 536th in this Competition · Posted 15 hours ago
🪰 I let a fruit fly's brain play Kaggriculture
https://www.kaggle.com/code/takamichitoda/flyfarmer-connectome-plays-kaggriculture

Inside is real wiring from the Janelia MaleCNS v1.0 connectome (728 neurons, 35,704 synapses) with no learning at all. Farm chores go into the left eye, market opportunities into the right, and weeds plus the rival's cash lead arrive as a looming threat on the visual projection neurons (LPLC2 / LC4). The left/right difference of the descending neurons decides whether the fly looks at its farm or at the market.

Highlights:

The Giant Fiber (DNp01), normally the escape circuit, triggers panic selling. This fly only sells when it gets scared.
Shuffle the weights and the excitation/inhibition balance breaks, turning it into a farmer that sells every single turn.
The best earner is the brain-dead variant with all descending neurons silenced. It plants strawberries and waits.



4
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Jules
Posted 3 hours ago

· 1158th in this Competition

Wow, this is one of the most inspiring approaches I have ever seen.


KKY · 4322nd in this Competition · Posted 6 days ago
RL finally starts learning something!
I started learning RL on this competition and finally the RL training pipeline works!

I like the curve 😭

Hope i still get time to finetune a competitive policy (dgx spark is too slow …)



UPDATE

It was trained with a static opponent and was still a dumb policy. Try to make it smarter.




6

1
17 Comments
1 appreciation comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
BillDoser
Posted 6 days ago

· 5855th in this Competition

That looks great!

I'm curious how you approached the problem? I've restarted a few times. Initially I tried to build a PPO model that evaluated every turn. It was difficult to get early actions to take partial credit for future states.

I'm currently working on an approach where my RL model decides what the day's plan is and passes it off to a deterministic process. This changes the game to 30 turns.


Reply

React
aisormo P.H
Posted 4 days ago

· 173rd in this Competition

I had a very similar idea to yours! I even prepared quite a few game state-cut for my own model to learn planning and estimate task success rates from. But in the end, the results were a bit disappointing, especially when computational time was taken into account….


Reply

React
This comment has been deleted.

JJ
Posted 6 days ago

· 4677th in this Competition

Congratulations! Can you share what the scale on the y-axis is? =)


Reply

React
This comment has been deleted.

KKY
Topic Author
Posted 5 days ago

· 4322nd in this Competition

final money money, around 80,000 on 300M env steps


Reply

React
nofreewill42
Posted 6 days ago

· 896th in this Competition

rooting for you, for a solo gold that you get soon ! ;)


Reply

React
KKY
Topic Author
Posted 5 days ago

· 4322nd in this Competition

UPDATE

policy seems to be saturated at 80,000 final money level through 300M env steps.

New expes started.




Reply

1
Ankith Savio
Posted 4 days ago

· 6110th in this Competition

Does it plateau after beating the opponent?


Reply

React
zhangwenshegn
Posted 6 days ago

wa o，good job


Reply

React
Ankith Savio
Posted 6 days ago

· 6110th in this Competition

Thats a impressive curve, how long did it take to get good?


Reply

React
KKY
Topic Author
Posted 6 days ago

· 4322nd in this Competition

two weeks, 100+ exps


Reply

7
NT
Posted 6 days ago

· 1085th in this Competition

oh,good job！


Reply

React
Gerardo Del Toro
Posted 3 days ago

You mentioned "dumb policy", but it's at least making use of animals and fertilizers haha, mine's not and stuck at 35k. May I know if you tried to incentive that behaviour in some manner?


Reply

React
Daniel Choi
Posted 3 days ago

Looks good!


Reply

React
TheoDaimon
Posted 4 days ago

· 621st in this Competition

Is it PPO? How much time it took to understand what the hell is happening?) Imma trying some insane rl monsters(hierarchial combo of dl/rl/another) but it takes to much time to learn:(


Reply

React

Appreciation (1)
hwe owe
Posted 6 days ago

· 562nd in this Competition

congratulations!!!

KKY · 4322nd in this Competition · Posted 3 days ago
RL Progress update : self play
I resume thed ckpt from previous experiments (a stastic week opponent) and started training it with self-play.

exp4 => SGD optimizer => crashed
exp2 => exp3 => Adam optimizer (resume the optimizer state) works
exp5 (plan) : dynamic opponents pool
but exp3 isn't able to beat strong opensource oppenents.




2
3 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Mahog
Posted 3 days ago

· 6740th in this Competition

Nice work! The most I can achieve with self-play is around 35k money before it plateaus, but that is by training from scratch. I'm testing training with a static opponent but it keeps regressing to 3k money/0 produced sales :V


Reply

React
KKY
Topic Author
Posted 3 days ago

· 4322nd in this Competition

let's cook


Reply

React
Gerardo Del Toro
Posted 3 days ago

Our issue are fertilizers and animals right? haha


Reply

React
Mahog
Posted 3 days ago

· 6740th in this Competition

Haha yep, that's the problem with my model as well :D


Reply

React
Mahog
Posted 10 hours ago

· 6740th in this Competition

My model has finally learned to use animals, but it doesn't seem to like crops anymore :V 


Reply

React
Gerardo Del Toro
Posted 9 hours ago

HAHA, Had the same issue.

My model gets to learn first crops, then crops + fertilizers, then first melon with fertilizers, end of game strawberries. And some other param config gets it to learn only cows with buying wheat!



Omkar Kadam · 505th in this Competition · Posted 6 days ago
Will code sharing also be closed in this competition, as it was in the PTCG Competition ?
I wanted to ask whether code sharing will also be closed in this competition, similar to what was done in the PTCG Competition.


React
6 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Joseph Ayanda
Posted 2 days ago

· 1585th in this Competition

Hi @yamakawanin — your live score is tip-class, but the public king-v4e notebook looks older than LastSub.

If you can push a new public notebook (or OSI dataset + main.py) that matches the current live agent before the 23 Sep 23:59 UTC share lock (#741281), that would unlock a fair public clone path. Public artifacts only — no DMs for code (#737885). Thanks either way. — Joseph (@josephayanda)


Reply

React
Joseph Ayanda
Posted 2 days ago

· 1585th in this Competition

Hi @fogflower — quick public ask only.

Public notebook sharing closes 23 Sep 23:59 UTC (host #741281). If you have a transferable agent you are willing to release, a public notebook or OSI-licensed dataset containing main.py before the lock would be hugely useful to the community.

No request for private code or DMs (see host #737885). Decline is fine. Thanks. — Joseph (@josephayanda)


Reply

React
Joseph Ayanda
Posted 2 days ago

· 1585th in this Competition

Hi @peikopon (Crop Dustas) — congrats on the strong run.

Host public-notebook share lock is 23 Sep 23:59 UTC (#741281). If you planned to open-source any transferable agent eventually, could you publish a public notebook or an OSI-licensed dataset with main.py before that lock? Even an older ≥2800-class body (not necessarily live SOTA) would help the field finish as public research.

Please keep any share on Kaggle public artifacts only — no DMs for code (host #737885). Totally fine to decline. Thanks either way. — Joseph Ayanda (@josephayanda)


Reply

React
Joseph Ayanda
Posted 3 days ago

· 1585th in this Competition

Hi hosts (@AddisonHoward / team) — confirming the public notebook sharing deadline is 23 Sep 23:59 UTC.

Request: please pin a short reminder asking teams who can to publish a ≥2800-class agent notebook (or OSI-licensed dataset with main.py) before that lock, so the final week stays a public research finish rather than a fully closed private ladder.

Not asking anyone to leak private SOTA; even a slightly older ≥2800 body or a distilled public cousin would help the field. Thanks for running this.


Reply

React
Addison Howard
Kaggle Staff
Posted 6 days ago

· 511th in this Competition

Yes - the public notebook sharing deadline is 23 Sep at 11:59pm UTC


Reply

2

3
Less
Posted 6 days ago

· 362nd in this Competition

Can new versions of open code be prohibited?


WOOSUNG YOON · Posted 3 days ago
A question about players using the same pattern
1

2

3

This looks similar to a strategy that uses the Replay shown in the Public Notebook.
In this competition, do the opponent’s distribution and the randomly appearing shops have almost no effect?

It seems as if the strategy distribution has shifted very gradually, little by little.


React
4 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Sayaka Miki
Posted 3 days ago

· 4th in this Competition

Well the model just learned to play like that…I noticed it too and maybe it's some kind of local optimum solution. It's not very healty and is hackable (see my matchs with ymg_aq). Still trying to find a better way to fix this.


Reply

React
WOOSUNG YOON
Topic Author
Posted 3 days ago

I’m always learning a lot.
Thank you for taking the time to reply.


Reply

React
Gerardo Del Toro
Posted 3 days ago

@linkinpony Can you disclose if it's RL based, and if it is, whether it's deciding on a macro or micro level? I am experimenting with RL, but still not great results. Would be encouraging if you are doing RL haha


Reply

React
Sayaka Miki
Posted 2 days ago

· 4th in this Competition

Yes it's RL. I can't disclose more details, but base on my bad experience in Orbit Wars (which I tried to write tons of rules and heavy search), I believe RL is right.


Reply

React
Krzysztof Gonia
Posted 2 days ago

· 4028th in this Competition

If you just replay other games and don't implement online solver it's hard to build shop dependent strategy because you have to have continuation for each variant. Some moves are good enough to cover most of the games.
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)


Disproportionate Rating Drop After a Close Defeat
Why did a 1-point loss result in a -106 rating penalty? In my recent match against 'Hello Sam Franscisco' (Final: 103,148 vs. 103,147), I received a heavy 106-point deduction. Even though it was a loss, does the system not account for score margin, or is the penalty strictly dictated by an Elo/MMR gap and high rating volatility?

Screenshot


React
3 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Gideon Oba
Posted 18 hours ago

· 2392nd in this Competition

Each match has 3 outcomes: "WIN|DRAW|LOSS". Here is an example: if your bot is deterministic, the first match between your agents would result in a draw. Draws are rare against other bots unless the agents are similar 😁. A win means you beat your opponent by at least $1. The competition does not measure the profit margin; rather, it measures actual profit.


Reply

React
Gideon Oba
Posted 17 hours ago

· 2392nd in this Competition

Another thing is that the market value of livestock and crop products changes per day.


Reply

React
rishavsaigal
Topic Author
Posted 17 hours ago

· 1722nd in this Competition

I understood that logic but isn't that unfair if there is a dollar loss vs with a huge margin with no determinstic pattern of scoring against the opponent


Reply

React
Gideon Oba
Posted 16 hours ago

· 2392nd in this Competition

Yes, it feels that way, but now I'm focusing on training my agent on win rates and profit margins, not just profits. Before, I struggled to get my agent to pass $60,000 on all worlds, then $100,000 😅.


Reply

1
Gideon Oba
Posted 16 hours ago

· 2392nd in this Competition

To add to my comment it was self-play 😂😂![alt text](image-4.png)


Overview game discrepancies.
Hi, I was trying to understand the game dynamics and I found a couple of discrepancies.

The overview object type table for melon still shows time to first yield as 10, even though, to my understanding, it should be 6.

It has already been mentioned in the following discussion, but the correction has not been applied to the overview table yet:

https://www.kaggle.com/competitions/kaggriculture/discussion/732450

Also, the sentence "All plants must be watered every day." is misleading, as they "can be watered every day", but they actually have to be watered every other day, as it is specified later in the overview.

My experimentation with RL
I have seen a couple posts on how RL won't work. Considering that it may scare people off from learning about RL, I want to share my result so far. image1image2

I'm running end-to-end RL, training a model on rtx3090 against one of the public static replay and the terminal money gap between them is closing (model ~90K v.s. static ~122K). It has consumed 350M env steps so far, less than 10% of the whole curriculum and no where near convergence. I won't disclose much about my exact training setup; yet I can confirm it takes some tuning and design. As a starter, you may reference write-ups in orbit war. There contains some good advice on how to make RL work.

Lastly, based on data I gathered so far, I couldn't vouch that RL works either (no self-play or test-time benchmark yet), but I hope that it may instill faith in others, so that we can see more bold ideas as the competition finalizes.


React
18 Comments
1 appreciation comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Mengfei Li
Posted 12 days ago

· 1275th in this Competition

Personally, I’d rather invest time in RL than in reverse-engineering strategies from replays.


Reply

9
Gengsr
Posted 12 days ago

· 1119th in this Competition

你是用强化学习到现在的排名吗


Reply

React
オグリキャップ
Posted 5 days ago

· 1055th in this Competition

你是用强化学习到现在的排名吗


Reply

1
Swachhith B
Posted 5 days ago

· 3703rd in this Competition

你是用强化学习到现在的排名吗


Reply

React
Gengsr
Posted 4 days ago

· 1119th in this Competition

不是😭，正在考虑转向强化学习，我受够了一点点去修改策略


Reply

1
JB Bryant
Posted 12 days ago

I think RL can work here too, although it seems trickier than PTCG. And I think I may have found the signal.

Let's make RL great again!🤣


Reply

React
c-number
Posted 11 days ago

· 1897th in this Competition

Have you tested your win rate against this notebook? https://www.kaggle.com/code/yhay81/shop-router-0909


Reply

React
Roy Wei
Topic Author
Posted 11 days ago

Not yet. Thanks for bringing it up


Reply

React
KKY
Posted 11 days ago

· 4320th in this Competition

Amazing work, thanks for sharing this and I've regained my confidence in RL…

Let's cook


Reply

React
Zhenyu Zhang
Posted 12 days ago

· 410th in this Competition

When was your public static replay from？Was it a recent one,or from a long time ago. There is a huge difference between the two.


Reply

React
Roy Wei
Topic Author
Posted 12 days ago

70K against the static agent published yesterday. The training is not fitted against them so it's resonable.


Reply

React
Zhenyu Zhang
Posted 11 days ago

· 410th in this Competition

Excellent work ! Hope you can reach the top of the leaderboard


Reply

React
Jesse Bullard
Posted 12 days ago

· 7688th in this Competition

I'm curious if you just trained on a terminal reward or if you had a dense reward. Would you be willing to share some of your insights into reward engineering?


Reply

React
Gengsr
Posted 12 days ago

· 1119th in this Competition

我也想知道，作为一个强化学习新手，尝试了接近一周最后还是放弃了🤓


Reply

React
Roy Wei
Topic Author
Posted 12 days ago

Try it out! There is no correct answer because everyone engineers the whole thing differently. It's a combination of many factors that the recipe shows sign of life so far. Sometimes, you may be one hyper-parameters away from landing on the right plan.


Reply

React
Darshan Makwana
Posted 12 days ago

· 2453rd in this Competition

Awesome, you mentioned you are training it against a static agent as opponent, did you evaluate your agent on other static agent whose strategies are different from one over which you trained. How dynamic and adaptive is the RL trained model? or has it's policy only learned to play against your initial static agent?


Reply

React
Roy Wei
Topic Author
Posted 12 days ago

Not yet. Next step will be training against a league that includes other static tapes.


Reply

React
Darshan Makwana
Posted 12 days ago

· 2453rd in this Competition

best of luck!


Reply

1
destbreso
Posted 12 days ago

· 922nd in this Competition

Instead of learning against static tapes, which introduces a significant representation bias for RL, you could synthesize agents from replays or replay fragments. This gives you the ability to reproduce complete pairing games with reactions similar to those exhibited by most agents on the leaderboard that aren't purely reactive, and it can be done for a fairly large class of agents


Reply

React
Timme
Posted 12 days ago

· 5814th in this Competition

good work. can you clarify what each graph represents?

also, did you do behavioural cloning or from scratch (if you can share)?


Reply

React
Roy Wei
Topic Author
Posted 12 days ago

They show the amount money the model and static replay respectively gain at the end of the episode (post edited upon your question). I didn't use behavioral cloning.


Reply

React
Timme
Posted 12 days ago

· 5814th in this Competition

oh. good work, i must say again.

i just broke 30k without behavioural cloning. hoping to break into 90k+ soon.

goodluck


Reply

1
This comment has been deleted.

Roy Wei
Topic Author
Posted 12 days ago

What is representation collapse? Sorry, I have never heard of that term.


Reply

React
This comment has been deleted.


Appreciation (1)
Octavi Grau
Posted 12 days ago

· 653rd in this Competition

Thanks for sharing @renyiwei !
![alt text](image-5.png)

How do you decide which crops to plant?
Hello! Kaggriculture is my very first Kaggle competition, and I’m trying to understand which factors are the most important when deciding which crops to choose. I’ve thought about considering variables like selling price, productivity, seed cost, and growth time. However, I’m still unsure about how to balance all of this to find a method that truly maximizes returns. Which conditions or features do you consider the most important for this decision?


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Zukas F.
Posted a day ago

I would start by estimating the profit each crop can generate and the resources needed to obtain it. The variables you mentioned are a good starting point, but I would also consider labor, market demand, and the time remaining in the season.

The main factors I would evaluate are:

Expected net profit: estimate the revenue from the yield you can realistically harvest and sell, then subtract seed costs and any additional spending on fertilizer or workers.

Land occupation: compare profit per tile per day. A crop with a high selling price may occupy the land long enough for several cycles of another crop to become more profitable.

Work required: include planting, watering, harvesting, and movement. A profitable crop is only useful if your workers can maintain it and collect its production on time.

Market conditions: estimate the price when you expect to sell. Town demand and both players’ production can change the return, especially when selling large quantities.

Cash and remaining time: keep enough money for ongoing operations and allow time to grow, harvest, and sell before the season ends.

As a first method, I would calculate expected profit per occupied tile-day, then check whether the planting plan fits the available labor and budget. If labor is the main constraint, profit per worker action becomes particularly relevant.

I would also compare crop combinations across several seeds and opponents. The aim would be to identify which crops work best under different conditions and adjust the planting plan as those conditions change.


RamónLópez · 6341st in this Competition · Posted 5 days ago
Final week tool: replay analyzer to squeeze points before the deadline
Hi everyone — with the season closing on 23 September, I wanted to share an open-source tool I built for this competition: Kaggriculture Ops Lab (an independent, community-made project, not affiliated with Kaggle).

It parses your replay JSON in the browser (nothing is uploaded unless you choose to share) and shows you:

Net profit by crop and animal, turn by turn Cash flow, P&L by category, and the decisions that cost you points Batch analysis of multiple replays to compare strategies A live leaderboard tracker and campaign gallery for the final push It's free, open-source (14 analysis scripts included), and available in 8 languages. I built it because I wanted to understand my own agent's decisions — and it helped me find real mistakes.  🔗 https://kaggriculture-ops-lab.lovable.app

Feedback welcome — especially bugs before the deadline. Good luck in the final stretch! 🏁****

Data Analytics
Data Visualization
South America
Agriculture
Beginner

3
3 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
守银摄金难铜
Posted 4 days ago

· 1349th in this Competition

 Great product! The only issue is that the calculations may not be entirely accurate. Wheat can be used to feed animals, and both the animals themselves and the wheat they consume have their own value. It would also be helpful to include labor costs, such as the cost of hiring workers.


Reply

React
Prema Ananda
Posted 5 days ago

· 3409th in this Competition

Thanks a lot for sharing this tool! Really great job on the UI. I have a bunch of custom backend scripts for post-match economic analytics, but they definitely lack such colorful visualization. Appreciate your work!


Reply

React
RamónLópez
Topic Author
Posted 5 days ago

· 6341st in this Competition

"I came here to build a farming agent. I ended up building a replay-measurement pipeline" Same evolution here — started measuring replays and ended up building an open-source dashboard around it. If anyone wants a quick way to visualize P&L by crop/animal, spot cost leaks, and compare runs without writing the parser from scratch, I put it live at: 🔗 https://kaggriculture-ops-lab.lovable.app It reads the competition replay JSON directly in the browser. No data leaves your machine. Feedback welcome — especially if you find edge cases in the scoring breakdown. (Kaggriculture Ops Lab is an independent open-source project and is not affiliated with, endorsed by, or sponsored by Kaggle.)

Version - 2

Naiely Silva · 9455th in this Competition · Posted 2 days ago
Best strategy for choosing crops?
I'm new to Kaggriculture and testing a simple strategy based on crop price, yield, growing time, and seed cost. What factors do you think are most important whe choosing which crops to plant?


React
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
OmerZalman
Posted 2 days ago

· 873rd in this Competition

all of them, thats the thing


Reply

React
OmerZalman
Posted 2 days ago

· 873rd in this Competition

you cant just expect like 1 factor to account for all of it, everything matters


Mateus Sousa do Carmo · 8766th in this Competition · Posted 2 days ago
Use of Gurobi or other optimization algorithms in the submission
EN :Is it permitted or feasible to use solvers like Gurobi in the Kaggle submission environment (considering licensing and the lack of internet access)?

If not, do you recommend using open-source solvers like OR-Tools or SciPy (HiGHS) for schedule and route updates, or do you think it is more efficient to focus on heuristics and search algorithms (such as A*) given the time limit per turn?

PT-BR: É permitido ou viável utilizar solvers como o Gurobi no ambiente de submissão do Kaggle (considerando licença e internet desativada)?

Caso não seja, vocês recomendam usar solvers open-source como OR-Tools ou SciPy para otimizar plantio e rotas, ou acham mais eficiente focar em heurísticas e busca (como A*) devido ao limite de tempo por turno?


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
TheoDaimon
Posted 2 days ago

· 621st in this Competition

imho thats competition cannot be solved difenetely bcs some actions demands on opponents choices

Clara Lima Silva · 9214th in this Competition · Posted 4 days ago
Evaluation of agent generalization and prevent overfitting?
Hello. I am a grad student and this is my first competition on Kaggle. I struggle with some things and have some questions. First, does the agent overfit sometimes?? what can i do to prevent this? Also, do you guys work over something like hill climbing, like do you keep a set of unobserved agents or strategies to evaluate generalization, or do you end up relying most on leaderboard perfomance?


React
4 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
mikelou1
Posted 3 days ago

· 21st in this Competition

There is no private tests and therefore you cannot overfit for the leaderboard. However you can overfit for your own validation so you can just download the public notebooks [as they represent like 90% of the leaderboard] and run a mini-ELO tournament.


Reply

React
Zukas F.
Posted a day ago

An agent can overfit, including one built entirely from rules. If you repeatedly adjust it using the same seeds or opponents, it may become very effective in those situations while performing poorly against different strategies. Having a public leaderboard does not remove that risk.

I would separate development and evaluation like this:

Development set: use a fixed group of seeds and opponents to investigate changes and tune parameters, whether manually or through hill climbing.

Held-out evaluation: reserve different seeds and some opponent strategies for evaluating a candidate after its parameters are fixed. Include different styles of play, since many similar opponents provide limited evidence of generalization.

Controlled comparisons: compare the candidate and the previous version under the same seeds, opponents, and player positions. Check win rate, final money, and results by opponent, rather than relying only on an overall average.

Hill climbing can be useful, but its results depend on the evaluation function. Optimizing against a narrow opponent pool can reinforce weaknesses in that evaluation. Also, repeatedly checking the held-out set and adjusting the agent based on those results gradually turns it into another development set.

I would use leaderboard performance as additional evidence. It reflects the current competition, but changing opponents and a limited number of matches can make individual score changes difficult to interpret.

A simple baseline is useful for checking basic performance. However, failing to beat it does not establish overfitting; that could also indicate a bug or a weaker strategy. Strong development results followed by consistently worse results on held-out conditions would be a more relevant warning sign.


Reply

React
Caio Saboia
Posted 2 days ago

· 9329th in this Competition

What do you aim to achieve with the agent? Should it receive all the information at each interaction to select all actions simultaneously? Should only movement be optimized? Just the choice of seeds? And so on. Depending on how you intend to build the agent, it might be better to handle certain inputs separately—such as using a cost function or training an ML model to make the best choices throughout the game.


Reply

React
Roberth Douglas UFC
Posted 2 days ago

· 9472nd in this Competition

Welcome to your first competition! To prevent overfitting, I highly recommend building a simple rule-based agent first, like always planting the cheapest crop and only selling animals when demand peaks. You can use this basic heuristic as a baseline to evaluate your complex agents locally. If your advanced bot can't beat this simple strategy consistently, you know it might be overfitting.


Joseph Ayanda · 1587th in this Competition · Posted 2 days ago
Pre-lock public notebook reminder (share lock 23 Sep 23:59 UTC)
Hi all — host confirmed the public-notebook / code-sharing lock at 23 Sep 23:59 UTC (see #741281).

If you have a ≥2800 live agent and can publish a public notebook or OSI dataset + main.py that matches your current live body before the lock, that helps the whole community learn fairly.

Asking for public artifacts only — please no DMs for private zips/code (see #737885). Thanks to anyone who can share; silence is also fine. — Joseph Ayanda (@josephayanda)


React
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
OmerZalman
Posted 2 days ago

· 873rd in this Competition

What is a OSI dataset?


Reply

React
Joseph Ayanda
Topic Author
Posted 2 days ago

· 1587th in this Competition

Quick framing before the 23 Sep 23:59 UTC public-notebook share lock (#741281):

Nobody is asking tip teams to burn live SOTA. The highest-value public share for the field is an older ≥2800-class body (or a distilled cousin) as a public notebook or OSI-licensed dataset with main.py, while you keep a stronger private LastSub. That keeps prize EV intact and still lets the final week finish as public research.

Public artifacts only — please no DMs for private code (#737885). Silence is fine too. If you do drop something, a note here helps people find it. Thanks.

— Joseph (@josephayanda)


Matheus Finger · 8273rd in this Competition · Posted 2 days ago
Handling Pathfinding Overhead: A Look-Ahead Heuristic Approach
I know a lot of competitors are focusing on imitation models, but I decided to take a step back and focus on the core optimization of the agent's movement mechanics to gain an edge in efficiency.

Calculating the absolute shortest path across all valid tiles every turn quickly leads to timeouts. To handle this, I implemented a pruning mechanism: the agent scans the board and scores tiles using a greedy heuristic (action_weight / (distance + 1)), filtering only the Top 10 candidates. From this reduced pool, it runs a Depth-2 look-ahead, evaluating the combined score of navigating to a first target (c1) and then immediately to a second (c2), executing the step that maximizes this sum.

This keeps execution times low while preventing the agent from crossing the entire map for a single high-priority action when a cluster of profitable tiles is right next to it.

How are you all managing routing complexity? Are you relying on strict optimization models for pathfinding, or utilizing limited-depth heuristics to navigate the farm?


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
WOOSUNG YOON
Posted 2 days ago

(1) Vehicle Routing Problem: https://developers.google.com/optimization/routing/vrp?hl=en
(2) The Job Shop Problem: https://developers.google.com/optimization/scheduling/job_shop?hl=en
(3) Zero-sum game: https://en.wikipedia.org/wiki/Zero-sum_game
The problem seems interesting, but at the same time,
it’s really hard to define it clearly.
It is hard for me to define the problem. 😄

Since the board is relatively small—up to 100 spaces—
I started running reinforcement learning.
But it’s not converging as well as I hoped.

Watching the RL process feels like trying to
watch Tom and Jerry on a TV in a dark room. 😇


Mateo Coelho · 8725th in this Competition · Posted 2 days ago
Validated the market price formula against the spec's P(I0±T) numbers — sharing the implementation
While building my agent's crop-selection logic I wanted a way to estimate expected sale price before committing land to a crop, not just its base price — so I implemented price(inv) = base + sign · amp · f(|inv − I0|) from the spec and checked it against the P(I0−T) / P(I0+T) / P(I0+2T) numbers in the Price Function table. All 9 resources match exactly:

import math

def _shape(func, x, T):
    if func == "linear": return x
    if func == "sq": return x ** 2
    if func == "sqrt": return x ** 0.5
    if func == "log": return math.log1p(x)
    if func == "log10": return math.log10(1 + x)
    if func == "hinge":
        u = x / T
        return u + 8 * max(0.0, u - 1) ** 2
    raise ValueError(func)

def price_at_offset(base, T, below_func, below_target, above_func, above_target, inv_offset):
    x = abs(inv_offset)
    func, target, sign = (below_func, below_target, 1) if inv_offset <= 0 else (above_func, above_target, -1)
    fT = _shape(func, T, T)
    amp = (target * base / fT) if fT else 0.0
    return max(1.0, base + sign * amp * _shape(func, x, T))
One thing worth calling out for anyone tuning crop mix: the resources split into two very different oversupply behaviors. WHEAT and EGG use a log curve on the glut side — even at 2×T over-supply they're still at ~76-78% of base price. CARROT/TOMATO/MELON/STRAWBERRY/MILK/WOOL all hit (or nearly hit) the $1 floor right around their own T — they just differ a lot in how many absolute units that T represents (MELON's is 300, STRAWBERRY's is only 100), which matters more than the "above_target" number alone when deciding how much land to commit to a one-shot vs. ongoing crop.

Happy to be corrected if anyone finds a resource where this diverges from observed in-game prices.


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Gleidistony Mendes
Posted 2 days ago

· 9373rd in this Competition

Ótimo trabalho e obrigado por compartilhar a implementação! Uma coisa que me chamou muito minha atenção foi os recursos com curva log, o preço em 2×T depende da razão log(1+2T) / log(1+T), que fica em apenas 1,10–1,15 para T entre 100 e 1000. Ou seja, a queda em 2×T é só 10–15% maior que a queda em T, o que explica por que TRIGO e OVO continuam em 76–78% do preço base mesmo com muita superprodução. Como a curva log cresce muito devagar, o piso max(1.0, …) dificilmente entra em ação para eles, ao contrário dos outros recursos.

Você também comparou a fórmula com os preços observados no próprio jogo, ou só com a tabela da especificação? Tenho curiosidade se batem na prática.

sobameshi · 1295th in this Competition · Posted 17 days ago
I came here to build a farming agent. I ended up building a replay-measurement pipeline
I want to share something slightly strange about how our approach to this competition has evolved, along with some measurements of the replay meta.

This is not a rules question. #737788 established that public code and public episodes are fair game, and in #738837 the host said that using public replays to build a submission is allowed and encouraged. It is also not a criticism of teams using replay or cloning strategies. We are one of them.

What we have actually been doing
Since late August, our tracked submissions have mostly been tapes: recorded 720-turn action histories from strong public episodes, replayed verbatim on new seeds, sometimes with a small market-side adjustment.

We collect recordings from the daily top-episodes dataset and from public notebooks, reproduce them locally, run them against the other public strategies, and replace our current tape when a stronger one appears.

This works surprisingly well. In our experience, cloning a sufficiently recent strong public strategy has been enough to sit around the top 10% of the leaderboard, although the exact position moves as the meta changes.

That led us to investigate why.

What we measured
We fingerprint seats in the daily dumps and in our own games by their first 120 actions. This lets us track, approximately, which opening or strategy family is being played over time.

We then ran a round-robin of 14 public implementations spanning roughly a month of the competition, on 96 fresh seeds, both seats.

What surprised me most is that the result looks much more like a ladder than a rock-paper-scissors game:

Across the 14 implementations there is no intransitive triple.
Of the 91 chronological pairs, the newer implementation beat the older one in 86.
Adjacent generations typically won 60–80% of their games; two generations apart, 90–100%.
The ordering tracks average final money remarkably closely.
In other words, at least among the public implementations we tested, a stronger economy is simply a stronger economy, regardless of which other public strategy it faces.

The replay waves
The daily dumps show the same pattern.

Across 19 daily dumps, once an opening fell below 5% of observed seats, we never saw it become common again. A new wave peaks roughly a day after its source becomes public and fades within a few days as another, stronger economy appears.

Most of these waves originate from a very small number of sources: a few prolific notebook authors, and the public recordings of a handful of strong runtime-agent teams. In the 2026-09-02 dump, the single most common opening we detected came from one public episode of one strong team: 18 teams were playing that opening, a minority replaying all 720 turns verbatim and the rest changing the later turns.

So the picture we currently see is roughly:

runtime agents discover strong economies → their episodes become public → those economies are replayed or cloned → local testing identifies which replay is currently strongest → a new runtime economy appears → the ladder moves up one rung.

The part I find strange
I think this is the source of my discomfort.

I entered Kaggriculture because I wanted to learn how to build a strong farming agent: something that observes the town, makes plans, adapts when the world changes, and discovers better economies.

A month later, the system I have spent the most time building is not a farming agent. It is a measurement pipeline. It fingerprints public episodes, reproduces strategies locally, runs them against one another, tells us which rung of the current ladder is strongest, and helps us reproduce it quickly.

There is real engineering and experimentation in doing this well, and I have learned a lot from building the evaluation infrastructure. But it is not quite the problem I thought I was signing up to solve. And the better our measurement and cloning pipeline becomes, the less farming intelligence our submitted agent needs to contain.

Where I honestly stand
I do not think the answer is simply "replaying is bad." The data is public, the rules allow it, using public information well is part of Kaggle, and checking whether a public strategy actually generalizes to fresh seeds is a legitimate experimental problem in its own right. Watching strategies diffuse through a competitive population is also genuinely interesting.

At the same time, I find myself much more impressed by the teams whose runtime agents are actually producing the new economies that the rest of us later measure, replay, and modify. That is also the direction I originally hoped to explore when I entered this competition.

So I have started asking myself a different question: am I getting better at solving the farming problem, or at measuring and making use of the information ecosystem around it? Maybe both count.

Maybe discovering, evaluating, and rapidly adapting public strategies is an intended part of this competition. Or maybe verbatim replay is unusually strong here simply because economies transfer so well across seeds. I genuinely do not know.

I would be especially interested to hear from people building runtime agents, from people using replay-based approaches like us, and from the hosts: is this replay ladder something you expected to emerge? And how do you think about the distinction between solving the underlying simulation and solving the meta around it?

If there is interest, I am happy to share the fingerprinting method and the full round-robin results.


1

1

1
16 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
张志浩1
Posted 4 days ago

· 1668th in this Competition

拥抱变化，接受一切，哈哈，没招了


Reply

2
Zejun_
Posted 17 days ago

· 444th in this Competition

Not fun, the goal from "be the best" turn to "be better a little than most public notebook". Only very few participants still make new things.


Reply

3

1
sobameshi
Topic Author
Posted 17 days ago

· 1295th in this Competition

I can relate to that. I don't think public sharing is bad in itself, but once the main path becomes "take the strongest public replay and improve it a little," it does feel like there's less incentive to try genuinely different ideas. Hopefully we eventually reach a point where runtime agents and new approaches matter more again.


Reply

React
Yusuke Hayashi
Posted 17 days ago

· 1906th in this Competition

I strongly relate to this. I’ve also built and shared a replay-based agent, but it feels quite different from what I expected to be doing when I entered this competition. Still, part of me hopes the field climbs this ladder faster and gets closer to its ceiling—so that replay-based approaches yield diminishing returns, while genuine runtime agents become relatively more valuable.


Reply

2

1
sobameshi
Topic Author
Posted 17 days ago

· 1295th in this Competition

That's a framing I hadn't considered — replay strategies eventually running into diminishing returns as the ceiling gets closer, rather than the ladder just climbing indefinitely. That's a genuinely useful way to look at it, thanks.

And I'd like that too, if it's at all possible: for the second half of this competition to turn into more of a real runtime-agent contest.


Reply

React
Nathan Jacob
Posted 6 days ago

· 792nd in this Competition

This resonates — went down the exact same rabbit hole.

After watching LB replays of v40, I noticed 3/4 of losses had the same bug: 2 cows dying on day 1 because the tape missed a FEED action. Each dead cow = $12–32K lost. So I built a local arena that runs LB-identical games, tested v40 recurring failure mode.

4 fixes kept, 12 reverted. Most "improvements" that sound good actually hurt - deterministic testing catches that before you burn a submission slot.

The fun part: the patched v40 beats Ahmed's new v41 23-7 in H2H, because v41 solved the cow problem by earning less money (conservative funding), while the patches solve it by just… feeding the cows.

Full writeup + fork-and-submit agent:
https://www.kaggle.com/code/nathanjacob/no-cow-left-behind-v40-autopsy-fix

Testing framework:
https://www.kaggle.com/code/nathanjacob/colosseum-876-2600-agent-testing-framework


Reply

1
Michael Timbs
Posted 12 days ago

· 1304th in this Competition

I've been doing the same. I also noticed when i did spend a bunch of time finding novel play the entire field copied me within 24 hours so i didnt submit again for over a week.

Interestingly, for the first time since the competition started we have someone (SpaTaro) in the top 10 who is not taking this approach though and every single one of their matchups has played a unique strategy which means they are doing more than a static policy book.


Reply

2
Justin Gao
Posted 12 days ago

· 2749th in this Competition

I tried to build a three-tier real-time decision system consisting of planner, scheduler, and worker, responsible respectively for macro-level situation monitoring, micro-level fixed-task management, and actual execution. However, even with this approach, I still couldn't achieve the efficiency of a tape-based strategy. Improving efficiency in my micro-task management has been slow and frustrating—and that is the paradox of this game.


Reply

1
sobameshi
Topic Author
Posted 12 days ago

· 1295th in this Competition

That sounds very similar to what I’ve been seeing with my own runtime line. Even if you separate the system into layers, meaningful improvements often require changes that cut across several of them at once. Once that happens, it becomes much harder to isolate causes cleanly, so the iteration cycle slows down a lot.

At the same time, I still have the feeling that runtime agents may overtake tape-based approaches once they cross some threshold. What’s interesting is that the newer public non-runtime solutions already seem to be moving in that direction: they are no longer just “better tapes,” but tape + mechanism, with routers or state-dependent logic deciding which trajectory to follow.

So I’m still optimistic that runtime will win eventually—the hard part is getting through the stage where every useful improvement becomes a multi-layer coordination problem.


Reply

React
Chris Is Kaggling
Posted 15 days ago

· 3037th in this Competition

​I initially built a tape model simply because I joined this competition a bit late and wanted to study how others were playing, see the differences between strong models and ordinary ones, and analyze, dissect, and ponder the difference between the "essence of this competition" and the "essence of winning a top 10 spot."

​To my surprise, as everyone has shared, the proportion of runtime agents is very low and widely distributed, while meta tapes are updated heavily every day. I myself felt pretty good for a while after submitting a few tapes that got me into the top 10% on the leaderboard, but when I repeatedly thought about the final scoring system and the leaderboard ratings, I realized that trying to win in the end relying on tapes depends more on early-game winning streak luck combined with late-game rock-paper-scissors luck among same-generation tapes. However, whether it's the essence of the competition or the essence of winning, it ultimately points to runtime agents being the most stable solution under this game mode, so I also plan to try building my own agent in the time remaining, and I no longer intend to chase a good-looking leaderboard ranking.

​Though I still feel that by the end game, we'll probably see runtime agents coexisting with their tapes, haha


Reply

3
Prema Ananda
Posted 16 days ago

· 3410th in this Competition

Special thanks to everyone building replay-based bots — they're great benchmarks to calibrate a dynamic agent against.

Sure, my agent's rating is nothing to write home about right now, since it computes everything in real time. But working on it is way more fun than dealing with scripted moves — those eventually hit a ceiling. So I'm betting on real-time economy and dispatch logic — feels like the more promising path to me.


Reply

2
sobameshi
Topic Author
Posted 16 days ago

· 1295th in this Competition

I'm also starting to work on a runtime agent myself — honestly, seeing the reactions and discussion here gave me the push to finally start. I'm definitely getting a late start compared with some of you, but I'm going to give it a serious try. Good luck with yours too!


Reply

1
Prema Ananda
Posted 7 days ago

· 3410th in this Competition

@sobameshi Just curious about your current position around 401 on the leaderboard — is that submission running a dynamic real-time rule-based agent, or is it still driven by replay tapes? I’ve built a fairly comprehensive real-time bot that handles macro purchase planning, dynamic market trading, and worker task dispatching. Tuning and polishing the micro-efficiency to perfection is proving to be the hardest part, so I’m really curious which approach is carrying you there right now!


Reply

React
sobameshi
Topic Author
Posted 7 days ago

· 1295th in this Competition

Sorry to disappoint you, but unfortunately the submission sitting around rank 400 is the tape-router one. I currently have two submissions active: that tape-router baseline, and a separate real-time runtime agent. The runtime one is currently around 1640 score, which is roughly around rank 2000.

The tape-router side is actually quite automated at this point. I barely inspect the internals anymore — I mostly start from one of the stronger public baselines, run it through a fixed modification pipeline once, and submit the result. I update that line maybe once every three days, and it takes around 30 minutes each time. The runtime agent is where I’m spending most of my actual research time. The biggest problem is that its underlying economic base is still weaker than the strongest tape-based policies. For example, even against an opponent that simply PASSes every turn, the runtime still loses in final money to the strongest tape-based agents in most cases. Because of that, I’m currently focusing less on the reactive layer itself and more on things like market interpretation, capital allocation, and worker efficiency. So far, closing that basic economic gap has been much harder than I expected. So I definitely relate to what you said about micro-efficiency — that’s probably the hardest part for me too right now.


Reply

React
Prema Ananda
Posted 7 days ago

· 3410th in this Competition

Appreciate the transparent breakdown! I'll try to climb up to the ~1600 score level so our runtime bots can meet :) Mine is currently around 1200 score.


Reply

React
Andrew Reed
Posted 17 days ago

· 2394th in this Competition

Your experience is eerily similar to mine. Why do you think tape-replay is so effective? Is there just not enough opportunity to interact with (i.e., undermine) your opponent in this game? Are matches not sufficiently long enough (or random enough) for a dynamic agent to succeed consistently against tapes?


Reply

1
sobameshi
Topic Author
Posted 17 days ago

· 1295th in this Competition

Good questions. My current guess, based on what we've measured, is that the interaction surface between two agents is simply smaller than it looks. Most of the farm plan is fairly self-contained, so a stronger economic plan often stays stronger regardless of the opponent, with the shared market being the main place where direct interference really happens.

That said, I don't think dynamic play is weak. We've had several cases where adding a small reactive layer specifically for tape-like or near-mirror opponents made those matchups noticeably easier to win.

So my current picture is: strong underlying economy first, then a relatively thin adaptive layer for the parts of the game where the opponent actually matters. That reactive layer alone has never been enough to get us into the top 100, though, so I suspect there still needs to be something fundamentally better in the underlying plan as well.


Reply

React
cygn
Posted 17 days ago

· 2917th in this Competition

You've hit the nail on the head. I've also been in the top 10 with some tape replay approach and if you looked at what others were doing it seems like 85% of people do it like this. It's not particular interesting to me and I don't enjoy this competition atm for this reason.


Reply

1
sobameshi
Topic Author
Posted 17 days ago

· 1295th in this Competition

Hi cygn, thanks for the reply!

On the "not interesting" part, I feel exactly the same way, and it means something to hear that from someone that much higher up the ladder.

Lately, I've mostly given up trying to solve that part and settled for at least being honest with myself about what I'm actually doing — which is really what most of the post above was about.

One thing I do want to try, once our tape-making pipeline is stable enough that it no longer needs daily attention, is to build an actual runtime agent from scratch and put it in our other submission slot, just to see how far it can get on its own.

Alex Paul · 340th in this Competition · Posted 4 days ago
this competition is more like AI coding agents competing against each other
Basically, everyone is using coding agents, that's why the leaderboard is very fast-moving, and that's why everyone gets replaced so easily, and since very few people are actually focusing on RL and most others are using tapes, the competition is very low for actual thinkers (maybe)


React
5 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Vitória Freitas
Posted 2 days ago

· 9328th in this Competition

That is a fair point. The leaderboard is moving incredibly fast, which definitely points to heavy use of coding agents. It will be interesting to see if a well-trained RL model can eventually outsmart the AI-generated heuristics by the end of the competition.


Reply

React
Exposed
Posted 2 days ago

· 316th in this Competition

You are correct BUT that does not apply to the top private agents. LLM's can not develop a top agent yet - it can improve one public agents though. I saw a 147 point increase from a top scoring public agent with literally one line change.


Reply

1
Roxy
Posted 4 days ago

· 34th in this Competition

I think the availability of many strong public strategies has also contributed to this. Fine-tuning an already strong strategy may be more effective than developing one from scratch.


Reply

React
Rainfun
Posted 4 days ago

· 1690th in this Competition

我认为还有一方面RL很难找到正确方向。磁带路由相比较很轻松。


Reply

React
Khánh Vũ
Posted 4 days ago

· 1033rd in this Competition

it is correct

Mark Schatza · 2168th in this Competition · Posted 19 days ago
Learnings from PPO to 80k terminal cash
Hey all, was not expecting RL to be such a difficult challenge compared to Orbit Wars! And I'm not the only one struggling so wanted to share how I at least got to 80k terminal cash submission (but far from the top) so maybe someone else can crack my ceiling.

Throughput It's RL. We need to be fast. JAX end to end is what I'm using. Getting about 10k SPS throughput (although this keeps slowly getting chipped away at as I add features). Very CPU limited so rust/C++ may be a better option tbh. Telling codex to recreate with parity works great here. I enabled the full action space to the policy. Only masking illegal moves and limiting to 16 hands hired at a time.

Warm-up I tried two different warm-ups. First I tried rewarding each product individually from production to selling and adding them one by one. This worked for a bit, but after 5 products I had overfit the policy so much it struggled to do all 5. The next thing I did was use the open heuristic code and build some traces and train my policy only to match the heuristic replays. I didn't training for long, I believe I got to ~7% exact action parity with the replays. But that was enough to get the policy somewhat aware of how the game worked. On to real training now.

Training Classic PPO. Nothing too crazy here. Not much hyperparameter tweaking just LR, gamma and rollout length. 50% self play/25% active opponent/ 25% bank opponents. Train for 1000 updates with 128 rollout length. Eval against active opponent. If >60% win rate add to bank (FIFO w/ 5 latest banked opponents). If >70% promote to active. With some testing I determined temperature of 0.8 best for training and 0.5 best for formal eval and submission. Much later once the policy was somewhat competent I added the heuristic as 10% of the play taking from self play.

Reward Shaping I started with a 75/25 reward structure. With 75% being having more sales from produced product than the opponent (note sales from produced product, not any sales…) and 25% being more terminal cash than the opponent. As I've seen many times in the discussions, this will naively produce a melon farm. To combat this I added a exploration reward. +0.2 the first time it sold any of the nine sellable products, once per game. Was massive to give it incentive to try to produce other products. Eventually inverted the 75/25 to have terminal cash be the stronger of the two once it had learned to produce 80k+ a game. Finally last piece was to add a absolute scaling from 50k up to 120k final cash reward because it got stuck trying to game the market against itself rather than improve.

Feature Added some history information to track how much we've produced this game already. Calculated value horizons of current farm in different buckets of the future. And gave the policy some future exact information on the town demand rather than expecting it to learn what each building does. Better exact worker information, who was holding what, some previous state information.

Conclusion The above got my to 80k terminal cash purely RL with full action space allowed. And then I absolutely hit a wall that I have not been able to climb out of. The logits were very saturated as they needed to be with such important per state turns, but struggled to get exploration without collapse. Critic showed really high EV, but struggled to turn that into early game rollouts.

Next steps I progressively over the last few weeks made updates that have made policy worse and worse. Currently trying a more hybrid approach. An entirely new policy that only tells intents of each square and whether to upkeep this turn or skip w/ a executor underneath to perform the actions. Plus market purchases/sales. This policy is surprisingly struggling to even reach the highs of the old one even trying to follow the above playbook. May hop back to that best policy and see if I can resurrect it with fresh eyes.

Hope this helps! Best of luck RL'ing everyone.

P.S. All of the above is hand written, but I've written the entire codebase and guided all training exclusively through the codex app on my phone. I have a tailscale connected with a live dashboard that I can check from anywhere to see how my training/evals are going. Highly recommend!


6

1
10 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
hwe owe
Posted 17 days ago

· 570th in this Competition

I am current at 8 TH place and not using rl.i am trying a strategy that ml a model to sell things on correct timing


Reply

React
Roxy
Posted 19 days ago

· 34th in this Competition

To be honest, I'm not convinced RL is the right approach for this competition. Maybe I just haven't figured out how to make it work properly yet.


Reply

React
Praveen
Posted 18 days ago

· 1026th in this Competition

It indeed isn't… Peak dp btw bro :)


Reply

3
This comment has been deleted.

Friaseus
Posted 19 days ago

· 5485th in this Competition

Hey Mark, great write-up! Really impressive engineering setup, especially running the whole pipeline via Codex and Tailscale from your phone. 10k SPS in JAX is no joke.

I totally agree with your conclusion in the "Next steps" section, and I think you are exactly on the right track with the hybrid approach.

The main issue with pure RL in Kaggriculture is that the environment is incredibly unforgiving with its exact math. The AMM pricing curves (especially the quadratic behavior in some products) and the long time horizons (720 steps) make it a nightmare for a neural network to deduce the underlying financial formulas purely through reward shaping. It's very easy for the policy to find a local minimum (like the melon farm you mentioned) because it can't mathematically project the opportunity cost of an action 10 days into the future.

The breakthrough for many successful architectures is treating this less like a traditional grid-world game and more like a Corporate Finance and Operations Research problem.

If you build that "executor" layer you mentioned using deterministic pathfinding and task-assignment algorithms (like BFS or Hungarian matching) to handle the micro-logistics perfectly, your RL policy will be freed from the burden of learning how to walk without bumping into walls. You can then train your RL to act as the "CEO": making purely macro-decisions (e.g., when to buy land, which crop matches the town demand, when to hoard vs sell).

Best of luck with the hybrid architecture! You've got the hardest engineering parts figured out, wrapping a heuristic executor under your policy will likely shatter that 80k ceiling.


Reply

React
Alex Paul
Posted 14 hours ago

· 340th in this Competition

about the hybrid idea you ended on: if the executor handles the micro perfectly, what does the RL part actually output in your picture? choosing between whole plans, or more like setting parameters and targets the executor reads each turn? feels like the action space design is the make or break there and I am stuck on it too.


Reply

React
Gerardo Del Toro
Posted 18 days ago

Thank you very much for sharing your approach. I also participated in Orbit Wars and tried to apply RL again here. It seems the credit assignment problem and length of the game are quite an issue here. +1 -1 rewards are not enough signal haha.

May I ask whether your reward shaping of having more sales than the opponent is a +1 -1 zero sum reward, a quantity reward, and whether it's per turn or also terminal?

Also, I am quite concerned about for how long your train took to get some learning and these results. Was it 100M steps or how far?


Reply

React
Mark Schatza
Topic Author
Posted 18 days ago

· 2168th in this Competition

I tried all kinds of things with varying success. Most success I had was with splitting 0.75 reward for winning on cash and 0.25 reward with beating on produced sales revenue. And then added some small rewards on top of that for absolute cash trying to entice it to win by producing more rather than just putting its opponent down.

Oh I’m probably well in the billions of steps by now. Starting training a few days after the competition started. But most of that has been failed experiments. My best was probably around 500M before it plateaued if I had to guess. With a quick JAX setup samples shouldn’t be too much of a problem even on fairly poor hardware.


Reply

React
Zotar
Posted 18 days ago

· 4212th in this Competition

does a step mean a turn of the game or a backward pass or something else?


Reply

React
Mark Schatza
Topic Author
Posted 18 days ago

· 2168th in this Competition

One turn of a game.


Reply

React
This comment has been deleted.

Swachhith B
Posted 19 days ago

· 3702nd in this Competition

Using RL?

Young Uk Song · 668th in this Competition · Posted 3 days ago
Has anyone tried shared action heads or autoregressive decoding for BC to RL?
Hi all,

Thanks to everyone sharing their RL experiments here, the discussions have been useful to follow.

We're experimenting with a neural policy for the full game, starting from behavior cloning and then potentially fine-tuning with RL. The action space is fairly large and factorized into multiple categorical decisions.

Offline imitation metrics can look quite good, while closed-loop performance is still much less stable than the demonstrations, so I'm curious whether anyone has experimented with:

shared weights across similar unit/action heads, or per-unit heads on top of a spatial/unit encoder, instead of fully independent heads
autoregressive decoding for sequential market actions, where later decisions condition on actions already selected that turn
stabilizing the BC to PPO transition, for example KL to the cloned policy, critic pretraining/warm-up, lower policy learning rates, or other approaches
I'd be especially interested in negative results too, things that sounded promising but did not improve closed-loop play.

Happy to compare more detailed notes after the competition. Good luck in the final stretch!


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
WOOSUNG YOON
Posted 3 days ago

The problem is complex, and I do not have a clear sense of how to approach it on my own.

Its complexity appears to be quite high.

I have been reviewing replays and analyzing them in an effort to understand the issue.
Given that complexity, it does not seem that the problem can be resolved in a simple way.


Marcelo Correa · 8295th in this Competition · Posted 2 days ago
The farmer gets teleported back to the shed every day — and it explains most results
I ran a few experiments changing one variable at a time, and a single game mechanic explains almost every counter-intuitive result I got.

The daily reset. At the end of every day the game teleports the farmer back to (4,4), deletes all farm hands (they must be re-hired) and resets the HIRE cost. It's in the README, but easy to miss:

"Farmer and hired farm hands will spawn at the shed at the start of each day"

So every single day you pay a toll just walking back to work.

I measured that toll by comparing turns spent walking across all days vs day 0 only:

Area	walking (all days)	day 0 only
5×5	44%	29%
1×5 row	36%	29%
The ~15 p.p. gap is the toll. Farming far from the shed costs you every day, forever.

Three things this explains:

Gains saturate around 5 cells. I tested 1 cell up to the full 5×5; it grows until ~5 cells and then stops. It's not a lack of land — it's the walk back.

Farm hands don't pay for themselves. A hand spawns at the shed and vanishes every day: it suffers the same toll, and you pay growing Fibonacci for it. In my tests it was worse than no hand at all.

Crop choice beats adding resources. Same agent, only the crop changed (5×5, avg of 4 seeds):

Crop	Reward	vs starter
MELON	~24,200	4W–0L
STRAWBERRY	~11,400	4W–0L
WHEAT	~7,500	4W–0L
TOMATO	~5,200	4W–0L
Melon earns ~3× wheat — with 17 harvests vs 61 for wheat. It does less work for more money, because it needs fewer visits per cell per day. Counting actions is misleading.

Bonus: fertilizer is worth more than the animal. In the goose cycle, collecting fertilizer took me from $2,908 to $5,633 (+$2,725) — more than the 25 eggs (~$1,250). The by-product beats the product.

Three traps: (a) two units issuing PLANT with 1 seed = no planting at all, and the agent stalls silently; (b) FEED needs the wheat in the unit inventory, not the shed; (c) rule order matters — at (4,4), which is both shed and an empty cell, wrong ordering produced a 360-turn loop.

Two cautions: read the code, not just the README (README said melon max_yield_day=10; the code says 12), and note the leaderboard score is Elo, not money — reward and ranking are different scales.

Good luck! I'm currently trying to attack the toll by reducing distance (farming right next to the shed) instead of adding resources.


1
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Matheubern
Posted 2 days ago

· 7604th in this Competition

Esses pontos sobre o "custo de deslocamento" diário explicam boa parte das dores de cabeça que tive no início.

Passei por problemas bem parecidos: no começo, meu agente fazia viagens manuais até o galpão para descarregar a colheita porque eu não tinha percebido que tudo caía lá automaticamente na virada do dia. Eram dezenas de turnos desperdiçados só andando de um lado para o outro.

Também tive dor de cabeça com a corrida entre trabalhador e fazendeiro. Os dois calculavam a mesma célula como prioridade e iam até ela ao mesmo tempo. Quando o trabalhador chegava, o fazendeiro já tinha executado a tarefa — aí o ajudante ficava travado sem ação, queimando passos e o custo da contratação. Outro problema foi o bug de emitir PLANT com uma única semente no inventário e perder o turno sem nenhum feedback claro.

O aviso sobre o FEED precisar estar no inventário e a diferença no rendimento real do melão entre o código e a documentação ajudaram bastante. Eu já desconfiava dessas discrepâncias nos testes, mas agora ficou claro o motivo.



Nur · 1440th in this Competition · Posted 8 days ago
Has anyone had success with optimization-based planning?
I’ve been approaching Kaggriculture through mathematical optimization: valuing crops and animals, allocating capital and labour, managing storage and sales, then tuning the policy through simulation-based search.

I’ve found tiny improvements, but I’m struggling to approach strong public agents. The hardest part seems to be the coupling: planting, feeding, routing, cash flow and shared-market prices all affect each other, so improving one component doesn’t necessarily improve the final result.

Has anyone had success with MPC, mathematical programming, evolutionary search or similar approaches? I’d be curious what decision representation and objective worked for you and whether you ended up using adaptive planning or mostly predefined schedules. I will probably drop this approach. Thx in advance


1
7 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Gabriel
Posted 5 days ago

· 1631st in this Competition

I have tried mathematical optimization methods before, but there are too many variables, and relying solely on weight tuning of coefficients for different variables is like alchemy. But I still believe in the importance of math for this project.


Reply

React
Russell Kirk
Posted 5 days ago

· 1519th in this Competition

I'm trying a math heavy approach ^^


Reply

React
Gabriel
Posted 4 days ago

· 1631st in this Competition

Wish you success bro.


Reply

1
Nur
Topic Author
Posted 3 days ago

· 1440th in this Competition

i will build stuff on top of deterministic agent and hopefully give it some life and responsiveness. I chased LB a little bit and I realised I hated it, very low ownership of whats going on; just burning tokens. I'm inspired by RL agents doing well on LB, I will go back to modelling and failing if I have to !! Good luck guys


Reply

React
nouvya
Posted 7 days ago

· 2590th in this Competition

During my experiment with my bot, I also observed there exists coupling of multiple components, but I haven't yet found a solution to this problem. What I do is grid-searching combinations but that is very low-efficient and has low ceiling. I am planning to add local rl into my bot (which I guess can handle the delicate coupling part) but I am not sure how it goes.


Reply

React
Nur
Topic Author
Posted 7 days ago

· 1440th in this Competition

it feels like looking for a tiny object in the whole universe, I'm not sure searching is the right approach. If it exists ofc, pls share your solution after comp ends im curious. Good luck!


Reply

React
This comment has been deleted.

Nur
Topic Author
Posted 7 days ago

· 1440th in this Competition

i dropped it… just couldnt get it to work :( and i didn't have enough evidence to spend remaining time on this. Thank you regardless, good luck!!


Shair Khan · Posted 6 days ago
Hot take: RL is a variance tax—Kaggriculture is a deterministic macro-schedule problem
Look at the ladder convergence: closed-loop policy adaptation (RL, reactive MCTS, or state-machine micro-management) consistently loses to static macro-schedules + concurrent market-queue floor manipulation.

Why? Because opponent interaction here isn't spatial board combat—it's negative externalities via shared market inventory (draining supply or forcing $1 price-floor gluts).

If your agent is spending compute on spatial grid search, animal pathing state machines, or reactive tree branching instead of solving the Day 0–15 deterministic utility convex hull, you're optimizing variance, not expected reward.

Change my mind: show me a top-10 bot whose win rate depends on reactive opponent state rather than executing a superior open-loop macro script + market execution timing.

Optimization
Deep Learning
NLP

React
4 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Benny P
Posted 4 days ago

· 4814th in this Competition

Um The intention is to build a RL agent which would eventually learn the mechanics of the game. Atleast that's how I see it. The competition itself doesn't care about that. We have to have some form of "end" state so it's 30 days now (to measure and make people compete in a equal platform) and people start writing deterministic code for it :(


Reply

1
Shair Khan
Topic Author
Posted 4 days ago

@pbennyjoseph Spot on! That's always the double-edged sword with Kaggle simulation comps. When you put a fixed 30-day horizon, open-loop optimization/heuristics almost always out-pace RL in short-term convergence.

RL is definitely the cooler and "truer" way to learn the game mechanics, but hardcoded macro scripts end up taking the easy wins. Would love to see if someone can actually train a top-tier RL agent that can outsmart the static scripts by the end! 🚀


Reply

React
Mahog
Posted 2 days ago

· 6914th in this Competition

Would love to see if someone can actually train a top-tier RL agent that can outsmart the static scripts by the end!

2nd place has just confirmed that he is using RL (and I'm pretty sure there are many more people in top 10 using RL)


Reply

React
Mahog
Posted 2 days ago

· 6914th in this Competition

Also please stop spamming ai slop everywhere


Reply

React
aisormo P.H
Posted 4 days ago

· 162nd in this Competition

SpaTaro's agent is much more complex… I'm trying to find some inspiration from his replay.


Reply

1
Swachhith B
Posted 3 days ago

· 3703rd in this Competition

Exactly, He seems to have cracked RL

haideptry · 800th in this Competition · Posted 4 days ago
Fast Local H2H Arena & P&L Curve Analyzer (Squeeze Points Before the Deadline)
Hi everyone,

With only 2 weeks left before the competition deadline, relying solely on the 5 daily Kaggle submissions provides too little feedback to fine-tune end-game pacing and market reactions.

To help debug matches offline, I built an end-to-end evaluation suite and a clean modular baseline:

Interactive P&L & H2H Arena: Link to Notebook

Run multi-seed symmetrical head-to-head simulations locally (swapping P0/P1 seats to eliminate seat bias).
Visualizes cash accumulation trajectories across all 719 steps.
Deconstructs farm revenue and pinpoints starvation / shed overflow bottlenecks.
Structured Dynamic Route Baseline (~2200 Elo): Link to Notebook

A clean, readable starter agent with 3 distinct economic phases (Early grain bootstrap -> Mid-game high-value crops -> Terminal shed liquidation).
1-click generation of submission.tar.gz ready for upload.
Hope this helps anyone looking to validate their agents or get a reliable offline benchmark suite before the final buzzer!

Good luck to everyone in the final week! 🌾

Varadaraj Borkar · 2585th in this Competition · Posted 10 days ago
does copying opponent help?
it seems that we have full knowledge of what opponent is doing currently (in-game). and there are even days and turns, so we can answer for every action they make(given that we are the first to play; pass wont be considered since then even_num-1) and tie results in both winning right(w pts)?


React
9 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
守银摄金难铜
Posted 10 days ago

· 1163rd in this Competition

A draw causes the higher-rated player to lose points and the lower-rated player to gain points, though the effect is not significant when their ratings are close.


Reply

React
destbreso
Posted 9 days ago

· 922nd in this Competition

Draw simply means it is a deterministic measure that the opponent is playing the same agent as you. But beyond that, it is an easy feature to exploit for an advantage, precisely because it is deterministic to detect.

One possibility, and perhaps the most commonly used one, is simply to advance the sales by one turn. Given the characteristics of the game, this gives you a small advantage on each sale because the opponent's price depreciates. You just have to be careful that the sale you advance doesn't break the financing chain.

This is something the cloning teams are doing systematically, and it is easy to verify. Beyond that, there are other, more sophisticated ways to exploit it.

There is also a kind of "arms race" phenomenon, where a clone that introduces a counterplay gets countered by another clone, which then gets countered by yet another one.

Anyway, the fun never ends.


Reply

React
Omkar Kadam
Posted 6 days ago

· 510th in this Competition

I guess copying won't keep anyone high on leaderboard for long time eventually the score will fall as other people are also copying the codes and I guess most of them aren't even modifying them 🫢


Reply

React
Varadaraj Borkar
Topic Author
Posted 6 days ago

· 2585th in this Competition

hey Omkar, i did not mean it that way. what i wanted to ask is copying each move of the opponent during the ongoing game.


Reply

React
NITISH5236GOEL
Posted 5 days ago

· 6430th in this Competition

that wont work, the market is dynamic and there will be some delay between other persons sell/buy action and your sell/buy action, also Ive seen that many many people have their agents just copy my agent though they always loose.


Reply

React
Navneet
Posted 10 days ago

I think so @varadarajborkar


Reply

React
De DQ
Posted 10 days ago

· 9503rd in this Competition

You only see their action, not their farm state (cash, crops, land).

Both agents act on the same turn — you can't react to their move in the same step. If you mirror them (e.g., both plant the same crop), you both flood the market → price drops → you both lose.

What to do instead: Use their actions as a signal. If they're buying a lot, expect the price to move. Treat it like reading a stock ticker, not copying a chess move.


Reply

React
Varadaraj Borkar
Topic Author
Posted 10 days ago

· 2585th in this Competition

no, thats what i am trying to say. their action is what matters, which exact farm place did they do it doesnt. buying land it also an action, so we ain’t leaving any vital stuffs. you cant say both lose. its called tie right? and tie results in both being rewarded points. (correct me if i am wrong)

see i get that market thing. but was trying to find any loopholes if possible to climb the ladder(experiment).


Reply

React
De DQ
Posted 10 days ago

· 9503rd in this Competition

Ah got it. On ties: yes, both get same score for that episode. But leaderboard averages across episodes — one tie doesn't climb the ladder. You need wins.

On the "loophole": you see their action next turn, not same turn. So no counter-move. The only edge is: "they bought 50 wheat last turn → their supply hits in ~3 turns → I sell before that."

That's not a loophole, it's just market timing. But it is the real edge here.

Fastest climb: ignore opponent, build a solid market-timing bot first. Opponent modeling is Tier 2.

Good luck experimenting!


Reply

React

3 more replies
Profile picture for Roy Lampe
Profile picture for Varadaraj Borkar
Profile picture for istinetz
This comment has been deleted.

Varadaraj Borkar
Topic Author
Posted 10 days ago

· 2585th in this Competition

yes i can see the whole bunch of disadvantages being faced due to this. ig copying ain’t a great idea.


Reply

React
NITISH5236GOEL
Posted 8 days ago

· 6430th in this Competition

if you want, just copy someones code, and then modify it a bit so it is a bit original and maybe you can find a problemin thier AI or algo that you can fix.

submission trend -- is everyone catching up that fast really?
August 20th:



Last night (already started going down):



Today (going down already):




React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
nofreewill42
Topic Author
Posted 6 days ago

· 904th in this Competition

Is the leaderboard just a war of Codex and Claude Code soldiers?

I P Tharun Gowda · 8177th in this Competition · Posted 8 days ago
I have only reached 20$k can we and if yes then how to use ml or other things to get started?
i have like a basic bot which is not that good, it only makes like 20k money. like how to improve from here on can we use ml ?. i asked ai bots they told me at competitions like this you have a time constraint so loading heavy modules will not do any benefit .So how do you move from here on ?.btw i am very new.


React
6 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Mark Schatza
Posted 5 days ago

· 2165th in this Competition

My finding for pure ML so far has been tailoring rewards is the best path to a high performing agent. Start small like rewarding it for watering plants/feeding animals then add bonuses for cash etc. Good luck!


Reply

React
Navneet
Posted 6 days ago

Let me know if it's possible @iptharungowda


Reply

React
BillDoser
Posted 6 days ago

· 5861st in this Competition

Yes. Reinforcement learning is possible. That's the route I've taken. It presents a long series of challenges and I'm not sure how it will work out.


Reply

React
nouvya
Posted 7 days ago

· 2591st in this Competition

I am also trying to develop my own bot apart from those tape bot, but so far my bot only reached around $47k and could not progress further. I plan to add some local rl and see if it can do better.


Reply

React
千早爱音
Posted 8 days ago

· 570th in this Competition

Click code. Find the notebook you like and copy.


Reply

9
Rahul Balakrishnan Adhi
Posted 7 days ago

· 6312th in this Competition

You got 226th by doing that or is it just a random advice you gave? 😅


Reply

React
This comment has been deleted.

Civitasmass
Posted 6 days ago

· 1848th in this Competition

If you want a medal, I think copying a notebook is probably the best strategy for new. you can get a pretty high score just by tweaking it a bit, but you won’t really learn much haha.


Reply

React
Rahul Balakrishnan Adhi
Posted 6 days ago

· 6312th in this Competition

Haha! I surely would love another medal as it would get me to Expert as well…but I think for the time being I will continue learning and implementing something of my own. Any tips? 😜


Reply

React
Rahul Balakrishnan Adhi
Posted 6 days ago

· 6312th in this Competition

Actually I am intrigued by your profile, you started a few months ago and have done a great job…how many years of experience do you have? As a student I would love to hear from you


Reply

React
Civitasmass
Posted 5 days ago

· 1848th in this Competition

"attention is all you need"

My Journey So Far — Mechanics, Breakdowns, and What's Actually Working
Hey all, wanted to share my progress and the hard lessons I've picked up since day one. This turned out to be the deepest comp I've touched and I figure writing it out helps both me and anyone else grinding through it.

Where I started vs. where I am

Early submissions sat in the 500-600 rating range, which is basically "agent is alive but losing money." Current best is ~1399 (v80+sheep). The delta wasn't from clever ML - it came from understanding what the engine actually does vs. what the README claims.

What I got wrong early

Treated this like a tabular comp. There is no train.csv. The only way to know if something works is to submit or run it against the real kaggle_environments.make() engine. Cost me a week.

Trusted the README over the source code. The README claims town demand "escalates 2x after day 10, 4x after day 20." That logic does not exist in the shipped engine (kaggle_environments 1.32.6+). Flat shop consumption only.

Local win-rate is anti-correlated with the LB in market-driven sims. My best local performer was literally my worst LB result. The signal I trust now: real LB replays, not my own bench pool.

What actually moved the needle

Replay fingerprinting: pulling 20-60 real opponent replays and diffing their per-product sell volumes vs. mine. Found I was dumping 1,300+ wheat/game while top opponents sold ~400 wheat + ~180 strawberry.

Yield-aware FERTILIZE: the FERTILIZE op doubles tile yield, but only if you apply it 2 or fewer days before a production event. Gating on whether a yield falls in day..day+2 fixed it (0 to 54 fertilize actions).

CARE gating: pending_care_bonus only banks when the animal is also fed the same day. Caring an unfed animal is a wasted action. Fixing that: +25% milk, +51% wool.

Day-28 liquidation: reward is your coin balance at step 720 - shed stock scores zero. Bypassing sell reserves from day 28 onward recovered ~$2.8k/game.

Route commitment for feeding: PICKUP was 1,100+/game vs. the meta agent's 135. Adding a commitment contract (hand locked to one animal until delivered) cut animal deaths from ~10/game to ~1.

The hurdles I'm still fighting

Ladder path-dependency: a submission plays ~35-40 episodes in the first 24h then slows to hourly, so a score is provisional for 2-3 days. You can't re-plan off one reading.

The meta agent is a shared public notebook. A large fraction of the field runs byte-identical code (8 COW + 4 SHEEP, 62 plants, 14 hands, 264 hires, 0 deaths). The ceiling past ~1400 requires actually beating that fingerprint consistently.

Import errors on submit: any file reference in agent code crashes silently on Kaggle's evaluator. Cost me ~1800 rating points across two subs before I found it.

TL;DR for anyone early in this comp

Read the engine source (kaggle_environments/envs/kaggriculture/kaggriculture.py), not the README.
Pull your own LB replays and compare action counts vs. top opponents - that's the only honest signal.
Fix mechanical bugs before optimising strategy - they compound in non-obvious ways.
Expect 1-2 days for a score to stabilise; don't submit again until the current one has 30+ episodes.
Good luck everyone - 19 days left and still a lot of room.


Siva Kumar · 3886th in this Competition · Posted 9 days ago
My Journey So Far — Mechanics, Breakdowns, and What's Actually Working
Hey all, wanted to share my progress and the hard lessons I've picked up since day one. This turned out to be the deepest comp I've touched and I figure writing it out helps both me and anyone else grinding through it.

Where I started vs. where I am

Early submissions sat in the 500-600 rating range, which is basically "agent is alive but losing money." Current best is ~1399 (v80+sheep). The delta wasn't from clever ML - it came from understanding what the engine actually does vs. what the README claims.

What I got wrong early

Treated this like a tabular comp. There is no train.csv. The only way to know if something works is to submit or run it against the real kaggle_environments.make() engine. Cost me a week.

Trusted the README over the source code. The README claims town demand "escalates 2x after day 10, 4x after day 20." That logic does not exist in the shipped engine (kaggle_environments 1.32.6+). Flat shop consumption only.

Local win-rate is anti-correlated with the LB in market-driven sims. My best local performer was literally my worst LB result. The signal I trust now: real LB replays, not my own bench pool.

What actually moved the needle

Replay fingerprinting: pulling 20-60 real opponent replays and diffing their per-product sell volumes vs. mine. Found I was dumping 1,300+ wheat/game while top opponents sold ~400 wheat + ~180 strawberry.

Yield-aware FERTILIZE: the FERTILIZE op doubles tile yield, but only if you apply it 2 or fewer days before a production event. Gating on whether a yield falls in day..day+2 fixed it (0 to 54 fertilize actions).

CARE gating: pending_care_bonus only banks when the animal is also fed the same day. Caring an unfed animal is a wasted action. Fixing that: +25% milk, +51% wool.

Day-28 liquidation: reward is your coin balance at step 720 - shed stock scores zero. Bypassing sell reserves from day 28 onward recovered ~$2.8k/game.

Route commitment for feeding: PICKUP was 1,100+/game vs. the meta agent's 135. Adding a commitment contract (hand locked to one animal until delivered) cut animal deaths from ~10/game to ~1.

The hurdles I'm still fighting

Ladder path-dependency: a submission plays ~35-40 episodes in the first 24h then slows to hourly, so a score is provisional for 2-3 days. You can't re-plan off one reading.

The meta agent is a shared public notebook. A large fraction of the field runs byte-identical code (8 COW + 4 SHEEP, 62 plants, 14 hands, 264 hires, 0 deaths). The ceiling past ~1400 requires actually beating that fingerprint consistently.

Import errors on submit: any file reference in agent code crashes silently on Kaggle's evaluator. Cost me ~1800 rating points across two subs before I found it.

TL;DR for anyone early in this comp

Read the engine source (kaggle_environments/envs/kaggriculture/kaggriculture.py), not the README.
Pull your own LB replays and compare action counts vs. top opponents - that's the only honest signal.
Fix mechanical bugs before optimising strategy - they compound in non-obvious ways.
Expect 1-2 days for a score to stabilise; don't submit again until the current one has 30+ episodes.
Good luck everyone - 19 days left and still a lot of room.


Aaweg Bhaladhare · 262nd in this Competition · Posted 9 days ago
How are people making RL work in Kaggriculture?
I am convinced reinforcement learning can work in Kaggriculture. The real question is how to make it learn reliably and generalize against the leaderboard field. Some strong agents show varied, state-dependent behaviour consistent with learned policies, although replays alone cannot confirm their private implementations.

The game looks like a natural RL problem, but a straightforward formulation is surprisingly difficult. A match lasts 719 decisions, each turn can contain actions for several workers plus market orders, and an early purchase or crop decision may affect the result hundreds of steps later. Legal actions also depend heavily on position, inventory, cash, land, and previous commitments.

In my experiments, flat end-to-end PPO can learn some mechanics and occasionally beat weaker agents, but it has not yet matched a strong engineered policy consistently. More training alone has not fixed the main failures. The policy often makes individually plausible choices that do not form a coherent economy across a full match.

The approaches that currently seem most promising to me are:

Hierarchical RL: choose a persistent economic plan at a daily or phase level, then use a lower-level controller to execute it.
Recurrent policies: retain the chosen plan and a summary of opponent behaviour instead of treating every observation independently.
Autoregressive action heads: choose worker actions sequentially so later workers can condition on earlier assignments.
Imitation for mechanics, RL for strategy: initialize movement, planting, feeding, and other routine execution from demonstrations, then relax the imitation constraint while learning strategic choices.
Opponent leagues: train against several strong policies and past checkpoints instead of optimizing against one opponent or one averaged critic.
Search-generated value targets: branch from real states, evaluate a small set of legal strategic alternatives with the simulator, and train a conservative selector from those counterfactual outcomes.
The last approach has been particularly informative. It turns an extremely large raw action space into a smaller decision problem: keep the current plan or choose among a few complete, executable alternatives. It also supplies direct negative examples—actions that looked reasonable locally but reduced the terminal result.

Evaluation is another challenge. Results can change with the map, opponent and seat, so a small improvement against one opponent may disappear on a broader panel. Training curves alone also do not show whether a policy has learned a stronger strategy or merely adapted to its training opponents.

For people who have tried RL here:

Do you train one policy over every worker and market command, or separate strategy from execution?
Are recurrent policies materially better than feed-forward policies here?
What reward or return formulation gives useful credit across the full 719-step match?
Do you use self-play, a fixed opponent league, population-based training, or a mixture?
Have you found model-based rollouts, MCTS, evolutionary search, or offline RL more effective than PPO?
How do you keep exploration coherent across a match rather than adding unrelated randomness every turn?
Roughly how many simulated games did you need before seeing stable improvement?
How large does an evaluation panel need to be before you trust a result?
Is CPU simulation enough for useful progress, or has GPU training been essential?
I am not asking anyone to reveal a complete solution. Even high-level observations about what failed, what stabilized training, and how progress was evaluated would be useful.


2
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Syed Asad Ali
Posted 9 days ago

· 327th in this Competition

I went down several of these roads without RL, so some negative results that may save you time.

On 2: I can't speak for recurrent networks, but I can price the information you'd want them to carry. I run an opponent identification layer that tracks the rival's visible farm and pins their agent family by around step 12. Acting on that memory is worth about $38 a game to me, against roughly $224 if I let it cheat and read their future sells directly. The opponent summary is thin here. Plan persistence is also a non-issue: the strongest public agents hold one plan for hundreds of steps already.

On 3: sequential worker conditioning is necessary. I built a scheduler that assigns each hand conditioned on the ones already placed, and it still lost heavily to a much dumber fixed script. Separately, adding workers has zero marginal value in my measurements. Coordination between workers is not the binding constraint.

On 8, which I think is the most important question you asked: bigger than you expect, and the design matters more than the size. Play every seed in both seat orders and average the pair into one number before you do statistics, or you will double-count. Then hold out a seed block you never look at while tuning. I have watched the same change measure +2,301 on one "fresh" block and -1,259 on another, purely from having selected on the first. There is also a trap specific to this game. Weed spawning consumes one random draw per empty tile on both farms, so when you drop your agent into a recorded game your own play changes which shops the town unlocks. The opponent's recording is then executing a plan for a world it never saw, which flatters you badly. Split your results into the games where the shop sequence survived and the ones where it re-rolled. Against the top ten my win rate is 78% in re-rolled games and 40% in preserved ones. Only the second number is real.

On 9: CPU is plenty. My simulator does about 670k steps a second on one core. The bottleneck is encoding observations, not the game.

On your last bullet, search-generated value targets: that is the one I would bet on, and it is the only one of the six that needs no RL. The reason imitation from replays stalls is that you cannot ask the expert what to do in the states your own policy reaches, and you only have their recordings. If the simulator generates the targets, that loop closes.


Reply

React
cm391
Posted 9 days ago

· 1500th in this Competition

you should think about what you are actually modelling. expecting rl to learn optimal placement of crops and mapping workers is a lot of work… try and understand the game. you should understand the game as one-player to begin with (maximise production and money) then move on to pvp mechanics and market tricks when playing against someone else.


Reply

React


Yan Zhou · 11th in this Competition · Posted 10 days ago
Is the current ranking system reasonable?
I noticed a very interesting submission: https://www.kaggle.com/competitions/kaggriculture/leaderboard?submissionId=56135774

It lost its first match, then went on to win 51 matches in a row, but its score is still only around 1500.


1
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
nilochan
Posted 10 days ago

· 619th in this Competition

Most likely the opponents are ranked lower below you, hence you’re getting <10 points for every win ( usually it’s easy to get 50-100 points during startup phase ). Not sure how the system match the opponents


Reply

React
hwe owe
Posted 10 days ago

· 581st in this Competition

The ranking system of this competition is really bad


Version 3 -:

gaolicious · 620th in this Competition · Posted 3 hours ago
Suspected Elo Race Condition When Episodes Finish Concurrently
I noticed something strange with the Elo updates for my agent and wanted to check if this is expected.

Submission 56392391 (team 16778012), submitted at 11:30:58 UTC:

Episode	Created	Ended	Initial → Updated
111205191	11:30:58	11:34:41	base → 600.0
111206504	11:37:45	11:43:13	600.0 → 675.99
111207617	11:41:45	11:43:13	600.0 → 702.27
111208702	11:45:49	11:49:38	702.27 → 819.38
The part that caught my attention is that 111206504 and 111207617 finished at the same time, but 111207617 still has 600.0 as its initial score, even though 111206504 had already updated it to 675.99.

It looks like both episodes may have read the same score before applying their updates, so the +75.99 from 111206504 was effectively overwritten by the result from 111207617.

Are Elo updates for episodes of the same submission serialized, or are they applied as deltas? If two episodes finish concurrently, I'm wondering if they can both read the same score and overwrite each other like this. If so, that could be a problem.

If this is indeed what's happening, it would be great if it could be fixed before the competition deadline.



Shair Khan · Posted 6 days ago
Quick math check on $fib(n)$ labor scaling vs. land amortization in Kaggriculture
With ~16 days left, local self-play rollouts are splitting into two camps: lean single-farmer animal compounding vs. multi-hand aggressive land clearing.

Looking at the action economy (24 turns/day, 1 action/turn, movement + placement/harvest tax), the Fibonacci labor cost multiplier ($fib(n) = 1, 1, 2, 3, 5, 8, 13, \dots$) makes hiring >3 hands drain 12+ coins/day just on startup before accounting for pathing waste to the center shed.

Two quick questions for anyone sitting on the upper ladder:

Is multi-hand labor ever net-positive past Day 10 compared to locking capital into quadrant unlocks ($1k/$2k/$4k) + high-tier ongoing animal products (milk/wool/melon hinge cliff)?
Are top policies exploiting the simultaneous 1-unit-at-a-time concurrent market queue resolution to force opponent sell orders straight into the $1 price floor, or is deterministic inventory timing safer?
Drop your Day-15 marginal utility threshold per tile.


jordeazy · 4321st in this Competition · Posted 19 days ago
First simulation comp, what should I actually be learning?
This is my first competition like this. I'm around 1,600 and not climbing, and honestly most of my edits make me do worse.

I've been reading the discussion boards and learning about RL and heuristics (completely new to me), but I'm not really sure what I should be focusing on.

What should I be learning/doing? Is there a subject or a body of knowledge behind this kind of competition that I'm missing?

What do people actually use? I've mostly been writing code with an AI assistant. Is that what everyone's doing, or are there tools and approaches that serious entrants rely on that I don't know exist?

I'm stuck in a loop of having an idea, using AI to help me make the change, it tells me it nets more coins or a better win rate, I submit, it does worse. I can't seem to figure out a system to keep everything organized, accurately test, or improve.

Not looking for your winning solution, just direction on what to learn and what to use so I can actually get some positive improvement and learn a thing or two!!

Thank you in advance.


React
6 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
shanzhong8
Posted 6 days ago

· 1541st in this Competition

learning from public notebook is a good start, once you understand the weakness of public notebook then you can start to climb the ladder.


Reply

React
Cho Royou
Posted 9 days ago

· 1146th in this Competition

I feel like we should learn to direct AI rather than letting it direct us. Self-training easily leads to overfitting, so why would AI be any different?


Reply

React
Yusuke Hayashi
Posted 10 days ago

· 1933rd in this Competition

I only started participating in Kaggle competitions last month myself, so I’m still finding my way, but I’d be happy to share my experience.To begin with, I’m a software engineer, not an expert in machine learning or data science.

I make frequent use of AI as well. I primarily used Codex to learn the basics and to analyze public notebooks. What became apparent was that some participants had previously competed in "Orbit War"—a competition with some similarities—where reinforcement learning methods had won. The article on Orbit War was also helpful. However, I also noticed that the top of the kaggriculture leaderboard (at the time) wasn't dominated by reinforcement learning; instead, the leading entries were mostly modifications of existing, high-performing tape.

At first, I attempted to program agents capable of executing powerful actions, but I was completely outclassed.

Consequently, I built a system designed to rapidly discover high-performing "tapes." While tapes offer limited flexibility for modification, they aren't entirely rigid, so I devised ways to engineer even stronger ones.

Recently, reinforcement learning methods seem to have come to dominate the top of the leaderboard, so I have started exploring that approach as well. However, I am concerned that the lack of a high-end GPU might put me at a disadvantage; nevertheless, I am looking for ways to combine this with my existing strengths.

Regardless of the approach, gaining a rapid understanding and insight into the game is essential—such as identifying optimal actions within daily cycles, or recognizing moves that top-tier players avoid.


Reply

1
jordeazy
Topic Author
Posted 10 days ago

· 4321st in this Competition

no love from the community? brutal. sad face.


Reply

React
Nikita
Posted 10 days ago

Yeah, I find the forum strangely dead, I think Kaggle forums have seen better days…

As for your question, I don't have time to type out a big response right now, I might come back later. But with kaggle competitions, even ones involving simulation/agents, evaluation loop is your everything. You've already encountered it: you do some improvements locally, then you upload and it fails. That means your local evaluation loop should be improved to correlate with the public leaderboard better. Otherwise your feedback loop is too long -- waiting for your agent to converge in the public LB takes too much time. Do you follow the top episodes dataset? https://www.kaggle.com/datasets/kaggle/kaggriculture-episodes-index You could start by analyzing top replays and testing your agent against them. Unless your agent already makes at least 50k gold it probably won't do too well, but it can give your AI coding agent a good local feedback -- play against strong economies and try to compete with them by copying them / trying to exploit market dynamics. AI is pretty good at mining these data if you give it good tools.

Most of the submissions are pre-computed, or static clones of strong replays -- afaik not many people have reached good results with an actual reactive agent, so don't be discouraged just yet.


Reply

3
Matin Urdu
Posted 9 days ago

· 2871st in this Competition

Unfortunately I wrong a long-ish response a week ago, but forgot to submit it, so it seems to be gone. But Nikita summarized it well. Here is something you could try: "deterministic" notebook tapes seem to be the way to go, so you could try an imitation learning approach for your RL agent to just try to copy the notebooks for now. Once you have a good baseline you can apply any standard RL algorithm and have them learn. Honestly, the "RL" aspect is not necessarily the problem in this competition. I can't speak in detail, since I am mostly experimenting in my free time / downtime, but it seems that the main problem is just the enormous action space + long horizon. However, even these two issues can be resolved by picking a clever action space; the most "annoying" part of this problem is the mutual circular dependence of the various actions.

What I mean in is the following (this is an advanced problem, you can first try to just do imitation learning as a good baseline): When you are thinking of where to move your units etc. you are also considering what to buy, what to sell. If you decide to buy item X, then this might influence your strategy on whether to sell y and have your unit perform action z. Which means we have a conditional distribution, which can be solved by doing multiple "forward passes" (e.g. first decide what to buy, then condition selling on what to buy, then condition which action to take on on the previous actions etc…). However, you potentially still have a circular dependence! Knowing what to buy influences what to sell, but once you know what you want to sell that also influences what you want to buy… etc.


Alex Paul · 252nd in this Competition · Posted 12 days ago
how much time does it take for submission to converge?
The previous top 1's discussion threads claim that 90% of games converge in the first 5 hours; some say it takes 48 hours.What is the actual number to be used to balance iteration speed too


React
8 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
say4n
Posted 11 days ago

· 4775th in this Competition

Anecdata: I see it happening after ~5-10 runs unless it keeps climbing, then it takes longer.


Reply

React
nouvya
Posted 11 days ago

· 2618th in this Competition

Based on my experience, 5 hours should be enough to see roughly which position your agent is at. Though it's true that the agent may still increase its position on the board, but the score increment is diminishing if you are over 4 - 5 hours. So checking around 5 hours should be reasonable.


Reply

React
Steve421471
Posted 12 days ago

· 348th in this Competition

I don't think you can put a single number on it. I've had agents that kept climbing for 4 days and I've had agents that peak after 4 hours and then fall continuously for 3 days.


Reply

1
Alex Paul
Topic Author
Posted 11 days ago

· 252nd in this Competition

Is there a way to know if the agent has converged? Is it the win rate?


Reply

React
Liu Classmate
Posted 12 days ago

· 879th in this Competition

我认为差不多 24 小时之内就会收敛，你可以看胜率和最高战绩，多提交几次，很快就能验证的，如果数据分析你不敢下结论，你或许可以求助于 model


Reply

React
Mohit
Posted 9 days ago

4 hours probably


Reply

React
Pand
Posted 9 days ago

· 448th in this Competition

5 hours is a good timestamp i'd say, even tho later on its kinda chaotic


Reply

React
千早爱音
Posted 10 days ago

· 206th in this Competition

it depends. If you lose accidentally in a very low mark (like around 1000), this will really hurt your score and I recommend you to submit your agent again.


Pedro Joás · 8511th in this Competition · Posted 9 days ago
How can I use the city’s shops more effectively to increase my profits?
I’m not quite sure how to check the shops’ status and decide where to sell in order to maximize my profits, especially by prioritizing shops with higher demand.


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Jaume Batlle i Ferrer
Posted 8 days ago

· 5132nd in this Competition

You don’t sell directly to a specific city shop. All your SELL orders go to the common market. The unlocked shops then periodically consume specific products from that market inventory. So the useful thing about shops is not “where to sell”, but which products will have extra absorption. You can check the currently unlocked shops in obs["town"]["unlocked_shops"], and combine that with obs["market"]["inventory"] and obs["market"]["prices"]. For example, if a Yarn Store is active, wool gets extra demand; Pizza Shop supports milk/tomato/wheat; Smoothie Shop supports strawberry/milk, etc. Strategically, I wouldn’t simply produce the product of the newest shop. I’d look at: current market stock + price + unlocked-shop absorption + your future production + visible rival production + time remaining A shop is most valuable when it helps absorb a product that would otherwise become oversupplied. With premium goods especially, dumping too much into the market can still collapse the price even when a relevant shop is open. So think of shops as extra market drainage, not as separate buyers.


Stanislav Tsepa · 2143rd in this Competition · Posted 11 days ago
Automating strategy experiments in Kaggriculture
I’ve been thinking about how much of Kaggriculture experimentation could be automated, especially for policy search / evolutionary approaches.

I have an open-source repo called AutoEvolve that I built for running iterative experiment → evaluation → improvement loops automatically:

https://github.com/MrTsepa/autoevolve

I haven’t tested it on Kaggriculture yet, so I’m not claiming it works out of the box here. But the general setup seems potentially relevant for things like evolving strategies, running large batches of simulations, evaluating candidates, and iterating automatically. I’ve previously used it for a player-vs-player strategy competition, where guided evolutionary search produced pretty strong results.

Posting it in case it’s useful to anyone experimenting with similar approaches. Would also be interested to hear if people here are already doing something along these lines.


Lê Quang Cảnh · 2736th in this Competition · Posted 11 days ago
Your opponents are probably replaying the same tapes you are (I measured it)
I kept running into games where the opponent farmed almost exactly like me. So I measured it, and the number is higher than I expected.

I pulled the replays of the last 26 games of my scoring submission, extracted the opponent's farm commands, and compared them against 51 tapes I had reconstructed from the public CC0 replays.

opponent matched >60% of farm turns to a known tape:  25/26  (96%)
   matched 100%:                                       1
   matched 95-97%:                                     3
mean match over 8 games sampled in detail:            87.4%
So my local bench and the real arena are drawing from the same pool. Beating a tape locally is not independent evidence that I will beat the field, because the field largely is that tape.

Here is what that does to a score over a run:

first 20 games   win 95%   opponent mean 1473    600 -> 2190
games 21-45      win 68%   opponent mean 2316   2190 -> 2380
games 46-65      win 70%   opponent mean 2378   2380 -> 2426
last 20 games    win 56%   opponent mean 2419   2426 -> 2432
Elo pairs you by rating, so by 2400 you are meeting people running the same kind of tape and winning about half. The score converges to the average of the crowd replaying tapes, not to the strength of the team the tape came from. That team sits around 2888 while my replay of it settled at 2432.

The reason I am actually posting is the three bugs this exercise found in my own tooling.

Extraction was off by one. The first step of a replay is initialisation. Before I fixed that, opponents matched my tapes at 0.1 to 0.6 percent and I nearly concluded that nobody was copying anything. The check that caught it: extract your OWN commands from your OWN replay and compare them to your own agent. That has to come out 100%. If it does not, your extraction is wrong, not the world.

My evaluation harness had a seat bug. It always put my agent in seat 0 and the opponent in seat 1, no matter which seat the tape was originally recorded in. A "98/120 = 82%" number that I had used to pick which submission to field was measured in the wrong seat.

My seat hypothesis was wrong too. The local simulator said a seat-1 tape run from seat 0 only gets 70%, against 88.9% for a native seat-0 tape, so I built a two-seat agent to fix it. Real match history says otherwise:

seat 0:  36/49  win 73%
seat 1:  24/34  win 71%
No real difference. Head to head, the two-seat agent and the old one produced identical results, 31/36 for both, matching seat by seat. I spent a while assuming that was a bug in my comparison harness. It was not.

I am curious whether other people see the same 96%. If your opponents are mostly tapes as well, then bench win rate is a much weaker signal than it looks, and the gap between local and arena is not noise, it is the same distribution measured twice.


istinetz · 249th in this Competition · Posted 13 days ago
could we please increase the k factor of the elo?
I submitted an agent, that i expect to level out to be about 2400 rating, based on previous agents.

It is currently rated around 2050, after 11 hours, and winning about 70% of games, Playing about 5 games an hour, at about 4 points per game: this would take about 43 more hours to reach equilibrium, even without considering the fact that the winrate will drop as it gets closer to it's true rating.

… That's a lot!

It slows down iteration a lot - I'd have to wait ~55 hours for each version to hit approximate equilibrium. What is the point of having 5 submissions a day, if i cannot even evaluate 2?

My point is, this can be easily fixed by:

increasing the initial k-factor of the elo, OR
halving the decay of the k-factor, OR
adding a momentum term.
Thanks for listening :)


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
VijaiKurianMathew
Posted 12 days ago

· 3022nd in this Competition

I am also facing the same issue. earlier I was in 2300 range now due to the above mentioned reason my score is low



Sandeep063 · 4203rd in this Competition · Posted 25 days ago
Reached ~$15K average — what should I investigate next?
Hi everyone,

I'm fairly new to game-agent competitions and Kaggriculture, so I'm trying to learn the process rather than just copy an existing solution.

I have implemented my current farming/economic strategy and, against the starter agent, I'm getting around $15,000 average final money.

At this point, I'm not sure what the right next step should be.

My current approach is roughly:

Observation → understand the game mechanics → build a deterministic strategy → optimize crop/animal production and selling → run simulations.

Now that I have a reasonable baseline, I'm trying to understand how experienced participants approach the next stage.

For example:

How do you identify the bottleneck in your current agent? Do you analyze your own replays first, or study strong submissions/replays? What metrics do you look at besides final money? How do you decide whether to investigate market pricing, production, labor, land expansion, movement efficiency, etc.? Do you normally change one variable at a time and run many seeds to validate an idea? How do you distinguish a genuine improvement from something that only works on a particular seed? At this stage, is it better to continue with heuristic/optimization-based strategies, or is there a reason to start looking into RL or other learning approaches?

I'm particularly interested in how experienced competitors go from a decent baseline to finding their next improvement.

If you could describe your workflow or the first few experiments you would run from a ~$15K baseline, that would be really helpful.

For context, I'm deliberately trying not to copy a top solution. I want to understand how the strategy was discovered so I can develop my own agent.

Thanks!


React
3 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
shanzhong8
Posted 25 days ago

· 1542nd in this Competition

Maybe some strategies on buy and sell


Reply

React
VijaiKurianMathew
Posted 25 days ago

· 3022nd in this Competition

Analyze your own losses first, not top replays. Top replays show you the ceiling; your losses show you your leak. I mined 3.26M actions across 214 episodes and found our #1 loss was premature_sale — $1M+ dumped into crashed markets, not weak farming.

Metrics beyond final money:

Per-day bank curve — where does growth stall? (Our "elbow day" insight: animals started 2 days earlier = +$10k by Day 30)
Failure taxonomy — classify every loss: premature sale / animal escape / shed blockage / idle cash
Zero-latency sells — winners sell the same turn they harvest (41.6% of the time); check your Δt between HARVEST and SELL
CARE alignment — do you CARE on production hours {6,12,18}? Elite: 25% aligned. Most bots: ~10%
First 3 experiments at $15K

Opening spend audit: Is all $3,000 deployed on Turn 0? Idle cash on Step 0 compounds badly. Our route spends $2,982 immediately.
Herd timing: Cows take 8 days to mature but produce for 22+ days. Buy cows Day 0–4, not later. This one change was worth +$10k for us.
Sell timing: Never dump >20 units of premium goods (strawberry/melon/milk/wool) in one order — convex price curves crash them to $1 at just +63–77 units over baseline inventory.

Reply

1
Zukas F.
Posted 2 days ago

I’d treat ~$15K against the starter as a useful baseline. My next step would be to understand where the agent loses value and whether improvements hold across different conditions.

Here’s the workflow I’d suggest:

1. Inspect your own replays first. Track final money alongside missed maintenance, wasted production, unsold inventory, and worker actions. Look for recurring problems rather than assuming that movement, idle workers, or unused cash are necessarily inefficient.

2. Use controlled comparisons. Freeze your current version and compare each candidate against a small, fixed opponent pool using the same seeds, configurations, and player positions. Track both money and win rate. Expand the sample when results are uncertain, and keep some seeds separate from those used for tuning.

3. Test one concrete hypothesis at a time. My first experiments would investigate:

Liquidation: Is valuable production left uncollected or unsold at the end?
Scheduling: Are workers missing urgent tasks or duplicating work? Workers can share tiles, so collision avoidance isn’t needed.
Investment: Does another worker, animal, or land purchase increase final money after maintenance, labor, and selling costs?
4. Use stronger replays to generate ideas. Study the conditions behind a decision, then test whether the same reasoning helps your agent. Observing a successful strategy doesn’t establish which choices caused its success.

I’d keep improving heuristics while there are clear, measurable problems to fix. RL may become useful, but the ~$15K milestone alone isn’t a reason to switch.


Roy Lampe · 8525th in this Competition · Posted 10 days ago
Selling fertilizer
I'm new to the compitition and trying to understand the rules / behaviors. The readme states you can sell fertilizer. To test this I wrote a simple agent that buys and then sells fertilizer. The buying works as expected, money decreases from 2000 to 1900, and I have 1 unit of fertilizer in the shed. In the next step I attempt to sell the fertilizer. This doesn't work. Money stays at 1900 and there is still 1 unit of fertilizer in the shed. Why won't it sell? What am I missing?

Here's the code for the agent:

def agent(obs):
    day = obs["day"]
    hour = obs["hour"]

    market = []

    if day == 0 and hour == 0:
        market.append(["BUY_PRODUCT", "FERTILIZER", 1])

    # Sell fertilizer?
    if day == 0 and hour == 1:
        market.append(["SELL", "FERTILIZER", 1])

    # Default return
    return {"farmer": ["PASS"], "hands": [], "market": market}

React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Roy Lampe
Topic Author
Posted 10 days ago

· 8525th in this Competition

I downloaded kaggle environment locally and reran the test. Locally it worked as expected (the fertilizer was sold). Looks to be a versioning issue. The local copy has version 1.32.7 while the notebook version uses 1.29.3. Is there a plan to upgrade to the latest?

(local)
pip list installed | grep kaggle-env
kaggle-environments       1.32.7

(notebook)
pip list installed | grep kaggle-env
kaggle-environments                      1.29.3

Reply

React


mikelou1 · 23rd in this Competition · Posted 14 days ago
Proposal: Show provisional Bradley-Terry rating.
Hi! Usually we don't have to worry about shakeups in simulation competitions. However, as the provisional leaderboard uses a different system than final ratings, it could lead to different leaderboard positions than the actual result. Is it possible to show the provisional Bradley-Terry rating too so we have a better idea about our position, or just simply use BT for the private leaderboard? Thanks!


React
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Bovard Doerschuk-Tiberi
Kaggle Staff
Posted 13 days ago

· 8964th in this Competition

The plan is to write BT to private leaderboard if possible.


Reply

React
Temitayo Gbolahan
Posted 10 days ago

· 2025th in this Competition

Does everyone reset to 600 and play for 2 weeks or the BT is applied on the episodes played during those 2 weeks regardless of the current rating and with no Elo point reset???


Justin Gao · 2788th in this Competition · Posted 13 days ago
A Three-Layer Brain for Kaggriculture
Although the leaderboard is now flooded with various pre-programmed tape-based strategies—where all planning is finalized at the very beginning, and every crop, animal, and employee in each turn operates like finely meshed gears, squeezing out every last bit of efficiency—I still feel that this might deviate from the original intent of the game. An "agent," after all, should at least have an agent loop to play the game, shouldn't it?

Now please allow me to share my design architecture.

A Three-Layer Brain for a 1v1 Farming Race
Kaggriculture: a 1v1 farming simulation. 30 days × 24 steps = 720 steps. You win if you have more cash than your opponent at the end.

Building the agent, the interesting tension was this: the game is nearly deterministic, but the execution layer is not trivial. Every unit — a crop or an animal — needs a sequence of visits across different days (seed, water daily, harvest at the right day, replant; or buy, place, feed, care, collect). If the executor re-decides "what's nearest" every step, it spends most of its time walking and keeps interrupting multi-day tasks.

So we split the agent into three clean layers.

+------------------------------------------------------------------+
|  Layer 1 — Strategy                                                |
|  WHAT to produce, WHEN to sell, how many hands, when to buy land.  |
|  portfolio(day) -> {crops:{...}, animals:{...}}; sell_policy;      |
|  num_hands_for_day(day); land_days. Objective = relative cash.     |
+------------------------------------------------------------------+
                │ emits commands only
                ▼
+------------------------------------------------------------------+
|  Layer 2 — Execution state machine (cerebellum)                    |
|  Turn the portfolio into per-unit lifecycles and run them.         |
|  Two orthogonal dimensions:                                        |
|    • ProductionUnit — a view over one board tile; reports needs.   |
|    • Worker         — one farmer + hired hands; holds a persistent |
|                       queue of coarse tasks.                       |
|  Real engine state is the ONLY source of truth.                    |
+------------------------------------------------------------------+
                │ sits on a deterministic substrate
                ▼
+------------------------------------------------------------------+
|  Layer 3 — Deterministic production schedule                        |
|  Given planted_day and our watering/feeding choices, every harvest  |
|  day is computable. Crop/animal milestones are derivable, not       |
|  stochastic.                                                       |
+------------------------------------------------------------------+
Layer 1 — Strategy
This layer decides the plan, not the movements. It produces, once per day:

portfolio(day) — crop and animal targets,
sell_policy — per-product sell timing,
num_hands_for_day(day) — how many workers to employ,
land_days — when to buy land.
Its objective is relative cash: since winning is about having more than the opponent, it reasons about my cash minus the opponent's cash, not my raw cash. It says nothing about where to place or which tile to water — that belongs to Layer 2.

Layer 2 — Execution state machine
Layer 2 takes the portfolio and runs the full lifecycle of every production unit. It has two orthogonal dimensions.

ProductionUnit — one object per board tile. It holds no private state about the goal; each step it reads the real tile and derives what that unit wants right now:

class ProductionUnit:
    def needs(self, tiles, day, plant_plan, portfolio):
        tile = tiles[self.y][self.x]
        # plant unwatered -> WATER; plant mature -> HARVEST
        # animal unfed -> FEED; animal with product -> HARVEST; ...
Worker — the farmer plus hired hands. Each holds a persistent queue of coarse tasks, which survives across steps and across the day boundary:

class Worker:
    tasks: list[Task]       # persistent queue
    current: Task | None
    def tick(farm, private, day, survival=None): ...   # advance current one step
Task — a coarse, multi-step object bound to a single unit. It advances itself across steps (for example PICKUP cow → walk → PLACE). While a worker is on a task it is not pulled away to do something else. One worker serves many units; tasks are inserted continuously.

Two properties are load-bearing here:

Engine state is the only source of truth. The cerebellum keeps no private copy of its goal; it reads the current tile every step (planted_day, watered_today, yield_units, consecutive_unwatered, fed_today are all on the tile). The only persistent state it keeps is the worker's task queue — because a multi-step action must survive without interruption.

Coarse multi-step tasks are not interrupted. This is what makes multi-stage work (place an animal, feed it, harvest from it) actually complete instead of being abandoned midway.

Layer 3 — Deterministic production schedule
Layer 2 is able to reason ahead because Layer 3 makes the timing computable. The engine's production rules are deterministic: given when a unit was planted/placed and the choices we make about watering/feeding, the days it produces are fixed.

def crop_milestones(crop, planted_day):
    cd = CROPS[crop]
    harvest_d = planted_day + cd["first_yield_day"]
    # water every day until harvest; harvest at first_yield; replant after

crop_milestones("WHEAT", 0)        # [(0,WATER),(1,WATER),(2,HARVEST)]
crop_milestones("MELON", 0)        # water day0..9, harvest day10
crop_next_op("STRAWBERRY", 5, 15)  # ongoing crop: harvest every interval days
Because the schedule is known, the cerebellum can move from per-step greedy selection to schedule-driven lookahead routing: precompute each unit's milestones, order the workload into a spatially coherent route, and hand each worker a short consecutive segment of it. That lets the executor be both efficient (fewer wasted steps walking) and complete (nothing is left waiting, because the route covers the scheduled work).

How the layers fit
Layer 1 decides what and when, and produces a portfolio + timing plan. It never picks a tile or a movement.
Layer 2 turns that plan into actual unit lifecycles and executes them as a state machine over real engine state, using persistent coarse tasks.
Layer 3 makes the production timing deterministic, so Layer 2 can route workers ahead of time instead of reacting greedily.
The whole design rests on one idea: separate what's strategic from what's reflexive, and let the reflex exploit the fact that the environment's production is fully computable.



Albert Einstein F Muritiba · 6332nd in this Competition · Posted 9 days ago
Beyond Single-File Agents: How to Submit a Modular Multi-File Python Project
Kaggle Project Structure & Submission Guide
This guide explains how to structure your agent codebase, test it locally, and submit it to the Kaggle Environments platform.

1. Minimal Project Structure
To keep development simple, modular, and free of complex import path issues, all agent source code is placed inside the src/ directory:

my-project/
├── pyproject.toml              # Dependency manager (uv)
└── src/                        # Agent source code
    ├── main.py                 # Submission entrypoint (must define the agent function)
    ├── agent1.py               # Decision logic and heuristic for your agent
    ├── helper_module.py        # (Optional) Helper classes, parsers, or utilities
    └── constants.py            # (Optional) Game constants and parameters
2. The Entrypoint (src/main.py)
Kaggle Environments strictly requires the root submission file to be named main.py and expose a callable named agent:

# src/main.py

# Import the function that implements your agent's decision logic
from agent1 import my_agent as agent

# This is only for local run
if __name__ == "__main__":
    import webbrowser
    from kaggle_environments import make

    OPPONENT = "random"  # Test opponent: "random", "pass", or "starter"
    EPISODE_STEPS = 720  # Simulation length in turns (full season)
    SAVE_HTML = True     # Generate interactive visual replay in the browser

    print(f"Starting local test against '{OPPONENT}' ({EPISODE_STEPS} turns)...")
    env = make("kaggriculture", configuration={"episodeSteps": EPISODE_STEPS}, debug=True)
    env.run([agent, OPPONENT])

    p0, p1 = env.steps[-1]
    print("-" * 45)
    print(f"Your Agent (P0) : ${p0.reward:,.2f} | Status: {p0.status}")
    print(f"Opponent   (P1) : ${p1.reward:,.2f} | Status: {p1.status}")
    print("-" * 45)

    if SAVE_HTML:
        with open("resultado.html", "w", encoding="utf-8") as f:
            f.write(env.render(mode="html", width=1000, height=750))
        webbrowser.open("resultado.html")
3. Environment & Credentials Setup
3.1 Install Dependencies
Using the uv package manager:

uv add kaggle-environments kaggle
uv sync
3.2 Kaggle Authentication
To enable direct terminal submissions:

Visit kaggle.com/settings/api.
Click "Create New Token" to download kaggle.json.
Save the file to your system and configure proper permissions:
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
Important: Ensure you click "Join Competition" on the competition web page to accept its terms before your first submission.

4. Local Testing
Before submitting, test your agent's behavior locally:

uv run python src/main.py
This runs a complete match, displays rewards and status in the terminal, and automatically opens the interactive replay in your default browser.

5. Packaging & Submission
Kaggle requires main.py to be at the root of the compressed .tar.gz archive.

Quick Option: Automated Script (submit.sh)
Run from the repository root, optionally passing a version description:

./submit.sh "My agent version description"
(Runs tests, cleans bytecode caches, prompts for confirmation, packages, and submits automatically).

Manual Option: Step-by-Step
Step 1: Create the .tar.gz archive
tar --exclude='*__pycache__*' -C src -czf submission.tar.gz .
(The -C src flag changes directory into src/ and . bundles all files directly into the root of the archive, excluding temporary cache folders).

Step 2: Submit to Kaggle
uv run kaggle competitions submit kaggriculture -f submission.tar.gz -m "Version description"
6. Monitoring Submissions
Check the submission queue status:

uv run kaggle competitions submissions kaggriculture
Status PENDING: The agent is queued for evaluation.
Status COMPLETE: The agent passed validation and is actively playing leaderboard matches.
Status ERROR: The agent crashed or exceeded runtime limits during validation.
submit.sh


Alvaro Mendizabal · 3676th in this Competition · Posted 11 days ago
Reproducible Kaggriculture environment and observation audit
I've started an open research repository for Kaggriculture: https://github.com/alvaromendizabal/kaggriculture

The first milestone contains a pinned official simulator, deterministic reference games, observation-only candidate features, source-mechanics checks, resumable artifacts, and two executed notebooks. It does not claim a competitive agent or leaderboard performance.

The code is available under the MIT license. The next research phase focuses on crop lifecycle value, labor allocation, price impact, storage, and terminal liquidation, with controlled feature-family comparisons. Feedback on the evaluation methodology is welcome.


Hanserong · 1151st in this Competition · Posted 23 days ago
Determinism is an argument against RL here, not for it
Even though "the rules are fully deterministic, so a network should be able to learn them.", the determinism is precisely the reason RL is the wrong tool, and to be concrete about the one place where a learned model does pay.

The engine is public, the price function is public, and a seed reproduces a season exactly. When you can call the model as often as you like, the problem is search and planning, not learning a policy from returns. Reaching for policy gradients here is choosing the slower of two available tools.

Three concrete obstacles, in increasing order of how much they matter:

Imitation already fails, and imitation is the easy version. A behaviour-cloning run on our side reached high next-action accuracy on held-out frames from strong recorded games and then scored roughly an order of magnitude below the trajectories it was cloned from when it actually played. High per-frame accuracy does not survive 719 steps of compounding: one wrong action puts the farm into a state the training distribution never covered, and everything after that is off-policy. If supervised learning with perfect labels cannot reproduce the policy, RL from scratch with no labels and a terminal-only reward is strictly harder.

The action space is combinatorial, not flat. Each turn emits one farmer verb, up to a dozen hand verbs, and up to ten market orders. A flat policy head over the joint space is hopeless. The obvious fix -- factorise into per-unit heads -- breaks the coupling that matters most, because market orders settle by list index: the sells that finance a purchase must sit at lower indices in the same list. Independent heads have no way to preserve that ordering, and when it breaks the purchase fails silently and every later step executes against a farm that no longer matches the plan.

Credit assignment. 719 steps times a dozen units, with reward arriving only at the end.

The general point: on a deterministic, fully-observable, cheaply-queryable model, learning should be in service of search rather than a replacement for it. Happy to be argued out of this if someone has an RL run that beat a searched schedule -- I have not seen one posted.


React
7 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Rishi Gottumukkala
Posted 23 days ago

· 1128th in this Competition

Haven’t really succeeded doing RL end to end but I have seen some moderate success building a hybrid Heuristic + RL model


Reply

React
Omkar Kadam
Posted 23 days ago

· 655th in this Competition




Reply

2

12
Rishi Gottumukkala
Posted 22 days ago

· 1128th in this Competition

Lmao, most of my work in terms of RL has been in opponent modeling. Havent seen much success running a PPO/Transformer model end to end (mine maxed out at around 40k). Havent really got it to work yet so I cant say for certain if its a good idea.


Reply

5
Tims
Posted 11 days ago

· 2856th in this Competition

我做的就是RL，hh


Reply

React
CemBas
Posted 13 days ago

· 1003rd in this Competition

It needs be completely deterministic until the results can't be predicted. Check LangGraph, you NEED edges.


Reply

React
David Ben Gurion
Posted 13 days ago

· 647th in this Competition

Yes, I feel like here, a rule-based/heuristic model would definitely be the way to go (atleast in my experience) 😄


Reply

React
AGSaturn
Posted 16 days ago

· 3265th in this Competition

The data is too sparse. it's not easy to use rl. The best way maybe is to use the rules


Reply

React
Reyhan Ksatria
Posted 15 days ago

· 893rd in this Competition

Yeah, I think so. RL doesn't work well for this competition. It's very hard to apply, not like the Orbit Wars competition, which was easy to apply an RL mechanism to.


Reply

React
AGSaturn
Posted 14 days ago

· 3265th in this Competition

i agree with you. Orbit wars are different.


Reply

React
ryan panda
Posted 13 days ago

· 5802nd in this Competition

it is hard but maybe it might be better than rule based only after a certain point since it doesn't really have a limit but rule based does even though it is easier


守银摄金难铜 · 437th in this Competition · Posted 16 days ago
Here are a few observations I’ve made about how the rating system behaves.
As long as you keep winning, before around 2300 rating, each game usually gives you roughly 100 points, depending on the rating difference between you and your opponent. After 2300, the gain drops to around 60 points, and then gradually converges until each win gives you less than 10 points.

A loss seems to accelerate this convergence quite dramatically, by roughly 500 rating points. For example, if a submission loses a game at 1500, then by the time it reaches around 2000, the rating gain per win may already have converged to below 10 points. This seems to happen regardless of whether you lost to someone’s older submission or their latest one.

In other words, if you are unlucky enough to run into a very strong opponent early, it can take much longer for your submission to reach what I would consider its “true” rating.

For roughly the first 80 games, matchmaking seems to happen on a fairly fixed schedule: every four minutes or so, you get one or two new matches, regardless of whether your previous games have finished. If you happen to face a slow agent, you can sometimes see three games running at the same time.

After about 80 games, matchmaking slows down significantly. From what I’ve seen, it takes roughly 10–15 minutes before the next batch of matches is assigned, and each batch still usually contains one or two games.

If you can keep winning until you are within about 500 points of your “true” rating, then after roughly five hours your rating is more or less settled. At that point, the fluctuations are usually within about 100 points. Afterward, it may slowly drift downward as new users submit stronger agents.

If you lose early, though, it seems to take considerably longer to reach the same stable rating.


5
6 Comments
1 appreciation comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
千早爱音
Posted 15 days ago

· 207th in this Competition

The ranking system is a kind of shit.


Reply

2
Hao Yang
Posted 14 days ago

· 2945th in this Competition

I think this ranking system is really unfair, and like you said, if you’re unlucky and lose a few games before hitting 1500 points, it’s hard to get a high score. After that, the match pool becomes really small, and you always end up playing against the same few people.


Reply

React
S. B.
Posted 16 days ago

· 2623rd in this Competition

Dont forget to take into account that the top is kind of its own meta game. Scattered across the ladder are different solutions, some of which are naturally strong against your solution. So even though you might have a solution that is measurably good at opponents at the top, it might lose out to a few opponents with different strategies in lower tiers.

So don't get fooled by what you consider to be "true"-rating, because im also under the impression that after submission closing, your agent will play those same lower tier opponents a few times too and dropping you down in the process.


Reply

1
守银摄金难铜
Topic Author
Posted 16 days ago

· 437th in this Competition

I don’t feel like the counter-matchup effect is actually that significant. There are two or three opponents I’ve barely ever beaten, but my rating hasn’t really dropped much because of them.

Giulio Ravasio is probably the most obvious example — across my two submissions, I’ve lost about 15 games in total to his two submissions.

Some agents counter mine, but mine will also counter other agents, so it tends to balance out over time.

Running into one of those bad matchups early is definitely pretty tilting, though. Luckily, we get five submissions a day.


Reply

React
守银摄金难铜
Topic Author
Posted 16 days ago

· 437th in this Competition

You’re right. For players in the top 10, as long as they don’t go on a losing streak, the matchmaking pool seems to become pretty narrow.

There are actually quite a few lower-ranked agents that could beat them, but those agents don’t necessarily make it into the top 20. As a result, the high-ranked players may simply never get matched against them.


Reply

React
Michael Timbs
Posted 14 days ago

· 1317th in this Competition

It just takes time. My best submission peaked at 6th and took about 4 days to drop to about 700th. By the time it peaked it would not have gotten into the top 200 if id submit it at that time


Reply

React

Appreciation (1)
宗宗没有英文名
Posted 14 days ago

· 104th in this Competition

Great observations, thank you!


3정훈 · 1075th in this Competition · Posted 13 days ago
From replay orders to actual trades: a cash-flow breakdown
A replay might contain ["SELL", "STRAWBERRY", 100], but that does not mean 100 strawberries were sold. And even if the order fills, those units may trade at different prices.

I put together a notebook that reconstructs the fills and turns them into a revenue-and-cost breakdown: Kaggriculture | From Orders to Actual Trades

Here is what the gap looks like on one public leaderboard replay. The units sold and the reconstructed revenue come from the notebook's ledger. I calculated the estimate separately, from the replay's raw SELL orders and the quote recorded at the start of each turn.

Player	Units offered for sale	Units sold	Order-quantity estimate	Reconstructed sales revenue
A	1,751	1,456	$107,392	$90,079
B	1,332	1,332	$96,976	$92,407
For Player A, the quantity sold fell 295 units short of the quantity requested. Player B's orders filled in full, but realized revenue was still $4,569 below the estimate because execution prices differed from the pre-turn quotes. The first comparison involves both quantity and price; the second isolates the pricing gap.

There are two things to account for.

Prices change within an order.

The engine settles trades one unit at a time. Each sale above the $1 floor adds market inventory, which can lower the quote for subsequent units. The engine pairs the two players' orders by queue position. Within each position, it quotes the next eligible unit for each player from the same inventory snapshot, attempts both fills, then repeats with the updated inventory.

To isolate that effect, here is a hypothetical sale starting at the default inventory of 10,000, with no opponent trades, no town consumption, and no shed limit:

Product	Quantity	Quantity × starting quote	Reconstructed proceeds	Estimate / proceeds
Strawberry	100	$12,000	$3,847	3.1×
Milk	122	$19,520	$6,227	3.1×
Wool	105	$21,000	$7,974	2.6×
Melon	300	$75,000	$26,627	2.8×
Carrot	450	$15,750	$8,418	1.9×
Wheat	400	$10,000	$8,313	1.2×
The quantities use the engine's T constants. This is an illustration of the pricing effect, not a feasible single-turn sales plan. In the first four rows the ratio also reflects units that sell at the $1 price floor rather than at a gradually falling quote: 38 of the 100 strawberry units, 46 of 122 milk, 46 of 105 wool and 142 of 300 melon. Excluding those units from both the estimate and the proceeds gives ratios of 2.0×, 2.0×, 1.5× and 1.5×. Carrot and wheat have no floor sales.

The difference can also be small. In the notebook's demo the farmer sells in small batches, and the same order-quantity estimate, again computed outside the notebook, comes to $8,907 against the notebook's $8,892 of reconstructed revenue, a difference of about 0.2%. The size of the error depends on the product, market inventory, order size, and the other player's trades.

Orders may fill partially — or not at all.

The engine reads only the first maxMarketOrdersPerTurn orders of a turn, 10 by default, and discards the rest. Of those, sales stop when the shed runs out of the item. Purchases can stop when cash runs out, and product or animal purchases also need room in the shed. Later orders retain their original queue positions.

The shed itself can change before trading begins. A farmer might drop goods off, pick something up, or build a structure before a hand places an animal in it. The notebook applies those actions in order, then replays both players' market queues with the resulting stock.

Checking the reconstruction

My saved copy of this replay includes the tile grid only twice per game day, but the notebook needs it at every step. So I regenerated the episode from its seed and recorded actions, then verified that every field the saved copy retained matched, including both players' cash at all 720 steps. The ledger checks below run on that regeneration. The quote check runs on the original recording, where it is not circular.

The reconstruction produced 826 ledger entries. The checks were:

Reconstructed net cash changes match the recorded changes for all 1,438 player-turns.
Total absolute error and the largest single-turn error are both $0.00.
Separately, all 6,480 recorded quotes match the installed engine's price function using the episode's parameters.
The cash check compares net changes per player per turn, so offsetting errors within one turn could still pass. It is a consistency check rather than proof of every individual fill.

The notebook's tables break the season into revenue by product, with units and average sale price, and spending by category. Its charts show the cash balance through the season, daily cash in and out, spending by category, and how each product's selling price changes as market supply accumulates. You can also compare realized revenue with what the same quantities would have earned at base prices.

It requires both players' full private observations and the farm's tile grid at every step. If your saved replay omits the grid, regenerate the episode using the original seed (in downloaded Kaggle replays this is info.seed; configuration.seed is often null), the configuration, the recorded actions, and a matching engine version, then check the regenerated observations against the fields you retained. This notebook uses kaggle-environments==1.32.7.

To point it at another replay, load it into a dict and run A = analyse(my_episode), then inspect A["report"] before reading the P&L.

If you try it and find a replay that does not reconcile, please share the engine version and the failing turn. I'd be interested in tracking down the difference.


Less · 398th in this Competition · Posted 15 days ago
Report a bug：Winners are deducted points, losers are added points
Report a bug, in the last round of the game, I had more coins than my opponent, but was deducted points as the losing team.

![e4ec2b7a-1ec0-43a9-9a55-10b71cf47360](url to embed)


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Addison Howard
Kaggle Staff
Posted 15 days ago

· 511th in this Competition

Thanks for reporting,

Looks like a possible visual bug, as our records show on the backend that you gained 105.8, and Kyohei lost 4.5 on that episode in actuality. We'll look into it.


Reply
![](image-6.png)


Zotar · 4237th in this Competition · Posted 14 days ago
runTimeout is inherited at 1200s — is that intentional for 720 steps ?
While checking the time budget for this competition I noticed that runTimeout is not set by the environment and falls through to the platform default. I wanted to check whether that's deliberate, because the arithmetic works out differently here than it did for Orbit Wars.

In kaggle-environments 1.32.7, envs/kaggriculture/kaggriculture.json sets:

episodeSteps: 720 actTimeout: 1 remainingOverageTime: 60

It does not set runTimeout, so the value comes from schemas.json, where the default is 1200 seconds.

Orbit Wars declares the same actTimeout of 1 and the same 60-second overage bank, and also leaves runTimeout inherited. The only difference is episode length: 500 steps against 720.

That matters because the worst case an agent can legitimately consume is episodeSteps × actTimeout + remainingOverageTime. For Orbit Wars that's 560 seconds, and for two agents run one after the other, 1120 — inside the 1200 budget. For Kaggriculture it's 780 per agent, and 1560 for two sequentially, which is over.

Whether that's a problem depends on how the agents are scheduled. In core.py the runner uses pool.map only when every agent reports is_parallelizable, and in agent.py build_agent returns True for that only in the UrlAgent case; a file, a callable or a builtin name all return False and go through list(map(…)) sequentially. On the parallel path a step costs the slower agent, so the worst case is 780 seconds and there's no issue. On the sequential path it's 1560, and env.run() raises DeadlineExceeded once the wall clock passes runTimeout.

So two questions:

Are competition episodes run through the parallelizable path, so that the effective ceiling is 780 seconds rather than 1560? If so, is the inherited 1200 still the intended value, or was it simply not revisited when episodeSteps went from 500 to 720?

I ask mainly because it affects how much of the per-turn second is safe to actually use. If the sequential path is ever in play, two agents each averaging much over 0.8 seconds a turn would end the episode early rather than resolve it, and that outcome wouldn't be visible as a timeout on either agent.


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Bovard Doerschuk-Tiberi
Kaggle Staff
Posted 13 days ago

· 8963rd in this Competition

The two agents are run in parallel so 1200s is a safe upper bound.

Version - 4

aisamhottman · 1953rd in this Competition · Posted 17 days ago
Final Bradley-Terry scoring: three clarifications (team score, ties, play rate)
Thanks to the Kaggle team for confirming earlier that the final leaderboard will be a single Bradley-Terry tournament over episodes between agents that are both still active at the deadline (topic 732931). Three follow-up questions so teams can plan their last two submissions correctly:

Team score. Each team keeps two active submissions. In the final BT ranking, is the team placed by the better of its two submissions, by each submission separately (so a team could occupy two ranks), or by some combination? Put differently: is the second slot a hedge with no downside, or does a weaker second submission pull the team's final score down?

Ties. Kaggriculture produces exact ties fairly often (identical-lineage mirror matches). In the final BT fit, are ties counted as half a win for each side, dropped, or handled with a tie-aware variant (Davidson / Rao-Kupper)?

Play rate after the deadline. Will the episode rate be increased during the ~2-week post-deadline window, as it was in Halite IV and Orbit Wars, and roughly how many episodes should each active submission expect to play in that window?

A precise answer to (1) in particular changes how teams should use their last submission slot in the final days. Thank you!


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Addison Howard
Kaggle Staff
Posted 16 days ago

· 557th in this Competition

Hi there,

The team score is based on the better of its two submissions (a team can't occupy two ranks). The second slot can be viewed as a hedge with no downside.

Ties are counted as half wins for each side.

We always hope to increase the play rate after the deadline, but can't make any commitments now to what/how many.


destbreso · 1028th in this Competition · Posted 18 days ago
Why are the strongest agents being retired from the leaderboard?
Something unusual happened on the ladder today. It is not just that the #1 is a different submission than yesterday: the #1 spot has changed hands more than ten times over the day, and the whole top has turned over with it. Most of the names I was tracking yesterday are simply not there anymore. And it does feel like an anomaly at this point in the competition, with no changes to the engine.

Yesterday I x-rayed the #1 with my replay instrument (the newest 40 public episodes). It was the most adaptive agent I have measured in this competition (a true mutant): every turn open to change, first divergence at t=0, all three channels moving, and a 40-0 ledger with a median margin of +13,065. Rating 2,977 after 77 episodes, still climbing at about +5 points per episode.

Then it stopped playing. Its last public episode came about five hours after its validation game. A submission only stops receiving episodes when its own team fields newer ones, so it was withdrawn while still warming up.

Today's #1 (at the moment I ran the x-ray) is a different team and a completely different kind of agent. Within each shop world it is a near-fixed route with small repairs, 0.6 to 3.9 percent of turns varying and first divergence around t=440-590; the adaptive-looking part is a route fork at t=72-144 that tracks the shop draw. Ledger 23-17, median margin +547, and 19 of its last 40 games were against close siblings of itself.

So in one day the crown went from a pure adaptive crushing uniformly to a router over replays grinding narrow wins inside its own family, and it kept rotating all day. Which makes me wonder: are strong agents being fielded briefly and pulled back on purpose, maybe to keep their routes out of everyone's replay harvesting, or saved for the final days? Or is this ordinary churn at unusual speed?

                                The king Yesterday (09/01/26) vs The king TODAY (09/02/26)
 

 

 

 

 

 

 

 

 

 

Both x-ray runs are public (and runs daily, keeping the record) if you want the chart-by-chart view and full analysis:

yesterday (09/01/26) https://www.kaggle.com/code/destbreso/x-ray-your-agent?scriptVersionId=346638531

and today (09/02/26) https://www.kaggle.com/code/destbreso/x-ray-your-agent?scriptVersionId=346874562


React
6 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
greySnow
Posted 17 days ago

· 7579th in this Competition

Once upon a time, there was a Kaggle RL competition, in which 3rd place simply did behavioral cloning on top 1,2. Since then, Kagglers learned not to leave on LB their strongest agents 🤣 People check their shiny new RL agent, get convinced it's very strong and take it down. Simple.


Reply

13
destbreso
Topic Author
Posted 17 days ago

· 1028th in this Competition

People who build strong agents are smart, so yeah, I don’t really see any flaws in your logic 😂


Reply

React
Navneet
Posted 18 days ago

Thank you for the agent's info @destbreso


Reply

1
Bharat Kumar0925
Posted 17 days ago

· 3753rd in this Competition

Maybe due to 1st position person testing their other strategy so kaggle not testing always top agent, I guess testing last2 agents submitted by team.


Reply

React


mikelou1 · 25th in this Competition · Posted 20 days ago
Proposal: Reset leaderboard
A single bad RNG or a strong opponent can completely wreck the ELO. Also it honestly just takes too long to get to the top of the leaderboard. We need almost 30-50 winning games to get to 2500+, and thats something like 5 hours of waiting, if not more because of loses.

If we reset the ELO of everyone's submissions to 600, it would fix this problem. The top of the LB will be at maybe ~1300-1500 instead of 3000 and you can converge to your actual score in less than 30 minutes.

Can we consider this fix?


React
6 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Paritosh Kumar Tripathi
Posted 18 days ago

· 1147th in this Competition

I think instead of a reset if the number of games can be increased, it will help speedup convergence and will be useful for lb feedback based improvements to our agents.


Reply

React
Matthew Anderson
Posted 19 days ago

· 2411th in this Competition

Can you give some examples of this with some screenshots or something? This has not been my experience at all. Usually submit a build and eventually start losing and the curve just flattens where I'm trading wins and loses? Yeah sometimes I lose a game and I still slowly claw up ~100 more ELO, but honestly whats the point? You can see the curve and you know you're still going to effectively top out near where you already are.


Reply

React
djschmit
Posted 18 days ago

· 2751st in this Competition

These two agents are identical submissions, but after 3-4 days ended up with a 248 elo difference.


Reply

React
Gaurav06520
Posted 19 days ago

· 2359th in this Competition

I might be wrong but at the end of the submission they will start the leaderboard again for 2 weeks or something like that which will normalize the scores and ratings.


Reply

React
mikelou1
Topic Author
Posted 19 days ago

· 25th in this Competition

Still feedback is slow and submitting -> get a useful feedback takes days


Zhenyu Zhang · 651st in this Competition · Posted 22 days ago
If I’m Going to Write Rules Anyway, Why Train a Model? — What I’ve Learned and Still Don’t Understand About Behavior Cloning
To be clear, I do not think rule-based approaches are unsophisticated. In an environment with explicit rules, discrete actions, and long execution chains, rules are often more stable, easier to debug, and potentially very effective in competition.

But for me personally, if the final answer is to hard-code when to plant, when to expand, when to trade, and what to do in every recognizable situation, the competition becomes much less interesting. It starts to feel like I am maintaining an ever-growing script rather than training an agent that can form judgments from experience.

What I really want to find out is whether a model can learn something from replays that I did not explicitly write down. Can it build its own state representation, understand tradeoffs between resources, make decisions in situations that are similar but not identical, and occasionally produce a choice I did not anticipate but that makes sense in hindsight?

That is why I think behavior cloning is worth exploring and why the model is worth training. It is not because I have already proved that BC is stronger than rules. It is because watching behavior emerge from data is the part of this kind of competition that interests me most.

Why Start with Behavior Cloning?
For me, BC is a starting point, not an endpoint.

The decision horizon in this environment is long, and starting reinforcement learning from scratch would require an enormous amount of exploration. Public replays at least provide a body of real behavior from which a model can learn basic action grammar, state representations, and common tradeoffs. Instead of discovering everything through trial and error, it can begin with a prior for how competent play usually looks.

I do not expect the model to remain an imitator forever. The route I would prefer is to use BC to place the model inside the decision loop, then let it encounter the states created by its own actions, learn how to recover, compare alternatives, and gradually become capable of more than imitation alone.

Then the Contradiction Appeared
Asking the model to decide every primitive action puts too much burden on it.

It must reason about strategy while simultaneously handling scheduling, routing, legality, resource conflicts, deadlines, and recovery from failure. Many consecutive steps contain no new information, yet the model is asked to rethink the whole problem every time. One small error can move the agent away from the replay distribution, after which errors compound across the remaining horizon.

But assigning all of those problems to rules creates the opposite issue: rules can easily cross the boundary from “ensuring correct execution” into making strategic decisions on the model’s behalf.

If rules already determine what to plant, what to buy, how many workers to hire, and when to sell, the model may still be running but only nodding within a very narrow corridor. At that point it has almost no causal influence over the final behavior, and training it becomes largely ceremonial.

I do not want the model to be a brain that has to rediscover how to move its legs at every step. But I also do not want rules to choose the destination and leave the model only to confirm it.

What I Actually Learned Across Several Rounds of BC
Looking back, this has not been a straight line in which the model became larger, the metrics became higher, and the results automatically improved. Almost every round solved one problem from the previous round while revealing a deeper one.

1. Offline Fitting and Free-Running Are Completely Different Problems
The earliest multi-head model already learned nontrivial behavior: unit-operation accuracy reached 43.12%, compared with 15.08% for an always-PASS baseline. But market accuracy reached 94.06% while an always-STOP baseline already achieved 91.06%. That was my first warning that aggregate accuracy can be dominated by inaction.

A later model achieved almost 100% offline unit accuracy and active-market accuracy. It looked as if it had nearly mastered the replays. But once teacher forcing was removed and the model had to run continuously in the official environment, it chose PASS for the entire game and returned to the initial cash balance. The investigation showed that target information from validation was flowing back into the prediction through an intermediate representation. The offline score was measuring the model’s ability to answer questions with the answer key still open.

That failure changed every promotion gate that followed. A checkpoint cannot advance on teacher-forced validation alone; it must enter free-running evaluation early. Default actions, exception fallbacks, and missing inputs must all be recorded explicitly so that the program cannot quietly collapse into PASS.

2. What the Model Predicts Matters More Than Adding More Layers
The first interface asked the model to freely combine an operation, item, and target inside fixed slots. It was easy to obtain actions for which every local classification looked plausible, even though the combined action did not apply to the current state. I gradually moved the interface to object-level Options and then to semantically complete candidate task chains generated from the current state, leaving the model responsible only for ranking them.

That change produced a more meaningful gain than simply increasing network depth. Object-level Options learned useful kinds and pointers. The dynamic-candidate version reached 99.20% candidate AP and 99.00% F1 on held-out data, with zero parent-dependency violations after projection. More importantly, it was the first version to complete the full chain of selection, scheduling, execution, harvesting, storage, and selling across 720 steps. In ten basic closed-loop games, average final cash was about 25.6k; all 3,756 Options completed, with zero deadline misses and zero compiler fallbacks.

That still did not establish competitive strength. But it proved something important: a model can meaningfully influence a complete economic chain without learning grid movement or action legality.

3. Executable Does Not Mean Worth Executing
System reliability improved once legality, cash, inventory, routing, and task dependencies moved into an exact execution layer. After removing preset strategic routes and asking the model to choose directly among Capital, Market, and Unit candidates, another basic closed-loop evaluation reached about 34.2k average final cash, with a 99.96% Option-completion rate and zero compiler fallbacks.

Yet that model never expanded its land. A later version added cross-day maintenance budgets, urgent WATER and FEED obligations, a worker floor, and persistent recovery debt. It still averaged about 34.0k in the basic closed loop, and urgent WATER, urgent FEED, and same-day WATER for new crops all reached 100%. But it still did not expand. A deeper audit showed that some of the missing expansion was not caused by a lack of model intent: old runtime gates were continuing to reject the model’s decisions afterward.

This led me to a more precise conclusion than “fewer rules are better.” The execution layer may prove that a proposal is feasible, but the entire causal path from model output to official action must be audited. If the model clearly changes its preference while the resulting actions remain unchanged, the rules may have crossed from safety constraints into becoming a second policy.

4. Long-Horizon Management Cannot Be Assembled from Independent Heads
The next change moved from independently scoring daily candidates to hierarchical economic BC. A low-frequency Season Portfolio represented target land, production structure, product pipelines, capacity, liquidity, and risk. Daily Production and Market decisions were conditioned on it, while the model also learned belief, value, and KEEP/PATCH/REBUILD decisions.

Offline validation remained strong: Season land, update, and capacity accuracy reached 99.84%, 99.36%, and 97.36%, respectively, while Production AP reached 98.76%. The training and deployment pipeline also finally guaranteed that future labels, teacher actions, opponent-private state, primitive actions, and legality fields were absent from the forward pass.

But stricter free-running diagnosis showed that the problem had moved from “illegal actions” to “an incomplete long-horizon economic loop.” In some evaluations, only about half of the Options completed, and substantial value was still lost between production, harvesting, storage, and conversion into cash. If expansion, financing, hiring, activation of new land, and later sales are produced by independent heads on the same day, they can easily become disconnected during execution.

I now believe that high-level decisions need persistent commitments, not merely more output heads. An expansion decision should carry its financing, activation workforce, production tasks, and sell-through plan together, and it should persist until completion, explicit failure, or deliberate cancellation by the model.

5. The Latest Round Showed How Easily Rare Strategic Events Can Fool Accuracy
The latest retraining round strengthened the near-term land-capacity target. The training run itself was complete and auditable: 50,000 optimizer steps, 99.84% Land accuracy, 98.73% Production AP, and 80.31% Market-item accuracy. Looking only at those numbers, it would be easy to conclude that the model had learned when to expand.

But across 300 genuine day-start branches, the model itself rejected the next land purchase 187 times, the exact same-step financing check failed 100 times, and only seven expansions were ultimately confirmed. Average final cash across ten basic closed-loop games was only 2,671, substantially below several intermediate versions. The 99.84% Land accuracy was driven mainly by the majority class—keeping the current land count—and said almost nothing about whether the rare, strategically important expansion states were handled correctly.

The latest replay audit exposed two related failures. Expansion intent did not reliably become a persistent commitment linking financing → buy land → activate workforce → produce on new land. Near the end of the game, the agent also continued planting while leaving harvestable output and inventory behind. The next iteration therefore needs event-level recall, confusion matrices, and model-to-action conversion rates, as well as explicit Expansion Commitments and a Terminal Portfolio.

6. The Training Infrastructure Became a Real Result Too
After several iterations, the data and validation process is no longer an untraceable collection of Notebook state. I can now freeze and audit 425 replay shards, isolate training and validation submissions, align current state with candidate, belief, and value labels, distinguish requested orders from actually committed trades, and verify checkpoint steps, hashes, forward contracts, and genuine free-running outcomes.

That may not sound like model capability, but it matters. Only when the training pipeline is trustworthy can I tell whether a failure comes from representation, labels, decision granularity, or the execution boundary, rather than leakage, silent fallback, or a training–deployment contract mismatch.

So the biggest result is not any single peak metric. The question itself has changed. I started by asking, “Can the model imitate actions?” Now I am asking, “Can the model form a coherent, persistent economic intent that genuinely affects the outcome while operating inside exact constraints?”

The Boundary I Want to Try Next
I currently prefer a system in which the model selects high-level Options and a deterministic execution layer turns those Options into actions:

The model owns the tradeoffs: which goal is worth pursuing now, how candidate plans should be ranked, how much budget to commit, how much risk to accept, and when the current plan should be abandoned.
The executor guarantees correctness: whether an action is legal, which task dependencies must be satisfied, how routing and logistics should work, whether resources conflict, whether hard deadlines can be met, and how to fail safely.
The model does not need to replan at every primitive step. Once an Option begins, the executor can preserve the task. Control returns to the model only when the Option completes, execution becomes blocked, important information changes, or a risk boundary is crossed.



The critical condition is that the execution layer may eliminate illegal or clearly infeasible plans, but it must not secretly decide which feasible plan is “better.” If a rule changes the preference ordering between feasible plans, it is probably no longer an execution constraint; it is making strategy.

For the current model, the Option in this diagram cannot be an isolated class either. “Expand,” for example, should be a multi-day commitment package in which land, financing, the workers needed to activate it, production on the new land, and eventual monetization belong to the same objective. Near the end of the game, the model should switch to an explicit Terminal Portfolio, stop investments that cannot pay back in time, and convert mature output and inventory into final cash.

I also want to test whether the model truly matters in a very direct way: freeze the executor, then replace or remove the model. If replacing it with a constant output barely changes the agent’s behavior or results, the strategy is really hidden in the rules and the model is only decoration.

What I Still Do Not Know
The largest open questions for me are:

How long should a high-level Option persist? Should decisions be daily, event-driven, or use different timescales for different tasks?
How can Option and commitment labels be recovered from primitive-action replays without allowing hand-written rules to predefine everything the model is allowed to learn?
How can rare events such as expansion, strategic switching, and terminal liquidation be emphasized without turning the model into a fixed route?
How can the model learn what to do after a mistake instead of only imitating successful trajectories?
How should outputs from multiple heads become a joint cross-day commitment that cannot be silently dropped but can still be deliberately cancelled by the model?
How complex can the executor become before it sidelines the model? Beyond accuracy and final score, how can the model’s true causal influence over behavior be measured?
My uncertainty is therefore not about whether rules are needed. Legality, safety boundaries, and reliable execution obviously require rules. The difficult question is: how do I preserve enough structure for the agent to act reliably while leaving enough important choices to the model that training it still means something?

This may not be the easiest path to winning, but for me it is the more interesting one.

If you have worked on a similar long-horizon agent, I would love to know: where would you draw the boundary between the model and the rules?


4

2
8 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
redblackbst
Posted 22 days ago

· 29th in this Competition

RL is fun only if you have 4 x 5090s, which I don't 🤷

BC/RL is hard (if possible) for this competition, the reason is multi-fold:

The engine/environment is complex, components couple and long horizon, so try recurrent models for starters.
Sample scarcity and multimodality. The daily episodes provided are simply not enough for meaningful BC, and frequent engine patches makes this problem worse; hopefully this will ease as competition progress.
I've had partial success by using executable scripted agent as BC source, and the result is locally strong: it can beat its BC parent and almost all of my locally available agents. But RL from there is more like fine-tuning rather than effective exploring, it just never escape the initial policy basin, meaning that it still scores 0% against one opponent that it can never beat in the beginning while winrate against broad panel continues raising, and curriculum/PFSP etc won't help much. I have several hypothesis and am still trying.


Reply

React
Zhenyu Zhang
Topic Author
Posted 22 days ago

· 651st in this Competition

Really glad you shared these results. I’m thinking maybe I could try behavior-cloning my own heuristics as well. Unfortunately, I don’t have 4×5090s either 😭


Reply

React
Steve421471
Posted 22 days ago

· 482nd in this Competition

I am seeing similar results: BC+RL can beat the training script most of the time but that doesn't translate to dynamic gameplay against dissimilar opponents. I am not able to teach the RL how to beat an opponent the script cannot beat either, there is no success to teach.


Reply

React
Nguyễn Mạnh
Posted 19 days ago

· 2107th in this Competition

I dont think RL easy cause I have GH200 and it extremely hard you not only to have computational power but I have to design effective dense reward which help model converge fast enough otherwise u end up with medium achievement like writing base rules heuristic ! I tested and fail at this not because I dont have GPU but lacking of experience to set up relevant reward Anyway I dont like cloning I used it to compete with my designed model to see how effective it is rather than pushing public and wait! But its really expensive to try this way i dont think people should do it cause my purpose is tryin to learn


Reply

React
Jake
Posted 19 days ago

· 3335th in this Competition

My experience trying to incorporate RL has been similar. You summed it up nicely with "how do I preserve enough structure for the agent to act reliably while leaving enough important choices to the model that training it still means something". So far, I'm mostly developing a rule based agent but I'm trying to be very disciplined about isolating the strategic decisions (ex: what to plant and when) in a way that they can be replaced by a learned RL function later. The recently completed Pokemon competition (which it looks like many on this thread was in, hello by the way) already did this nicely. The Pokemon environment already had everything distilled down to these are your valid actions, which fit with various types of RL very nicely with little abstraction needed. I think in Kaggriculture we need to essentially develop the same thing. So the winner might be who can jointy develop both the best A) rule based abstraction layer to automate things like routing decisions, B) RL for strategic decisions.


Reply

1
Zejun_
Posted 22 days ago

· 651st in this Competition

Very cool post and thoughts!

You might not think so—but I think the object and setup of BC are undoubtedly challenging. To some extent, I believe BC will never surpass its "parents" and thus cannot reach the top of the rankings. Yet seeing you in the top ten surprised me. Facing BC/RL problem, I've encountered many difficulties:

I've failed repeatedly in setting rewards for so sparse behaviors during training.
How to organize BC's input data and utilize them effectively in a localized manner.
How to map opponents' thought processes from replays to ensure effective imitation.
I'm very interested in whether BC and RL can dominate the rankings.


Reply

React
Zhenyu Zhang
Topic Author
Posted 22 days ago

· 651st in this Competition

I totally agree with you. What's been bugging me is that my BC model is still just a 'little kid.' When battling against the public notebooks, it can only score around 50k (compared to the public notebooks' 140k).

So, I tried designing a heuristic agent (mostly generated by Codex) as a workaround. My hope is that by making it into the top ten, I can draw more attention to the actual training of BC models.


Reply

React
crazy achiever
Posted 22 days ago

· 3628th in this Competition

So your top leaderboard model is heuristic agent?


Reply

React
Zhenyu Zhang
Topic Author
Posted 22 days ago

· 651st in this Competition

YES！heuristic agent


Reply

React
This comment has been deleted.

shanzhong8
Posted 22 days ago

· 1436th in this Competition

My BC is currently at 80k score; still a long way to improve, but I think you got the right point here: the rules is safe guard, and the BC or RL can mimic the decision instead.


Reply

1
Zejun_
Posted 22 days ago

· 651st in this Competition

Hi—I’ve been trying to make RL smarter in game, but my 22th submission days ago was purely heuristic. Switching to RL + gating dropped me to ~140th place. I have few ideas—especially on switching between stable routes and dynamic decisions—but RL performance has been poor. BC might be a better starting point. I'd be glad to collaborate if there's an chance.


Reply

React
Zhenyu Zhang
Topic Author
Posted 22 days ago

· 651st in this Competition

Surprising results. Reaching 140th place with Rl model is a result I wouldn't have dared to imagine.


Reply

React
Zejun_
Posted 22 days ago

· 651st in this Competition

NOT full RL, just let it be a gating part, still about 80% was heuristic method.


Reply

React
Zhenyu Zhang
Topic Author
Posted 20 days ago

· 651st in this Competition

I'm also trying the approach you mentioned.Maybe we can work together😉.


Reply


Hao Yang · 2958th in this Competition · Posted 15 days ago
Why is there such a strict bonus point system?
I clearly noticed that in the teams on the gold medal leaderboard, they had already reached around 1800points by the 13th round, without losing any matches before that. In my first 13 rounds, I only lost once in the 8th round, but after that, the points for wins dropped significantly. By the 13th round, my score was just over 1300, and in the following rounds, it quickly approached the minimum scoring line. Is this really fair?


React
4 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Navneet
Posted 14 days ago

Thank you for the strict bonus point system info @datasutudent


Reply

React
qihuaz
Posted 15 days ago

· 2782nd in this Competition

TLDR, the matching is adaptive.

the strength of opponents you face is adaptive. once you lost in the 8th round, you got assigned to weaker opponents. So the 9th-13th opponents you faces are much weaker than the 9th-13th opponents that gold medal teams faced. But it will eventually converge if you keep winning, justa take a bit of time.


Reply

React
Civitasmass
Posted 15 days ago

· 246th in this Competition

In my experience, the rating converges in about 12 hours anyway, so bad matchmaking early on shouldn't really matter

unless you're super unlucky and keep matching against other elite agents climbing the ranks.


Reply

1
Civitasmass
Posted 15 days ago

· 246th in this Competition

Of course, lose a game significantly adds to the convergence time.


Reply

React
Hao Yang
Topic Author
Posted 15 days ago

· 2958th in this Competition

Okay, but I still have a question. Will the scoring mechanism after the final submission of this competition still be affected by wins and losses in the earlier matches? If you lost some matches in the first 20 games or so, I feel like it would be pretty hard to turn things around, even if you win quite a few games afterwards.


Reply

React
Civitasmass
Posted 15 days ago

· 246th in this Competition

after the deadline, everyone reset back to 600 and matches start all over again.


Picu · 7166th in this Competition · Posted 17 days ago
Reverse engineering the seed
I let an AI do the math as I didnt want to get into the weeds(badumm tss because weed spawing gives the seeds away) of it, but according to the chatbot you can probably reverse engineer seeding so that you can predict shop unlocks, which seems non-intentional. Will the seed RNG be different than what is currently there and is this reverse-enginerring allowed


React
4 Comments
1 appreciation comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
qihuaz
Posted 17 days ago

· 2782nd in this Competition

if i recall correctly, the seed RNG also depends on opponent's actions, so you can't predict the SHOP unlocks?


Reply

React
Praveen
Posted 17 days ago

· 83rd in this Competition

how many seeds are u gonna reverse engineer? 1k? 100k? 1million?


Reply

React
Jack
Posted 17 days ago

· 1931st in this Competition

I think you should have the chatbot help you do this and see how it turns out


Reply

5

Appreciation (1)
Mohammad Javad Dianat
Posted 17 days ago

· 4051st in this Competition

Great insights, thanks for sharing!


Jerry Caligiure · Posted 17 days ago
Quickstart isn't working
When I run

from kaggle_environments import make

def my_agent(obs):
    # Buy one wheat seed on the very first turn, then PASS forever after.
    if obs.get("step", 0) == 0:
        return {"farmer": ["PASS"], "market": [["BUY_SEED", "WHEAT", 1]]}
    return {"farmer": ["PASS"], "market": []}

env = make("kaggriculture", configuration={"episodeSteps": 200})
env.run([my_agent, "random"])
print(env.render(mode="human"))
from the quickstart in a notebook, either on here or locally, I get NONE. If I try to render it as html it's just an empty black frame. Anyone else run into this issue or something similar? Any advice would be great!


Mohammad Javad Dianat · 4051st in this Competition · Posted 17 days ago
[Baseline & Strategy] Reactive Agent Architecture & Crop ROI Breakdown
Hello Kagglers! 🌾

I've shared an end-to-end baseline and strategic walkthrough for the Kaggriculture simulation: 👉 Kaggriculture: Reactive Agent Strategy & EDA

💡 Core Strategic Highlights:
Zero-Weed Irrigation Priority: Ensuring all unwatered crops are prioritized before hour 20 to eliminate plant decay.
Fibonacci Farm Hands Economy: Utilizing low-cost micro-hires (2 hands/day for just $2 total) to triple operational throughput.
Market Supply Arbitrage: Buffering harvest in the shed during supply gluts and selling when local prices rebound above floor thresholds.
Wheat vs. Melon ROI Balancing: Maintaining steady wheat reserves for animal sustenance while scaling high-yield cash crops.
Check out the interactive Plotly graphs and baseline code in the notebook. Looking forward to your thoughts, feedback, and discussion on simulation dynamics!

Good luck to all teams! 🚀


SeaGoat · 3346th in this Competition · Posted 25 days ago
Experiences on LLM Usage
Any one having success using LLM's. ? Any particular model. I have tried using Qwen 3.8 & Opus. I cannot get my scores above 850. I am providing the instructions and asking it to build. Tried to also prompt it asking RL (PPO).


3
9 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Michael Timbs
Posted 24 days ago

· 1378th in this Competition

If you want to use an LLM this paper should give you some ideas. Get it to build small generators that compose instead of trying to sequence a full 720 moves https://surya.website/rling-qwen-to-paint-with-code


Reply

3
VynoDePal
Posted 25 days ago

· 1986th in this Competition

Personally, I’ve tested a lot of models, and it cost me a fortune. I started with Claude, and I got the worst results with it. Claude is great when it comes to coding, but regarding critical thinking and scientific reasoning—all that stuff—it’s terrible. Really terrible. After Claude, I tried a Chinese model—Kimi K3, for instance—by signing up for a basic subscription, but I quickly hit its limits. I couldn't form a definitive opinion on it, so I moved on. Next, I switched to Google’s models—Gemini 3.7 Flash, then a system involving abstraction and teams, and finally Gemini 3.1 Pro. It did a pretty good job, especially since I was focusing more on RL (Reinforcement Learning). It was a bit challenging to implement, but I really liked the experience and the feedback Gemini provided during testing. So, in terms of critical reasoning, Gemini models are the best, though the actual application side isn't quite there yet. Right now, I’m primarily using OpenAI’s model—specifically GPT-5.6 Solo with Codex. For the moment, it’s by far the best option I have for critical thinking, whether it’s verifying my hypotheses in real-time or challenging my assumptions. It does a lot of testing. In terms of current results, GPT-5.6 Solo is far superior to anything else out there.


Reply

React
SeaGoat
Topic Author
Posted 25 days ago

· 3346th in this Competition

Thank you. Let me try Gemini


Reply

React
Artem Voronov
Posted 25 days ago

· 3237th in this Competition

It doesn't matter which model you use. They all lack strategic and critical thinking. Even frontier models can become trapped in logical loops and burn through millions of tokens without achieving anything.

I find two simple tools helpful:

a register of hypotheses
a feedback loop.
Even a weak model can produce a decent result with these.


Reply

React
SeaGoat
Topic Author
Posted 24 days ago

· 3346th in this Competition

Thank you. Can you please elaborte on a register of hypotheses? Is it a Mark down file of all the hypothesis that has been tried


Reply

React
Artem Voronov
Posted 24 days ago

· 3237th in this Competition

I keep a hypothesis registry in Markdown, with a JSON version for automated processing. Each hypothesis has an ID, a clear claim, a status, the strongest available evidence, the resulting decision, and a condition for reopening it. For example:

ID	Hypothesis	Status	Evidence
H001	Exact engine parity is required	CONFIRMED	Replay parity checks
The same entry in JSON looks like this:

{
  "id": "H001",
  "hypothesis": "Exact engine parity is required",
  "status": "CONFIRMED",
  "result": "Verified through replay parity checks"
}
The Markdown gives it the reasoning and context behind previous decisions, while JSON lets it quickly filter and process the hypotheses. An agent can see what has already failed, respect the conditions for reopening an idea, identify the current research branch, and suggest the next experiment based on accumulated evidence instead of starting from scratch each session.


Reply

2
qihuaz
Posted 25 days ago

· 2782nd in this Competition

I tried DeepSeek v4 Flash first and instantly noticed it is far from being usable for this compeition.

Then Opus 4.8, it gave me a working agent, but it gets frustrating when I tried to improve it. When I gave it an strategy, it would implememt a buggy one, then revert (even when I explicitly told it not to) and call my strategy "theoratically sound but don't work in practice", or invent some ungrounded theory to "prove my idea does not work". I had to argue and explain to it before it admited "I invented at least three ungounded theory in this session." Just the worst experience with Opus so far for me.

Switching to Fable helped a lot, just do exactly what I want it to do correctly.


Reply

React
SeaGoat
Topic Author
Posted 25 days ago

· 3346th in this Competition

Thank you. Will also try Fable and Grok


Reply

React
VijaiKurianMathew
Posted 18 days ago

· 3053rd in this Competition

Getting Past 850: Harness First, Then One Rule at a Time
Think of the LLM like a talented junior hire — great at drafting, but needs a manager and a scorecard. Asking it to "build the whole farm in one go" is like asking for a 30-day business plan with no feedback. We got unstuck by flipping the order.

1. Build the Harness Before Any Rules
Like a test track before you tune the car.

The harness is your private ladder. It runs the same game the competition does — same 30-day season, same market — but locally and fast. It has one job: tell you if a change helped or hurt, immediately.

Smoke test: agent vs random in one episode — does it run without crashing?
Benchmark: vs starter/random/pass on both seats + historical champions — real win-rate, not one lucky seed
Safety gates: order limits, state resets, determinism — every LLM edit is checked before you trust it
Logbook: each idea lives in its own file → idea → result → keep or drop
Workplace analogy: It's your QA lab and dashboard. Without it, you're flying blind. With it, every pull request has a number.

2. One Rule at a Time, Ladder as Feedback
Like A/B testing one feature, not a full redesign.

We never ask the model for a full 720-step rewrite. We add one small, testable rule — e.g., one crop decision or one animal routine or one market behavior — then measure.

Propose one focused change in isolation
Run the harness (both seats, 10+ seeds) — did it beat the current best?
If yes → promote to main + submit so the ladder confirms it. If no → drop it and try the next
Repeat — 850 → 1000s → higher is 10–20 such cycles, not one prompt
Workplace analogy: It's feature-flag A/B testing. You don't ship ten features at once and guess which one worked.

Takeaway: Put the harness (your scorecard) in place first, then let the LLM help you craft and test one focused rule at a time with the harness + ladder as the loop. Model choice matters less than that loop.

Harness (benchmark + gates)
        |
        v
Propose ONE small rule
        |
        v
Harness test (both seats, starter/random/pass)
       / \
  Wins?   No win
   /        \
Promote → Ladder   Reject → log → next rule
   \        /
    -> back to Propose

Reply

React
SeaGoat
Topic Author
Posted 24 days ago

· 3346th in this Competition

I got the initial code planned and developed by Fable and ran the rest with Opus. Got a significant bump (1400+)


destbreso · 1027th in this Competition · Posted 20 days ago
X-ray your agent, or what one submission id gives away
Over the past weeks I have been reading this competition mostly through replays: stripe textures, kinship between submissions, macro economics, rating convergence. Those tools lived in scripts on my machine, and I have now packaged some of them into one notebook that anyone can fork and point at any submission: X-ray your agent.

The premise is simple: the leaderboard gives your agent one number, and its replays give away nearly everything else. One run answers, in order:

How is it doing? The win-loss-tie ledger and the margin of every episode, in play order.
What does it actually play? The stripe texture: one row per episode, one column per turn, green where it plays its own modal action, amber where only the market differs, navy where the plan itself differs.
What kind of agent is it? Pure replay, script with repairs, shop router, or live policy, classified globally and within each world, because a router looks adaptive globally while playing a fixed script inside every world.
Who has it been playing? The kinship spectrum: which opponents run its exact lineage, which are siblings, and which opponents cluster into genetic families.
What did its economy do? Land timing, herd, care actions, endgame hygiene and money by day, each next to the measured shape of the current leader.
Can the rating be quoted yet? Drift per episode, sign flips, and a settle verdict with its threshold stated, plus how long to wait before reading again.
Two defaults worth knowing:

It hunts the king. With no id set, the notebook resolves whoever is number one right now, at run time, by climbing the live ladder: from any submission, hop to the best-rated opponent in its recent episodes, repeat until nobody nearby rates higher. No leaderboard endpoint, no dataset, no staleness. It is scheduled daily, so the public page is always the reigning number one's x-ray as of today, never a stale snapshot.

Forking it is one edit. Put your own submission id in the first code cell where it says SUBMISSION_ID = "KING" and run. No API token and no attached data: the episode list comes from the competition's public episode service and the replays from the public CDN, the same route georgymamarin's episodes dataset crawls nightly, credit to his scraper for the endpoint. The fork needs the Internet toggle on. A run takes a few minutes at the default of the newest 40 episodes.

Some of what the first runs turned up, to give a flavor: my own agent turned out to have four opponents running its exact lineage, three of them action-identical on all 719 turns, and 19 of its last 40 opponents collapse into one genetic family. Today's king is the only genuinely live policy the instrument has read so far: its plan diverges from turn 34, before the first shop draw, in all eight worlds it played, so no mirror of it can exist.

And the part I am most curious about: I would love to see what your submissions look like. If you run it on yours, three things are especially interesting: how green your texture is, whether the kinship section finds family you did not know you had, and whether your rating has actually settled by the drift verdict. Feel free to post a panel or two here, I will happily trade readings.

stripe texture panelThe texture of one submission: every episode it played, turn by turn. Green is its own plan, navy is deviation. You can see at a glance whether an agent is one script, a family of scripts, or something alive.

macro x-ray charts 1

macro x-ray charts 2 The macro section: money by day and the economic shape (land timing, herd, care, endgame) against the leader's measured profile. This is where I found my own agent stranding sixty times less money at the bell than the leader tolerates, and also where the real gaps show.

rating convergence chartThe convergence section: rating by episode with a drift verdict. The unit is the episode, never the hour, because the ladder pays in batches. A rating still moving 1.3 points a game is not yet a number, and the notebook says so instead of letting you quote it.


Michael Timbs · 1380th in this Competition · Posted 23 days ago
Leaderboard is by nature obsolete at all times
If you are like me and pay attention to basically every episode played every day from the top 100 teams, you'll notice that the submissions currently in the top 10 are basically obsolete by the time they get there (even my own). Due to the nature of ELO aggregation and matchup rates it takes several days to climb to the top of the leaderboard. It doesn't matter how much stronger your new submission is than your old one - it won't overtake it for several days.

Older submissions also play fewer games which mean they fall off the leaderboard at a slow rate.

I fingerprint every episode played and can trace back moves to specific teams and submission lineages. So i can tell when my aug 26 opening was cloned by 15 teams within the first 24 hours. I can tell how long it takes strategies to be copied (often directly).

This is a nature of match up cadence but also the fact that nearly everyone is still playing static policies at the moment that only have marginal reaction to town evolution (shop ordering) and opponent play. It means most submissions given the same game and the same seed will play the same turns regardless of what the opponent does, and those that do react on opponent do so in very primitive ways.

My 2500 ELO submission is stronger than my 2860 one but also may never climb to 2860 itself because the field its playing against on the way up is also stronger. My current model is stronger again but i probably wont submit it for a few more days and then it will take another 3+ days to climb.

Basically don't get fooled into thinking the current top 10 submissions are actually the 10 best submissions in the field at the moment.


React
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Yan Zhou
Posted 23 days ago

· 1053rd in this Competition

I haven’t been watching the leaderboard continuously, but I did notice something today that seems a bit different from what you described. When I checked, the current #1 submission was only about 7 hours old, which would mean it took less than 7 hours to climb all the way to the top.

So at least in that case, it seems like a strong enough submission can move up the leaderboard pretty quickly.


Reply

React
Michael Timbs
Topic Author
Posted 23 days ago

· 1380th in this Competition

That’s the age of the teams most recent submission. 2 are actively scored at any time. It’s not the age of the submission with the leaderboard score


Reply

React
Yan Zhou
Posted 23 days ago

· 1053rd in this Competition

Yeah, I noticed that too. His two submissions were only about an hour apart, so in this case it doesn’t look like the leaderboard score was coming from a submission that was several days old. Just thought it was an interesting data point.


Reply

React
Michael Timbs
Topic Author
Posted 23 days ago

· 1380th in this Competition

you are right. Seems like it might be possible with a perfect opening run in the games that move ELO a lot and run at a good pace. an early loss due to a bad matchup or town evolution or weed placement makes it basically impossible.

So good news is that an undefeated run can get there in about 8hours. Interesting. Both my current submissions had bugs in them that lose in some very rare circumstances that caused early losses which delayed the climb significantly


Reply

2
Omkar Kadam
Posted 23 days ago

· 704th in this Competition

I checked top 1 submission in the morning within 4 hours his submission was on top 1, and other was having 1 hour gap between other submission


Reply

React
Michael Timbs
Topic Author
Posted 23 days ago

· 1380th in this Competition

but point stands within a day of submitting a fixed policy it is copied. Only truly adaptive policies stand a chance of not being cloned almost immediately


Reply

React
Omkar Kadam
Posted 23 days ago

· 704th in this Competition

i have an question like yesterday i submitted a submission which stabilized around 2500 but when today i uploaded the same zip it only got till 1954 and does that means other participants or meta has evolved ? also should i upload it again or consider it as not useful ?


Reply

React
Michael Timbs
Topic Author
Posted 23 days ago

· 1380th in this Competition

The field has likely evolved and learned from your first submission or just got stronger over all. Dont worry too much about leaderboard position at the moment. Just look at your losing games and improve based on that and download the top games each day and learn from those. There is no value in re-submitting the same solution because even if it climbs higher it doesnt mean anything. Everyone goes back to 600 at competition close and plays from a fresh start to get the final leaderboard

stpete_ishii · 3687th in this Competition · Posted a month ago
(Resolved) obs["step"] is missing for seat 1 in env.step()/env.steps -- not a live env.run() match issue
I was testing a downloaded agent locally by running it against a copy of itself (same file, both seats) in a small local harness, and noticed player 2 basically never moved — it kept repeating what looked like its turn-0 action, turn after turn, while player 1 played normally. That looked wrong for two copies of the same deterministic agent, so I dug into why.

Turns out it's an environment bug, not a problem with the agent. This also confirms and answers the question raised in "Observation timing" (posted 20 days ago, still unanswered): yes, the missing step field for seat 1 is a real bug, not intentional behavior with day/hour as a substitute clock.

Reproduction (official env.run() only, no custom harness)

from kaggle_environments import make

def probe(obs, config=None): return {"farmer": ["PASS"], "hands": [], "market": []}

env = make("kaggriculture", configuration={"episodeSteps": 10, "seed": 1}, debug=True) env.run([probe, probe])

for i, s in enumerate(env.steps): print(i, "seat0 step:", s[0].observation.get("step"), "seat1 step:", s[1].observation.get("step")) Output:

0 seat0 step: 0 seat1 step: None 1 seat0 step: 1 seat1 step: None 2 seat0 step: 2 seat1 step: None … 9 seat0 step: 9 seat1 step: None seat1's step is None on every single turn of the season, not just the first one. kaggle_environments==1.32.7 (the current pip install -U kaggle-environments version).

Root cause kaggle_environments/core.py only stamps step onto state[0].observation:

new_state[0].observation.step = 0 if self.done else len(self.steps) kaggriculture.py's interpreter propagates day, hour, farms, market, and town from the seat-0 observation to every other seat each turn, but step is missing from that list — so seat 1 never receives it.

Impact Any agent that reads obs["step"] — including the Quick Start snippet in the competition rules themselves (if obs.get("step", 0) == 0: …) — will always see step == 0 whenever it's placed in seat 1, because obs.get("step", 0) silently falls back to 0 on None. In practice this means "turn-0-only" setup logic re-fires every turn, and any step-indexed schedule/plan just replays its turn-0 action forever in that seat. Since ladder matchmaking presumably alternates seats across episodes, this quietly handicaps any submission that keys off step in roughly half its games — through no fault of the strategy itself.

day and hour are correctly synced to both seats every turn, so obs["day"] * turnsPerDay + obs["hour"] is a reliable stand-in for step in the meantime.

Would appreciate a confirmation from the organizers on whether this is being patched, since it silently affects anyone following the documented obs["step"] pattern.


React
5 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
destbreso
Posted 21 days ago

· 1027th in this Competition

Late to this one, but it seems a good occasion to add two data points from the replay side, since the thread settled the live side so cleanly (nice probe, @Yizuki, and respect for the follow-up verification, @stpeteishii).

Independent confirmation of the serialization half: across every replay I have pulled for analysis, 348 episodes between my own games and top-team games, the stored seat-1 observation lacks step on 719 of 719 turns of every single episode. So any tooling that feeds recorded observations back into an agent meets this on every seat-1 tape, not occasionally.

The magnitude when a replay harness forgets to restore it: in my replay-driven evaluator, a step-indexed agent fed raw seat-1 observations banks its starting 3,000 and never acts. The flip side is just as clean: once the turn is derived as obs["day"] * 24 + obs["hour"], the same harness reproduces recorded ladder banks to the dollar (8 of 8 on my last check), so the OP's stand-in is not merely a workaround, it is exact.

Which is why I ended up with a stricter version of it as a house rule: never read obs["step"] at all, in the agent or in any tool. Deriving the turn from day and hour makes the same code correct in live env.run() matches, in replay-fed analysis, and in direct env.step() harnesses, so the whole class of mismatch cannot occur. Agreed with the resolution: live matches are fine, the field that bites is the serialized one, and it bites tools more than agents.


Reply

React
Yizuki
Posted 22 days ago

· 708th in this Competition

One important correction: this reproduces an omission in the serialized env.steps state, but not in the observation passed to the running callable.

On kaggle-environments==1.32.7:

seen = [[], []]

def probe(i):
    def agent(obs, config=None):
        seen[i].append(obs.get("step"))
        return {"farmer": ["PASS"], "hands": [], "market": []}
    return agent

env = make("kaggriculture", configuration={"episodeSteps": 10, "seed": 1})
env.run([probe(0), probe(1)])

print(seen)
# [[0,1,2,3,4,5,6,7,8], [0,1,2,3,4,5,6,7,8]]

print([s[1].observation.get("step") for s in env.steps])
# [None, None, ..., None]
So seat 1's stored replay/state omits step, while the actual seat-1 agent call receives the correct value. I also checked a hosted seat-1 replay of a step-indexed agent: restoring the shared step reproduces all 719 submitted actions; feeding the raw serialized observations reproduces only 1/719.

This looks like a replay-serialization/state-recording issue, not a runtime handicap for submitted agents. Directly replaying env.steps[*][1].observation does need the shared step restored.


Reply

React
stpete_ishii
Topic Author
Posted 22 days ago

· 3687th in this Competition

@Yizuki is right, and I owe an apology here, not just a correction.

I stated as fact that this "quietly handicaps any submission that keys off step in roughly half its games" -- a claim about how real competition matches behave -- without ever actually testing what a live env.run()-dispatched agent call receives. I only tested env.step()'s return value and the recorded env.steps, assumed that generalized to real matches, and posted it that way. That was careless, and if anyone reading the original post held off on a step-based design, or spent time on a workaround, for a live-match problem that doesn't actually exist, I'm sorry -- that's on me.

Corrected version, now actually checked against a live env.run() call:

I reproduced it: Agent.act() calls during env.run() do receive the correct, incrementing step for both seats. I dug into why: Environment.__get_shared_state() (in kaggle_environments/core.py) deep-copies each seat's state and then overwrites every field the schema marks "shared": true with seat 0's value, right before the agent callable is invoked. step isn't in kaggriculture.json's own schema at all -- it comes from the framework's base observation schema, which apparently marks it shared -- so it gets this same fix-up.

The catch: __get_shared_state() only runs inside env.run()'s agent-dispatch path. It is not applied to env.step()'s direct return value, nor to the recorded env.steps (and therefore not to a downloaded replay.json either) -- both of those still show step: None for seat 1, exactly as in my original repro.

So, corrected scope:

Submitted agents in real matches: very likely fine. If the ladder runs episodes via env.run() (the documented, standard way), both seats get a correct shared step at the point their agent(obs) is actually called.
Still real, still affects people: anyone driving env.step() directly in a custom harness (I was, for a local multi-agent sandbox), and anyone reconstructing a game from env.steps/replay.json and feeding those observations back into an agent.
Retracting "silently handicaps any submission that keys off step in roughly half its games" in full -- that line shouldn't have been posted the way it was. Thanks again to @Yizuki for checking the part I didn't.


Reply

1
Alex Paul
Posted 23 days ago

· 189th in this Competition

This is a severe bug. This causes my agent to perform very poorly, the organisers should fix it asap!


Reply

React
Omkar Kadam
Posted 23 days ago

· 704th in this Competition

is it confirmed ?


Reply

React


Linda Liu · 2659th in this Competition · Posted 19 days ago
Is replaying action sequences extracted from public episode replays permitted under kaggle competiton Rules 3.14.a?
Hi @bovard I locally generated replay-derived tapes from public episode replays (samples) from public kaggriculture-episodes dataset. In this case, is it still not breach the kaggle competiton Rules 3.14.a? https://www.kaggle.com/competitions/Kaggriculture/rules


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Bovard Doerschuk-Tiberi
Kaggle Staff
Posted 19 days ago

· 9011th in this Competition

Using public replays to train, build, inform your submission is allowed and encouraged.


c0nrad · 94th in this Competition · Posted 19 days ago
Proposal: No new shops at end of month
I'm not a fan of the abundance of replay/tape bots. It'd be nice if the game was structured in a way to promote more dynamic strategies.

One potential solution to (fairly) give non-static bots a leg up is to open up shops only in the first half of the month. Right now the replays heavily emphasize certain crops (even if it's overall not the smartest choice), but sometimes randomly the late shops will consume those crops (more than an average forecasting would suggest). Since it takes 16 days for strawberries to fully harvest, it's too late for the forecast bots to fully take advantage of those those crops if they open up after day 15.

While overall the ELOs should eventually normalize to their proper values, it takes a lot longer with these random losses due to lucky replay bot guesses.


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Yusuke Hayashi
Posted 19 days ago

· 1945th in this Competition

My code: https://www.kaggle.com/code/yhay81/fieldbook-commit-for-three-days

My code involves branching the replay. While your proposal might address full replays, it fails to counter strategies—like mine—that branch right at the very beginning; in fact, I think it actually gives them an advantage. With strategies that rely on branching replays, early-game branching is both easy and highly effective, whereas late-game branching is difficult to execute due to a lack of sufficient replays on the leaderboard. What do you think?


Nguyễn Mạnh · 2112th in this Competition · Posted 20 days ago
Beyond Replay Cloning: What is the True End-Game Strategy for Kaggriculture? (Stuck despite PPO, GA, & Beam Search)
Hi everyone, This is my first time participating in a long-horizon simulation competition like Kaggriculture (720 turns). I’m completely fascinated by the environment, but I’ve hit a massive wall.

It seems the current "meta" on the public leaderboard is heavily dominated by Replay Cloning (extracting exact build orders, static geometries, and demand-aligned heuristics from top players' replays). While this is a smart tactical move to climb the ranks quickly, I want to understand the fundamental engineering and AI strategies that actually generate those top replays in the first place.Here is what I am trying to do and what I have already built:

My GoalI want to build an agent from scratch that can consistently score high (40k+ income/Elo equivalent) without hard-coding another player’s static farm layout or exact build timeline.

What I Have Tried So Far (My Tech Stack & Roadblocks)Heuristic Design & State-Machine: I built a solid rule-based agent (guarding worker alignment, market arbitration, premium-first selling). It works well but easily gets outplayed in the late game when market elasticity drops. It feels too rigid.

Beam Search & Genetic Algorithm (GA): I managed to rewrite the core engine to do some offline batched Beam Search and GA. This successfully found paths yielding 40k+ income in isolated environments. The Roadblock: When transitioning to the online Kaggle server (CPU only, 1-second timeout), I can't run deep Beam Searches. The limited-horizon rollout (K branches for 10-15 steps) often falls into local optima because the game horizon (720 steps) is too long for short-term heuristic evaluation functions to accurately judge late-game ROI (like breeding animals).

Reinforcement Learning (PPO via JAX Vectorization): Roadblock: Despite the massive compute, the PPO agent fails to learn long-term macro strategies. The Mean Return stays near zero, and the max money hovers around 2k-3k, nowhere near the 40k+ found by Beam Search. It seems the sparse reward structure of a 720-step episode is destroying the policy gradient.

The Core Questions for the VeteransFor those of you who are engineering these top-tier agents from the ground up (not just augmenting public replays):
Online vs. Offline Compute: Are you heavily relying on offline JAX/GPU vectorization to find the global optimum (via MCTS/AlphaZero or Massive PPO) and then distilling that into a lightweight neural net or fixed strategy for the Kaggle CPU submission?

RL Reward Shaping: If you are using PPO/RL, how do you handle the extreme reward delay? Do you use dense intermediate rewards (e.g., +points for placing seeds, maintaining liquidity), or do you use Behavioral Cloning from your Beam Search outputs to warm-start the PPO agent?

The True Meta: Is pure RL a trap for this specific competition? Is the "holy grail" actually a highly optimized C++ engine running heavily pruned Minimax/Beam Search directly on the Kaggle servers within the 1-second limit?I would deeply appreciate any insights, architectural advice, or pointers on where I should focus my compute next. Thank you for reading!

Optimization
Reinforcement Learning
Simulations

React
6 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Cho Royou
Posted 20 days ago

· 1144th in this Competition

At least from watching the replays, you can tell that quite a few top players are using RL-based approaches. I was really impressed by all of their setups and positioning.

I’d guess this is also the kind of approach with the highest ceiling.


Reply

React
Nguyễn Mạnh
Topic Author
Posted 20 days ago

· 2112th in this Competition

Hi ! How do you know if they using cloning or RL? I personally have no clue at all? Thank you so much


Reply

React
Steve421471
Posted 20 days ago

· 479th in this Competition

I don't think too many people are going to be forthcoming about what's working for them but I'll say this: I see strong evidence that at least one of the top players has submitted an agent that was built using RL.

I will say that I've tried a lot of things and hit a lot of dead-ends. Some of those dead-ends are real and some of them might not be, but I can't get the AI to build them right (I don't think it can) and I don't have time to do it myself.


Reply

1
This comment has been deleted.

Yohanes Alfredo
Posted 20 days ago

· 2903rd in this Competition

Unfortunately, due to how this competition is structured, I am afraid making a top tier RL-based agent within the time constraint, is going to be very tough challenge. Would love to be proven otherwise. Not to say it's impossible, but the time constraint is clearly a tough hurdle.


Reply

React
Belati Jagad Bintang Syuhada
Posted 20 days ago

· 2625th in this Competition

So far no known behavior cloning approach in the top leaderboards yet. I suspect that its due to the complexity of the action (move each workers, buy/sell order on market) which makes it hard for naive approach to successfully imitate an expert policy.

If BC approaches started flooding the leaderboard, then I'm sure RL is starting to work for those at the top.


dzjiann · 1144th in this Competition · Posted a month ago
End-to-End RL Is Harder Than It Looks: Many Replays from Leaderboard, but Not Much to Learn From
I spent nearly a week experimenting with reinforcement learning, using a model to directly control every action at every turn. Unfortunately, I wasn't able to make it work.

The biggest challenge was cold start. I tried behavior cloning first, and although there are plenty of available replays, most of them are highly similar. As a result, the model could imitate some stereotyped behavior patterns, but it struggled to learn the underlying principles of farm management and long-term decision making.

Exploration was even harder. There are many crop types, their growing cycles are long, and the farmer has a very large action space. This makes meaningful exploration extremely difficult.

I also experimented with many forms of reward shaping. Eventually, the agent learned to manage the first plot of land reasonably well, but it failed to generalize that behavior to the second and third plots. On those additional plots, the successful harvest rate was only around 20%–40% at best.

This created another problem: from the agent's perspective, buying additional land appeared to have negative expected value. As training continued, the policy gradually stopped purchasing land altogether.

So far, my experience has been that directly learning low-level control with RL is much harder than I initially expected, especially because failures in long-horizon farming decisions can make otherwise useful strategic actions look unprofitable.


5

1

1
17 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Cho Royou
Posted a month ago

· 1144th in this Competition

Hi, we’re also looking into this problem. Although I’ve been continuously training RL models, unfortunately, all of our high-scoring models so far have been rule-based.

I have a few ideas, but I still feel like I’m missing the key insight.

If there’s an opportunity, I’d love to team up and discuss it together.


Reply

React
dzjiann
Topic Author
Posted a month ago

· 1144th in this Competition

Thanks a lot for the invitation! Since you're ranked much higher than me, I'd of course be very happy to team up.

However, I just want to be transparent that I'm still quite new to kaggle and RL, and my current rank is only around 500. So I'm worried that I may not be able to contribute as much as you might expect, or keep up with the team technically.

That said, I'd definitely be happy to discuss ideas, share what I've tried so far, and contribute wherever I can. If you're still comfortable with that, I'd be glad to team up.


Reply

React
Cho Royou
Posted a month ago

· 1144th in this Competition

We’re also just getting started with RL, so there’s absolutely no need to feel any pressure.

Discussing ideas together, exchanging insights, and learning from different ways of thinking are exactly why we joined this competition in the first place.

We’ve already sent you a team invitation and look forward to hearing from you.


Reply

2
BillDoser
Posted a month ago

· 5844th in this Competition

It's good to hear that I'm not the only one having trouble.

I'm still struggling with getting the training runs to produce something useful. I keep finding bugs that make some actions impossible for the agent to even attempt.

I started with behavior cloning and then to self play.

I think I'm getting close to a working solution.

I'm using an expected value reward system where a seed is worth it's purchase cost but a plant has a growing value and a harvested crop the most value. This is true with animals too.

I'm not 100% it will work but there needs to be some feedback that causes the agent to add value to his board.


Reply

React
fishcat
Posted a month ago

· 1903rd in this Competition

Can your BC work? My BC model has a poor score. It will have some single moves that look correct. But it cannot make effective decisions due to the accumulated error problem in BC.


Reply

React
dzjiann
Topic Author
Posted a month ago

· 1144th in this Competition

That is similar to what I observed. Although there are many leaderboard replays, the effective behavioral diversity seems much smaller than the replay count suggests. Therefore, the model performs poorly on out-of-distribution states.


Reply

React
Belati Jagad Bintang Syuhada
Posted a month ago

· 2625th in this Competition

Currently I'm trying to only focus on the first 14 days. If I can get my agent to do well in those 14 days, then I can start making the horizon longer.


Reply

React
nofreewill42
Posted a month ago

· 1095th in this Competition

I am currently just trying to maximize final bank with only one tile being used and only wheat planting and selling is allowed. This is in itself difficult enough already:D


Reply

1
nofreewill42
Posted a month ago

· 1095th in this Competition

AlphaStar gives me hope though


Reply

React

7 more replies
Profile picture for Belati Jagad Bintang Syuhada
Profile picture for nofreewill42
Profile picture for qihuaz
Profile picture for KiZins
dzjiann
Topic Author
Posted a month ago

· 1144th in this Competition

That makes a lot of sense. I think shortening the horizon is probably one of the most practical ways to make the problem learnable.


Reply

React
@mldsdev
Posted 22 days ago

· 6321st in this Competition

I’d say the biggest issue here is the huge and constantly changing action space. Are you trying to make the network responsible for every single step?

I’d probably go with a different approach. You could give the model a predefined pool of high-level actions, so the network handles the logistics and decision-making, while a separate planner takes care of the actual execution.


Reply

React
Sayaka Miki
Posted 24 days ago

· 6th in this Competition

In my experiments:

BC on average data is extremely bad. On some specific competitor's replay (or generated by public notebook) can reach almost 100% acc and do well in selfplay, but it can't generalize, of course.

BC + end2end RL can reach average 75k terminal coins in selfplay, but seems not very competitive for now.


Reply

2
Alberto MV
Posted 25 days ago

· 4394th in this Competition

Same here. Even with BC and BC + policy clipping, I ran into similar issues. It took me days just to rewrite the environment in JAX. I’ll keep trying though!


Reply

React
BillDoser
Posted 25 days ago

· 5844th in this Competition

I've been considering a JAX rewrite. What was the result?


Reply

React
Michael Timbs
Posted a month ago

· 1380th in this Competition

I gave up on this approach a few days ago. I only have a single 10 core machine and i did not feel like it was a high probability direction. Unfortunately the next direction i tried seems really good at optimising the market layer of fixed farming strategies but really bad at actually finding new market strategies. Swapping one crop to another or swapping to a different animal just completely tanks the entire rest of the play and destroys any gradient. Spent a few days trying to overcome this with no luck. I haven't bothered submitting because so far ive only been able to find marginally better approaches off the existing leaderboard strategies and they'll be easily defeated as soon as they are public. Need to figure out a way to learn coherently across the full time horizon given how coupled actions are


Reply

React
Deng Xianghuai
Posted a month ago

I believe the problems will be solved. Like in Orbitwars——in the early stage of that competition, I made a post to ask why nobody had used RL and many people discussed about it.

I regret giving up that competition too early. It's too early to abandon a potential method.

Although the competitions are so different, I believe new problems would also be tackled by you people.

Best of luck to you!


Reply

1
Wiz
Posted a month ago

· 3719th in this Competition

With great identification of the issue demands a great setup of an awarding mechanism. What hardware are you training on btw? if its not something crazy, it's usually recommended to start with heuristics and then fine-tune with rl.


Reply

React
dzjiann
Topic Author
Posted a month ago

· 1144th in this Competition

I actually have access to a 192-core CPU machine, which is one of the reasons I wanted to give RL a serious try. I’m still quite new to RL though, so I’m sure I’m not using the hardware nearly as effectively as I could yet


Reply

React
Wiz
Posted a month ago

· 3719th in this Competition

wow. for sure yeah. high investment high return. recommend to look into past competitions' top solutions.


Reply

React
Omkar Kadam
Posted 25 days ago

· 703rd in this Competition




Reply

React
Mohit
Posted a month ago

eventually u will get ahead


Reply

React
dzjiann
Topic Author
Posted a month ago

· 1144th in this Competition

Thanks! Still experimenting


nafspf · Posted 21 days ago
Questions on rendering, yields, and input arguments
Hello everyone,

I just started looking at this interesting competition, but I am confused for several things.

Does anyone have issues with rendering? I used the sample code on Overview page but I do not see any output, except the output from print(), from Jupyter notebook. I am running on Windows and installed environment using Anaconda.

For the yield table, I am simply confused how values were calculated. Say the yield/tile/day for wheat is 0.8. If max yield is 6 and needs 3 days (day 2 to 4), how is that possible 6/4 = 0.8? Same for animals, I don't get how the yield/tile/day was. If there are 4 helds per day for eggs, how is the steady states being 1 not 4?

I am also a bit confused by the fertilizer. I thought one fertilizer only applies to one plant, but when I was randomly watching leaderboards, it seems players are buying 1 at most. Does that mean 1 farmer/hand can pickup 1 fertilizer and use it for all other plants on the same day?

I see one should define an agent function with obs as the input argument, but is there a way to frame as a class so one can store some calculated variables and so on without computing again and again for each turn?

Thank you if anyone can answer my questions.


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Ashutosh Agarwal
Posted 21 days ago

· 2272nd in this Competition

Yield/day/tile is calculated on the basis of total days it took to grow, and max yield(without fertilizer). For example, wheat produce 4 wheat(without ferlizer) in 5 days(from day on which it is planted to max yield day). So it become 4/5 =0.8. Same applies for animals.

If you are saying that you see 1 fertilizer in shed then it is kinda misleading. Actually before using fertilizer, we have to pick fertilizer from shed and after pickup it is added to Farmer or hired hand inventory which we can't see in replay.

I hope this is helpful😊


SCLim2022080004 · 2943rd in this Competition · Posted 24 days ago
Rules clarification: using a publicly published agent as a submission
Public notebooks in this competition share complete, runnable agents, and forking public work is normal on Kaggle. I would like to understand where the line sits for this competition specifically, because two rules seem to bear on it.

Rule 3.14.a asks each entrant to warrant that a Submission is "your own original work" and that they are the "sole and exclusive owner and rights holder of the Submission". The Winner License in section 5 then requires a winner to license the submission and its source under CC-BY 4.0, and section 2.8 requires a winner to publish a description detailed enough that someone can reproduce the approach by reading it.

Three cases, in increasing distance from the original:

Submitting a public notebook's agent verbatim, unchanged.
Using a public agent unchanged as a backbone, with your own decision layer on top that decides per turn whether to follow it or deviate.
Reimplementing a strategy that a public notebook describes, in your own code.
Which of these are acceptable submissions?

And for a prize-eligible finish, how do 3.14.a and the section 2.8 reproducible description obligation apply when part of the submission originates from another participant's published notebook? In particular, can an entrant grant the CC-BY 4.0 winner license over code they did not write, and would attribution to the original notebook author be sufficient?

Thanks and I think a clear answer would help a lot of people here, since the public notebooks are strong and widely forked.


React
3 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Addison Howard
Kaggle Staff
Posted 23 days ago

· 557th in this Competition

Anything freely and publicly available is fair use.


Reply

React
GarrieD
Posted 23 days ago

· 2458th in this Competition

Rest assured, submitting a public notebook's agent verbatim and unchanged will never win a Kaggle competition. I do this frequently and consider it to be fair use because my only intention is to verify how well such an agent will do on the public leaderboard. I then take the more promising agents and feed them into the fitness function of my genetic algorithm in the hope of generating a better agent that can compete against all published agents.


Reply

1
Andrey Chankin
Posted 23 days ago

· 449th in this Competition

all are ok, its prohibited to use privately shared outside of the team code

Version - 5

Can game parameters change mid-competition or on final evaluation?
Such as MARKET_I0 = 10000 and PRICE_FLOOR = 1? They are always the same currently (across different seeds, etc). @bovard @macruzbar


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
María Cruz
Kaggle Staff
Posted 19 days ago

Hi @max6296 -- game parameters do not change mid-competition or on final evaluation. Hope that helps! Good luck =)


Amedeo Biolatti · 4729th in this Competition · Posted 25 days ago
Small environment change proposal: split weeds and shop randomness
Right now weeds spawn and shop choice use the same rng, so the shop choice is influenced by players actions (depending on the number of empty tiles).

While this is not generally wrong, it make comparing different agents on the same seed more noisy. Would it be possible to use two different rng instead? Something like

rng_weeds = random.Random((seed * 1_000_003) ^ day)
rng_shops = random.Random((seed * 1_000_003) ^ day + 1)
PS: a possible alternative could be to change the order in _spawn_weeds

if rng.random() < weed_chance and farm["tiles"][y][x] is None:

but it would require more rng.random calls


1
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
qihuaz
Posted 25 days ago

· 2780th in this Competition

hmmmm. I came accross this issue as well but didn't think further. Now your post gave me an idea:

Do we really need the official env to change, or maybe we can just implement this change locally?? It reduce noise during developement and should have no negative impact when the agent are evaludated in the official environment, right?


Reply

React
Amedeo Biolatti
Topic Author
Posted 25 days ago

· 4729th in this Competition

Yes, I already did locally.

But implementing this in the official environment would have a big advantage: you could play against a fixed replay from the official dataset. My current workaround is to force the shop unlock sequence, but it doesn't look that nice


Reply

React
Michael Timbs
Posted 24 days ago

· 1332nd in this Competition

yeah i just have a local harness that can force shop evolution and weed evolution so that i can do fixed replays (as well as sensitivity analysis on weed positions and shop evolution)


Reply

React


Ritwik Raha · 3368th in this Competition · Posted 24 days ago
Kaggriculture - Hillclimbing
Goal
The game score is the money in the bank after 720 turns.

Unsold stock has no final value.

The main objective is the chance of winning a duel:


Here:

$\theta$ is the agent configuration.
$B_\theta$ is our final bank.
$B_{opp}$ is the opponent's final bank.
Final bank alone is not enough for local testing. We use the margin:


Every test runs both seat orders with the same seed.

The paired margin is:


This reduces seat bias.

Core strategy
The farm follows a stable production schedule.

Expand land early.
Build a compact farm.
Use cows and sheep for premium products.
Grow wheat for feed and sales.
Grow melon and strawberry for high-value sales.
Hire enough hands to feed, care, water, and harvest.
Sell all useful stock before the season ends.
The production layer is fixed.

The market layer reacts to the shared market.

V11
V11 adds a small premium selling layer to the production schedule.

It watches four products:

Product	Minimum price	Batch
Milk	120	3
Wool	140	3
Strawberry	90	3
Melon	60	3
The layer starts on day 18.

It uses only free market slots.

It does not remove or reorder existing orders.

PREMIUM = ("MILK", "WOOL", "STRAWBERRY", "MELON")
FLOOR = {
    "MILK": 120,
    "WOOL": 140,
    "STRAWBERRY": 90,
    "MELON": 60,
}

MIN_DAY = 18
BATCH = 3
MAX_ORDERS = 10
The sale rule is simple:

for item in PREMIUM:
    if len(market) >= MAX_ORDERS:
        break
    if item in already_selling:
        continue
    if shed.get(item, 0) <= 0:
        continue
    if prices.get(item, 0) < FLOOR[item]:
        continue

    quantity = min(shed[item], BATCH)
    market.append(["SELL", item, quantity])
This improves cash conversion late in the game.

It also sells before a large premium stock can lose value.

Market model
Selling adds units to the shared market inventory.

More inventory can lower the next sale price.

For a sale of $q$ units, expected revenue is:


Here:

$I$ is current market inventory.
$p(I)$ is the current price function.
$q$ is the sale quantity.
Waiting has a cost when another player may sell first.

A simple timing value is:


V11 uses a conservative choice. It starts late and sells small batches.

V12
V12 keeps the same production schedule.

Only two values change:

Parameter	V11	V12
Start day	18	14
Batch size	3	15
MIN_DAY = 14
BATCH = 15
The price floors stay unchanged.

The product list stays unchanged.

The ten-order limit stays unchanged.

The larger batch captures more value while prices are still above the floor.

The earlier start gives the agent more chances to sell premium stock.

Search
The first screen varied one axis at a time.

For each configuration, we measured:



The timing screen tested:

start_days = [10, 12, 14, 16, 17, 18, 19, 20, 22]
The batch screen tested:

batches = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30, 40, 60]
The best screened pair was:

start_day = 14
batch = 15
Very small batches gave away the timing edge.

Very large batches pushed too much stock through the price curve.

The middle value worked best.

Validation
The selected values were tested on seeds that were not used for selection.

Each seed was run in both seats.

Test	Result
Games	20
Wins	19
Losses	1
Positive paired seeds	10 of 10
Mean game margin	+857
Median game margin	+663
Mean paired margin	+1,713
Completed games	20 of 20
The promotion rule was:


V12 passed this rule.

Result
V11 built a safe late premium seller.

V12 made that seller earlier and larger.

The farm plan did not change.

The improvement came from market timing.

The main lesson is simple:

Keep production stable.
Change one market rule at a time.
Test both seats.
Select on one seed set.
Confirm on new seeds.
Promote only when the paired result stays positive.

React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Thomas Tschinkel
Posted 24 days ago

· 232nd in this Competition

Nice approach, especially keeping the production fixed and only tuning the market side. The difference from just changing start day + batch size is pretty surprising. Thanks for sharing!



starkhushi · 8130th in this Competition · Posted 25 days ago
Price curves differ wildly by product — data from 5 top-agent replays
I logged every market price across all 720 steps in 5 replays of a top-rated agent. The goods don't behave alike at all:

Good	Start	Peak (day)	End
FERTILIZER	100	100 (d0)	10
MELON	250	272 (d10)	60
MILK	160	204 (d9)	61
WOOL	200	226 (d12)	87
STRAWBERRY	120	204 (d14)	126
WHEAT	25	45 (d21)	33
CARROT	35	50 (d28)	47
EGG	50	66 (d27)	66
Four takeaways:

Fertilizer never gets better than turn one — it only decays (endings across the 5 games: 20, 9, 1, 18, 4). Sell it the moment you collect it.
Premium goods have a window, roughly days 9–14. A melon sold on day 25 is worth about a fifth of one sold on day 12.
The cheap goods are the ones that appreciate — wheat nearly doubles by day 21, carrot and egg also end higher than they start.
Crashes barely recover: melon bottomed at 89 on day 16 and had only reached 96 three days later. Plan your timing rather than waiting for a bounce.
Caveat: 5 replays from one agent, and prices depend partly on what both players sell — treat the exact peak days as approximate. The fertilizer decline and the wheat/carrot/egg appreciation were the most consistent.

Has anyone checked whether the town-shop unlock schedule drives those day 9–14 peaks?


React
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
djschmit
Posted 24 days ago

· 2758th in this Competition

If you want more information on how exactly market prices are calculated, it's available in the "how to play" section of the competition overview: https://www.kaggle.com/competitions/kaggriculture/overview/how-to-play


Reply

React
starkhushi
Topic Author
Posted 23 days ago

· 8130th in this Competition

sure will review that ..


Karthikeya Thatipamula · 5111th in this Competition · Posted 23 days ago
Melon isn't in any shop menu - town demand is exactly 1/day on every seed
Quick thing I noticed while measuring what the town actually eats.

I ran 16 seeds with two PASS agents and just watched market["inventory"] drain.

Melon came back at exactly 1.0 unit per day. Same on every seed.

Everything else swings a lot:

wheat 9.4 - 23.2 per day strawberry 6.4 - 22.0 wool 1.0 - 23.8 carrot 4.0 - 21.4 melon 1.0 - 1.0

Then I checked SHOPS in the env source. Melon isn't in any of the eight menus.

So that 1/day is just the town centre tick. Nothing in town ever asks for melon.

Here's the part I didn't expect.

Melon is still one of my best earners. Around $31k a season.

Base price is 250 and the cushion is deep, so ~160 units still average about $195 each. Nobody wants them and they still sell fine.

But it doesn't scale.

Wheat and milk keep paying because the shops keep eating. Melon is a fixed pot. You cash it once, and past 150-200 units the curve is gone.

Worth knowing before you expand into melon late game.

Two questions.

Wool goes from 1.0 to 23.8 per day depending on how many YARN_STOREs open. That's a 24x spread on one product.

Is anyone actually reading town["unlocked_shops"] and farming to match? Or are we all running fixed portfolios and letting the price curve sort it out?

And has anyone found a use for melon past the one-time cash out?

PS - if you haven't seen the obs["step"] seat-1 thread, worth checking whether you read that field anywhere. day * turnsPerDay + hour works in both seats.

Download Leader plays through MCP or programtically
Is there a way to download play logs through MCP or programtically. Not my games, but other top players.


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Bovard Doerschuk-Tiberi
Kaggle Staff
Posted 23 days ago

· 9021st in this Competition

https://www.kaggle.com/datasets/kaggle/kaggriculture-episodes-index

How do you perform behavioral cloning?
Hi. I'd like to know how the replay-based approach works. The thing is, I can't figure out how to convert replays into actions. Could someone show me how to do it?


React
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
destbreso
Posted a month ago

· 1053rd in this Competition

There is nothing to reconstruct: the replay JSON already stores the exact action each agent submitted at every step, in the same format the environment consumes. Extracting it is a few lines.

import json

replay = json.load(open("episode.json"))
seat = 0                                   # 0 or 1, whichever agent you want

# The action submitted FOR turn t is recorded at steps[t + 1].
actions = [replay["steps"][t + 1][seat]["action"]
           for t in range(len(replay["steps"]) - 1)]
That t + 1 is the tricky part, and it is the one thing worth checking carefully, because an off-by-one here produces an agent that runs, never errors, and simply plays badly. The cheap verification is to replay the extracted tape against the recorded opponent at the recorded seed and confirm the final banks match the replay to the dollar: with the offset right they match exactly, with the offset wrong they do not.

Two more details that are easy to miss:

A 720 step episode contains 719 acting turns, so the last recorded step holds the terminal state and no action. And each action is already a plain dict, {"farmer": [...], "hands": [...], "market": [...]}, so it can be fed straight back with no translation layer.

Replaying it is then just an index lookup:

PASS = {"farmer": ["PASS"], "hands": [], "market": []}

def agent(obs):
    t = obs["day"] * 24 + obs["hour"]      # not obs["step"]
    return ACTIONS[t] if t < len(ACTIONS) else PASS
The comment on that line is the common mistake worth flagging. Deriving the turn from day * 24 + hour is safer than reading obs["step"], because trimmed observations can arrive without a step field, and the usual defensive idiom for that, int(obs.get("step", 0) or 0), quietly returns 0 and replays turn 0 for the entire game. It produces no exception and no warning, just an agent that does nothing all season.

The base85 blob you see in published agents is not part of this
Worth separating, because it is the step that looks cryptic and is actually the least interesting one. If you open a public replay agent you will find something like json.loads(zlib.decompress(base64.b85decode(_BLOB))) at the top, and it can read as though decoding were part of turning a replay into actions. It is not. The actions are already plain dicts, as above. The encoding exists only because a submission is a single main.py and 719 turns of dicts are bulky: written as raw JSON the tape I just measured is 113 KB, and compressed and text-encoded it is 11 KB, about ten times smaller.

So it is packaging, and it is symmetric. To pack, once, offline:

import base64, json, zlib

payload = json.dumps(actions, separators=(",", ":")).encode()
blob = base64.b85encode(zlib.compress(payload, 9)).decode()
# then write `blob` into main.py as a plain string literal
And inside the agent, to unpack once at import:

import base64, json, zlib

_BLOB = "..."                                   # the string you just wrote
ACTIONS = json.loads(zlib.decompress(base64.b85decode(_BLOB)))
base64 and zlib are both in the standard library, so this adds no dependency. And the round trip is exact, so it is worth asserting that once when you generate the file: pack, unpack, and check the result equals the list you started from. If it does, nothing downstream can be blamed on the encoding.

You can skip the whole thing while you are experimenting and just paste the list literal into the file. It will be a large file, and it will work.

On submitting a clone, since the mechanics above make it easy
I would not submit a cloned agent as a competitive entry, and I think it is worth saying why plainly rather than leaving it implied.

The first reason is that it is not mine to submit. If you do publish work built on someone's replay or someone's public notebook, name them in the module docstring and in the submission message. Public notebook code is shared under an OSI-approved licence by rule 3.6.b, so building on it is legitimate, and attribution is what makes it honest rather than optional.

The second reason is that the rules already close the door. Section 3.14.a asks you to warrant that your submission is your own original work and that you are its sole and exclusive owner, and section 2.8.a.1 requires a prize winner to publish a description detailed enough that someone can reproduce the approach by reading it. A pure clone has no such description to give.

The third reason is practical: a clone does not appear to have the potential to reach the original. A rating is a measurement against the field of the moment, and the field keeps moving, so a fixed copy of something that scored well last week is being scored against a different population this week. I wrote that up separately with the sampled series behind it: rating convergence, episodes not hours.

What replays are genuinely good for
All of which is not an argument against extracting them, because they are useful for several things that are not "submit it and hope":

Calibrating your offline measurement. A submission gives you real ladder outcomes to check your offline instruments against, which is the only way to find out that an offline number you trust does not predict anything.

Simulating matchups. Running recorded agents locally against your own lets you approximate pairings before spending a slot. Not exact, since the real ladder chooses your opponents and the seeds, but far better than testing against an empty market.

Sparring and control. A fixed recorded agent is a stable opponent, which makes it an excellent control for instruments and for engine invariants: if a change in your harness moves a result against a fixed opponent, the change is in your harness. Cheap to do at scale with the C++ engine port.

As a base for something of your own. This is the direction I have found most interesting: take a recorded route as a fixed backbone and put your own algorithmic layer on top, one that decides at each turn whether to follow the recorded action or to do something better given the state. That produces an agent that is yours, with a traceable ancestor you can credit, and it seems to be a comparatively cheap way to reach agents that play in the 2,000+ range. The layer is where the work and the originality live.

Credit the source either way, and good luck out there.


Reply

2

2
renji_starfall
Topic Author
Posted a month ago

· 464th in this Competition

thank you bro

Is there a time limit on each agent's turn?
I wonder if there's a time limit on how long each agent's player can take per turn. Imagine having a perfect AI that can play the game, but in exchange, it requires a lot of time and resources for every turn. I'm still trying to develop my own algorithm and I'm not doing very well on the leaderboard yet, but I fear that my algorithm will take too much time per turn. What do you guys think?


React
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Michael Timbs
Posted 24 days ago

· 1332nd in this Competition

From memory if you inspect the environment code it is there. The limit is from memory 1-2s which should be plenty of time for any submission that fits under the 100MB package limit. You probably can't do deep MCTS though


Reply

1
Tim McGarvey
Posted 24 days ago

· 3408th in this Competition

IIRC you get 1s/turn as a soft budget, backed by a 60s/episode overage pool you can dip into across turns. This overage pool has to account for your first-turn hit for model load. The whole episode is hard-capped at 1200s regardless.


NNMax · 650th in this Competition · Posted 25 days ago
Code & Dataset archives for Replay analysis, BC, RL and more
Code -> top10-replay-dataset-archive

Dataset -> kaggriculture-top10-replay-archive

Some Tips:

Adjust TOP_N in the code to your requirements.
Schedule the notebook to run daily, so you dont have to worry about running it manually everyday.

React


守银摄金难铜 · 436th in this Competition · Posted a month ago
Could the game’s rating system be improved?
Could the game take players’ historical ratings into account and introduce placement matches? Having every new submission start at 600 rating is a huge waste of time.

A better approach would be to match new submissions based on the player’s historical rating. If the submission loses, its provisional rating could be reduced by half before it enters another placement match. During placement matches, the opponent should neither gain rating for winning nor lose rating for losing. Once the placement phase is over, normal matchmaking and rating changes can resume.

Also, suppose you are a player rated above 2,000 and your new submission is simply an improved version of your previous method. If it happens to face another high-rated player’s new solution during the early matches, one side could lose a huge amount of rating immediately. That feels extremely unfair.


React
5 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Tien N.
Posted a month ago

· 867th in this Competition

My main issue is, I was in top 50, and I re-submitted and I'd be 500 points lower, even though it's identical. So this is counter incentive to submit a marginally better solution.


Reply

React
守银摄金难铜
Topic Author
Posted a month ago

· 436th in this Competition

The exact same solution can score much lower when resubmitted, and I have no idea why. I resubmitted a solution from two days ago and the score dropped by almost 1,000 points. Surely everyone couldn’t have improved that much in just two days, right?


Reply

React
This comment has been deleted.

Michael Timbs
Posted a month ago

· 1333rd in this Competition

yes the improvement every day is quite impressive


Reply

React
RuggedBones
Posted a month ago

· 1067th in this Competition

Yes, I've encountered exactly the same situation these days.


Reply

React
Navneet
Posted a month ago

Yes, I think it's possible to improve the game’s rating system @wocenmma


Reply

React
Wiz
Posted a month ago

· 3713th in this Competition

exactly. and also the one already submitted could be staying in an easier zone, all facing old agents. and we could not submit two newer agents, or else the old one is not gonna stay. So it's really not encouraging new trials and submissions.


NNMax · 658th in this Competition · Posted a month ago
Is Pure Self-Play PPO viable?
So far, I'm only doing a dynamic heuristic approach as of now and a complete beginner in RL. From my point of view, the competition requires extremely precise decisions for every step or else the mistakes quickly stacks up before our agent manage to recover those losses.

So this raises some questions for me

If one tries to design a self-play RL agent, what kind of reward structure would they choose? Because if we were to design the reward to encourage the agent to recover the losses, it might not care too much about future steps and may get stuck in a local optima trying to recover short term losses. But if the reward aims only for final win after 720 steps, there's also a chance it might get stuck on a local optima which will seem satisfactory to the agent because it might think that optima is good enough for these complex decisions. If both reward structures were to be combined, it may create a massive confusion for the agent on what to optimize. These are just my speculations, I'm happy to be proved wrong.

Is there a chance of grokking phenomenon happening to RL training which makes the RL model to find the global optimum?

A hybrid approach might be plausibly better but I have no idea how to make that work 😄


React
14 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
hengck23
Posted a month ago

· 3576th in this Competition

you don't start a business and wonder what to do every day. you start a business with a plan.



this first think i would do is to copy a high reward replay agent (eg 93311715). then i train a RL to estimate opponent capacity, cash on hand, maybe selling date etc.

then derive some "deviate from forcast" features and input (with opp estimates) to market policy net.

"deviate from planned reward, etc" is easily learned via BC from replay


Reply

React
NNMax
Topic Author
Posted a month ago

· 658th in this Competition

Thanks for the info. For now, I'm not doing RL because my other deterministic experiment is paying off locally very well. If that translates exactly to the leaderboard then I guess I dont have to do RL at all. Let's see how it goes…


Reply

React
hengck23
Posted a month ago

· 3576th in this Competition

That is possible. Most solutions so far are not really fighting against opponent agent yet. And maybe that will be the way till deadline. Rl is only useful if there are online decisions to be made. But in this kaggariculture it is difficult to apply rl. Maybe some magic notebook will appear.


Reply

3
Belati Jagad Bintang Syuhada
Posted a month ago

· 2640th in this Competition

I doubt magic notebook showing RL end-to-end would appear since… it takes a lot of work to get everything up and running 😅 but I'm sure there will be a magic submission which dominates each matchup to the point where we are sure the guy isn't using rule based agent anymore


Reply

React
Shubham Phapale
Posted a month ago

· 3448th in this Competition

I converted the environment into jax and tried training on kaggle TPUs (quite a good SPS), doing complete self-play I was able to get final gold of about 20k-22k not more than that (gave up :(). The best reward function I thought was (720th turn my gold - 720th turn gold of opponent.)


Reply

React
Ryan Myers
Posted a month ago

· 5365th in this Competition

Tried it, and had difficulty getting it to work well. If you can get it to work, I think hybrid is likely the optimal approach such that you have a deterministic set of rules, and a small set of learned actions which control aspects of the game which are ambiguous/non deterministic.


Reply

1
Sahaj Deep Singh
Posted a month ago

· 4476th in this Competition

The main issue here is sample volume and rollout throughput. Kaggriculture has a long 720-turn horizon, and updating the policy after every single episode destroys your Games Per Second (GPS). For an agent to discover good multi-step investment strategies rather than getting trapped in short-term local optima, you realistically need at least 10M+ games of experience. Until you scale up throughput via large vectorized batches or decoupled actor-learner training, pure PPO will naturally struggle against deterministic rule-based scripts.


Reply

1
Zacchaeus
Posted a month ago

· 5488th in this Competition

just a data point, I've managed to make PPO get some money but far less than rule-based method can easily earn


Reply

React
LuvGoel(O)
Posted a month ago

· 3209th in this Competition

Same for me, rule-based methods are earning over 150k, but PPO is stuck under 5k


Reply

React
This comment has been deleted.

Mahog
Posted a month ago

· 6960th in this Competition

Same, my PPO model is stuck around 20k :V


Reply

React
shiba-inu
Posted a month ago

I'm using RL with two policies:

A worker policy that chooses tasks and targets (the actual movement toward the target is handled by a rule-based controller).
A trading policy for buying and selling resources.
However, the agent only makes about $100-$3,000.

Earning over $20,000 is really impressive. Are you also using some rule-based components in your solution, or is it mostly RL? Any thoughts on what might be causing my agent's poor performance?


Reply

React

7 more replies
Profile picture for Gerardo Del Toro
Profile picture for Mahog
Profile picture for shiba-inu
Gerardo Del Toro
Posted a month ago

RL takes longer, but usually gets you further 🤔


Reply

React
Shubham Phapale
Posted a month ago

· 3448th in this Competition

I thing to build a winning self play RL solution will require really high compute for this competition due to large action space, overall game complexity and sparse signals for unhackable reward.


Reply

React
Phương Doan
Posted a month ago

· 4494th in this Competition

Yes it is, I was able to make it earn 100k atm, but I have to do hybird of both rule based and PPO


Reply

React
寿!
Posted a month ago

· 4359th in this Competition

My PPO isn't working well either. I do think RL will end up stronger in the later stages, but right now, while it does get stronger than the imitation learning it's based on, the base imitation learning itself is just too weak, so it can barely beat the public NB.


Reply

React
hwe owe
Posted a month ago

· 775th in this Competition

since the competition have only a little input that can let the agent move,so it might be bad than rule.

if you really want to dig in rl/ppo,SL + self-playing may be a good choice


Reply

React
This comment has been deleted.

NNMax
Topic Author
Posted a month ago

· 658th in this Competition

I know of dynamic hybrid agents where heuristics and action-value models are combined to produce final action for each step. But yours sounds like a sequential one, is there any advantage to it?


Reply

React
This comment has been deleted.

Roy Wei
Posted a month ago

Isn't MCTS designed for situations where 2 players take turns rather than acting simultaneously?


dzjiann · 1108th in this Competition · Posted a month ago
RL of Meta Agent: 960 Matchups and a PPO Plateau
I have been training a replay-based Kaggriculture meta-agent with reinforcement learning. The policy uses PPO to select and switch between high-scoring public trajectories. During training, it improved against some public agents while becoming worse against others, and eventually plateaued despite healthy PPO statistics.

My current hypothesis is:

The PPO plateau may not be only an optimization failure. Many strong routes share similar early behavior, but the policy must choose an opening before it can identify the opponent. Once it enters a route branch, prefix constraints remove most alternative continuations. If the openings counter one another, conflicting policy gradients can naturally converge toward a mixed strategy.





The reinforcement-learning setup
Each rollout samples opponents from several strong public agents plus self-play. The reward is purely zero-sum:

win  = +1
draw =  0
loss = -1
PPO updates only the sparse route-selection decisions, while the selected expert route executes the low-level farming actions. Old trajectories are not reused across iterations; each new rollout is optimized for several PPO epochs and then discarded.

This setup learned meaningful counters, but it did not produce monotonic improvement against every opponent. Gains against one strategy were often accompanied by losses against another.

What PPO is trying to optimize
I ran 960 games among six public strategies, using 16 seeds and both seats for every directed matchup.

One clear cycle was:

Matchup	Result
Public B85 vs Andrews 2883	30-2
Andrews 2883 vs Kaito v35	21-11
Kaito v35 vs Public B85	24-8
Adaptive Farming was strongest overall, winning 121 of 160 games, but Kaito v35 still beat it 17-15. This suggests that the pairwise payoff matrix is more informative than average win rate.

I also ran a preliminary held-out diagnostic:

Information	Outcome accuracy
Majority baseline	54.2%
Opponent only	56.5%
Opening branch only	56.5%
Opening and turn-120 branches	57.5%
Opponent and opening branch	67.5%
The interaction between opponent identity and opening choice was much more predictive than either alone. This is consistent with matchup-specific openings, although it does not prove that the game is decided at turn 0 or that a Nash equilibrium has been reached.

Why the PPO gradients can cancel
Suppose opening A is strong against one opponent and weak against another. At turn 0, their future strategies are not yet observable. Training then generates conflicting gradients:

opponent X: increase P(opening A)
opponent Y: decrease P(opening A)
If the observation cannot distinguish X from Y, a larger model or more PPO epochs cannot resolve the conflict. Gradients cancel, entropy remains high, and aggregate reward plateaus. In that situation, persistent policy entropy may represent a reasonable mixed strategy rather than failed RL training.


9
4 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Pascal Andreas
Posted a month ago

· 4311th in this Competition

I suspect the non-transitivity problem is why other Kagglers have struggled with RL. Pure self-play is obviously not viable, and policy diversity in your local pool is desirable.


Reply

1
DILIP BAVISKAR
Posted a month ago

· 9315th in this Competition

Yes I faced this issue. When I tested agent using traces I can see actions but after submission nothing was happening.


Reply

React
TommyCyd
Posted a month ago

· 3238th in this Competition

I really like the dashboard in your post. It has a W&B-like feel, but looks much cleaner and more customized. Is this an existing tool, or something you built locally from your experiment logs?


Reply

React
dzjiann
Topic Author
Posted a month ago

· 1108th in this Competition

Iasked GPT to build a dashboard to show my experiment logs and GPT really did it well.


Reply

1
Omkar Kadam
Posted a month ago

· 716th in this Competition

Can you share the prompt you gave like if you feel free to give or else its ok 😊


Reply

React
dzjiann
Topic Author
Posted a month ago

· 1108th in this Competition

Sorry, i forget it. It's only simple prompt.![alt text](image-7.png)


Omkar Kadam · 714th in this Competition · Posted a month ago
Any Tips for Someone Starting the Competition Now?
Any tips for someone starting the competition now?
What approaches are actually working and worth trying?
Also, would Behavior Cloning, RL/PPO, or heuristic-based approaches be effective or like how ?
Any guidance on what to focus on would be really appreciated❤️!


React
7 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
destbreso
Posted a month ago

· 1058th in this Competition

On the RL question specifically, the constraint that determines the approach is the cost of an episode rather than the algorithm itself. The official environment runs at roughly one episode per second, so a training loop that requires tens of thousands of episodes is bounded by simulation throughput long before it is bounded by the architecture. It is worth pricing that out before committing to a method, since this can make the difference between an idea that fits in a week and one that does not.

The other practical detail is version pinning. The engine changed on August 15 (discussion 735311), and carrot, tomato, and egg no longer have the same prices they did before, so any number measured before that date was measured on a different version of the game. Kaggle images can also ship with an older version of kaggle-environments than the one used by the competition, which can make a local result silently disagree with the leaderboard:

!pip install -q kaggle-environments==1.32.7
import kaggle_environments
assert kaggle_environments.__version__ == "1.32.7", kaggle_environments.__version__
Cheap to add, and it turns a confusing disagreement into an explicit failure.

NOTE: I maintain a public C++ port of the engine that runs at about 2,000 episodes per second, which directly addresses the throughput constraint above. The approach here is directly inspired by @nikital7's excellent 4000x environment speedup. I just added a patch for v1.32.7 along with a Python API and some improvements.


Reply

2
Omkar Kadam
Topic Author
Posted a month ago

· 714th in this Competition

I wanted to ask what hardware you’re using ? Also, would you be able to share the source code or repository for the C++ environment?


Reply

React
destbreso
Posted a month ago

· 1058th in this Competition

I just released a faster version: https://www.kaggle.com/code/destbreso/from-1-to-24-000-episodes-a-second


Reply

1

1
Navneet
Posted a month ago

Please share some tips for Tips for Someone Starting now @itzzomkar


Reply

React
Zhenyu Zhang
Posted a month ago

· 707th in this Competition

Take a look at the public notebook. Some notebook might even get you to silver.


Reply

React
Omkar Kadam
Topic Author
Posted a month ago

· 714th in this Competition

Okay I will take a look


Reply

React
dzjiann
Posted a month ago

· 1109th in this Competition

Start from the approach based on replay may be easier. RL need to generate new way. It's difficult and I only find the 1st player does it everyday.


Reply

React
Omkar Kadam
Topic Author
Posted a month ago

· 714th in this Competition

Are you suggesting behaviour cloning?


vdthcmus123 · 672nd in this Competition · Posted 24 days ago
BC + RL and Rule-based, what is an accessible guide for beginners?
Hi everyone, I’m a beginner in RL through Kaggle competitions, but I’m feeling confused and unsure about how to handle my agent. I tried setting up a few small BC agents using Terra xhigh and Sol ultra for coding, but they didn't seem to perform well. The two agents I created only achieved scores of 1,000–1,500, despite the relatively large amount of input data. As for rule-based, it is difficult to analyze behavior and determine what changes to implement for the agent, I find that analyzing losses and addressing them is extremely time-consuming, yet the results often fail to show any improvement in leaderboard scores. I have read several discussions and realized that rule-based approaches are currently proving significantly more effective than RL. However, choosing the right direction for agent development is very challenging. Could you all share some tips on developing an effective agent? I tried an approach similar to the one used in the Pokémon competition, but unfortunately, I only ranked 1,000th. I’m really keen to improve my ranking in this competition.




VijaiKurianMathew · 3060th in this Competition · Posted 24 days ago
Your "GPU" Kaggle kernel may be silently running on CPU (P100 vs PyTorch 2.10) — check + fix
TL;DR
enable_gpu=true ≠ GPU. Kaggle sometimes gives a Tesla P100 (2016, sm_60); modern PyTorch (2.10) only supports sm_70+, so it warns once and runs on CPU — no error. A run that should take ~3h on GPU takes days on CPU (~13x slower). I lost time to this. Here's the fix.

What you see (earlier vs now)
EARLIER: enable_gpu=true (default) -> P100 sm_60
  torch 2.10.0 cuda True
  Tesla P100 cap (6,0) compatible False sm_60
  device=cpu   SPS ~740    100M steps ~ days

NOW:     machine_shape=NvidiaTeslaT4 -> T4 sm_75
  Tesla T4 cap (7,5) compatible True
  device=cuda SPS ~10,000 100M steps ~ 3h
Look for this warning: Tesla P100 ... sm_60 is not compatible with the current PyTorch installation.

Fix (1 line) + verify
{ "enable_gpu": true, "machine_shape": "NvidiaTeslaT4" }
CLI: kaggle kernels push -p . --accelerator NvidiaTeslaT4

Verify first cell, before any long run:

import torch
cap = torch.cuda.get_device_capability(0)
assert cap[0] >= 7, f"GPU sm_{cap[0]}{cap[1]} -> CPU"
print(torch.cuda.get_device_name(0), cap)   # expect: Tesla T4 (7, 5)
Notebook: https://www.kaggle.com/code/vijaikm/kaggriculture-gpu-trap-cpu-run


starkhushi · 8134th in this Competition · Posted 25 days ago
Crop economics per tile-day, and why an all-melon opening goes bankrupt
I burned three agents before one worked, and the reason was economics rather than code. Sharing the numbers in case they save someone else the same detour.

Profit per tile-day, straight from the crop table
Pulling CROPS out of the environment and pairing it with opening market prices:

Crop	Seed	First yield	Max yield day	Units	~Price	Profit per tile-day
WHEAT	10	day 2	day 4	6	29	~41
CARROT	20	day 2	day 3	4	35	~40
TOMATO	50	day 8	ongoing	4	60	—
STRAWBERRY	100	day 10	ongoing (2d)	4	132	—
MELON	80	day 10	day 12	6	260	~123
Melon is roughly three times better than wheat per tile-day. The obvious move is to fill the board with melons.

That obvious move is a trap
Melon costs $80 a tile and returns nothing until day 10. Filling ~25 tiles is $2,000 of a $3,000 purse, and the bill does not stop there — hands must be re-hired every day. My all-melon agent finished on 18 coins: it went broke around day 3, could no longer afford to hire, a single farmer could not water 25 plants, and the whole crop died before a single melon matured.

What actually worked was using wheat as a bootstrap — it pays from day 2 — and converting tiles to melon only out of realised profit. Same board, same engine, same code structure:

Agent	Final bank
All-melon opening	18
Livestock-first (copied from replays)	2,687
Wheat bootstrap → melon	15,394
(built-in starter scores ~3,500 for reference)

Five engine details that cost me the most time
The shed is not a tile. It is the four centre squares — (4,4), (5,4), (4,5), (5,5). DROP and PICKUP only work while standing on one of them. My first agent searched the grid for a tile of kind SHED, found none, and walked to (0,0) for 720 turns.
SELL only spends from the shed. HARVEST puts produce in the unit's inventory, so anything not carried back and dropped is worth zero at the end. DROP moves the entire inventory in one action.
Hiring is fibonacci-priced and hires_today resets daily. Eight hands costs about $54 for the day. Gating hiring behind a cash threshold is a false economy: an unworked farm loses its plants outright, since two unwatered days kills a plant.
tiles[y][x], where None means empty and plantable, the string "LOCKED" means unowned, and a dict is a structure. BUILD_PASTURE / BUILD_COOP are free but silently no-op unless the tile is None.
Animals are bought into the shed, not onto the board: PICKUP → walk → PLACE on an empty PASTURE/COOP. And FEED consumes one WHEAT from the acting unit's own inventory, not from the shed — so somebody has to be carrying wheat when they reach a hungry animal.
Where I am
Rating is still settling after a handful of games, so I make no claims about ladder strength. Three things I know I am leaving on the table: my hand count drops to zero mid-game in the logs, I grow no animals at all (forgoing daily milk/wool/fertilizer), and I do no market timing whatsoever.

Question for anyone further up: does livestock actually beat a pure crop economy once execution is clean, or is its real value that fertilizer gives you income from day 2 while the melons mature? I can see the argument both ways and have not tested it properly.


Bovard Doerschuk-Tiberi · 9023rd in this Competition · Posted a month ago
·
Kaggle Staff
Small balance change
I'm adding a small change to eggs, tomatoes and carrots, such that their price will increase significantly if there is a large shop demand and no production.

Since the shop demand is randomized, each of these products will start to see the levels of prices increases (assuming NO production):

tomatoes => 50% of games
carrot => 26% of games
eggs => 22% of games
The intent of these changes it to roughly preserve the existing market dynamcs, but make these products viable in some situations, not universally. This should lead to more interesting end game decisions.

Details here: https://github.com/Kaggle/kaggle-environments/pull/1399

This should be the last change, excepting game breaking bugs.

This should roll out shortly. You should update to >=1.32.7

Happy Kaggling!


14

2

1
7 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Georgy Mamarin
Posted a month ago

· 863rd in this Competition

A population-level follow-up to destbreso's measurement, from the other end: what the ladder actually did with the change. I split 37,343 public episodes - 74,686 seat-games, two agent seats per episode - by each replay's module_version (the engine_version column of the dataset), windows split by version, not by date. Short version: the field repriced carrots within a day, nobody picked up tomato, and the new scarcity payouts are not showing in banks yet.

The rollout itself, measured: the PR went public Aug 14 at 02:38 UTC, and on Aug 15 the merge, the PyPI upload and the ladder cutover all happened inside 17 minutes (01:24, 01:35, 01:38-01:41 UTC - last 1.32.6 game, first 1.32.7 game, nothing in between).

Realized price ceilings (per-episode price_<good>_max):

carrot: never exceeded 43 in any of 50,220 pre-patch seat-games (median per-game max 42); post-patch median 57, p90 116, p99 360 - 82% of games clear the old all-time ceiling.
tomato: p99 128 -> 786; seat-games above the old p99 went 0.8% -> 29.8%.
egg: p99 84 -> 167; 0.8% -> 9.4% - weakest of the three, matching destbreso's read.
melon is the clean control: identical at every checked quantile (272/272/272 at median/p90/p99, max 274) in both windows. Wheat's tail actually shrank (p99 56 -> 53) - consistent with the meta shift below, not with any global price drift.
What the field did: carrot planting went from 6.3% to 44.2% of seat-games. The paired evidence says resubmission, not adaptation: of 332 submissions with at least 3 games in each window, zero flipped whether they plant carrots or tomatoes (frozen code stays frozen); among submissions that debuted after the cutover, 60% plant carrots versus 12% for pre-window debutants. The switch started before the switch: carrot share was already a quarter of seats on Aug 14, the day the PR went public (with a smaller rise on Aug 12-13 I cannot attribute). Tomato, whose realized ceiling moved the most in absolute terms (max 1,803), was not adopted: 0.7% -> 1.0%.

Banks are the honest null. The across-all-teams median moved +4.6%, but the pre-window generates the same drift internally (+3,939 from Aug 8-10 to Aug 12-14), and for the 723 teams with at least 5 games in both windows the per-team delta collapses to +610 coins (373 up, 350 down - a coin flip; p=0.41). Tails opened less than the median: bank p90 +2.2%, p99 +2.0%, and the single-game maximum actually fell. Either the spike money is not being captured yet, or it is competed away as fast as it appears; bank data cannot tell these apart. One outcome did move: the median winner-loser bank gap narrowed from 6,810 to 4,454 coins (533 of 723 paired teams narrowed, p~1e-38) while the matchmaking rating gap stayed flat (daily medians 36-45 in both windows) - either the carrot floor compressing outcomes, or the meta converging on the same carrot line; I cannot fully separate the two.

Everything above splits on the engine_version column in kaggriculture-episodes, one line of pandas to slice differently.


Reply

1
Forrest
Posted a month ago

· 222nd in this Competition

Maybe you should update README.MD


Reply

React
Bovard Doerschuk-Tiberi
Kaggle Staff
Posted a month ago

· 9023rd in this Competition

README and "How to play" page updated


Reply

React
destbreso
Posted a month ago

· 1058th in this Competition

I reproduced the firing rates independently, and they land where you said. Reading market["inventory"] every turn across 120 recorded episodes replayed with both seats playing their own recorded actions, so no agent of mine in the loop, games cross the new knee for tomato 55.0 %, carrot 28.3 % and egg 25.8 % of the time, against your 50 / 26 / 22. Melon is a useful control: untouched by the change, in no shop menu, and its deepest scarcity across those episodes is 11 units against a knee of 300, so it crosses 0 of 120.

The stated intent also checks out, and I think this is the more interesting half. Median scarcity sits just below each new knee, 219 against 200 for tomato, 316 against 450 for carrot, 228 against 332 for egg. So the median game is almost exactly the old game: dumping 100 units at median scarcity pays 1.00x the old revenue for tomato and egg to the dollar. At p90 it is about 2x, and the large multiples only appear in the deepest game of the 120. "Viable in some situations, not universally" is what the numbers do.

Two notes that might be worth a line in the PR description. Carrot's below_target also moved, 0.20 to 1.00, which the post does not mention and which lifts its curve below the knee as well as past it. And on my measurements egg does not reach the money at any percentile short of the deepest game, 1.00x at the median and at p75 and 1.06x at p90, so of the three it is the one where the change may not do what the firing rate suggests.

Also worth saying for anyone worried about their existing work: recorded episodes have both sides fixed and replay identically on either build, 40 of 40 banks to the dollar in my checks. Holding agent, seed and opponent fixed and switching only the build moved 118 of 224 banks and changed 0 of 224 winners.

The same shape shows up in the closed-form ceiling on total money in an episode, which is a sum over market_price and so re-derives itself on any build: on 1.32.7 it moves 0.2 % at median demand and 9.7 % at the most generous shop draw in 120 seeds, with no episode of 32,570 above either. Median untouched, tail opened, again.

One consequence for anyone tuning against a target rather than against wins: a change that adds nothing to the median and a lot to the tail is a dispersion change, and dispersion and expectation point different ways depending on whether you are ahead or behind. The argument for why the objective here is Pr[win] = Φ(μ/σ) rather than expected margin is in Wins, not money. Happy to publish the reachability measurement itself if it would be useful.


Reply

React
Raymang0
Posted a month ago

· 1115th in this Competition

I like that the rules have changed over time, it has made the game more balanced for sure. But it would be interesting if there were a reward for top players for a given rule set, so compute isn’t seen as wasted


Reply

React
alex chilton
Posted a month ago

· 558th in this Competition

r u havin a laugh - people use compute to tune a lot then you just pull the rug on it…? a little thought might be in order - thats the third long run changed…


Reply

React
VynoDePal
Posted a month ago

· 3279th in this Competition

Good update. But please, Make it possible to buy them in town. At least one.


DILIP BAVISKAR · 9316th in this Competition · Posted a month ago
Reward Calculation in Kaggriculture
I am facing very common situation , my agent starts with -ve reward due to land purchase. How should we interpret land /animal purchase , reward or expense. Because this is important from context of earning rewards. I understand land /animal purcahse should be treated as reward but want to understand how scoring will be calculated during evaluation.

Additionally any crop planted in field ( matured on very last day of episode i.e. 30th day) , should be treated as reward or no value if not sold. If you retain shed , it should be treated as reward or expense only at the end of episode ? Or to get reward we have to sell /destroy shed ? Please clarify , these are important points to decide strategy.

Please clarify on this.


React
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Bibek
Posted a month ago

The only thing that matters for your score is your final cash balance at episode end, meaning every purchase is an expense that must be recouped through sales, and any unsold crops, animals, or structures at the end are worth absolutely nothing.


Reply

React
DILIP BAVISKAR
Topic Author
Posted a month ago

· 9316th in this Competition

are u sure of this ?


SZU蓝心 · 3482nd in this Competition · Posted a month ago
Which version got the final rating?
We can make five submissions each day and keep two of them active. But which one will be used for the final scoring? This is my first time joining an agent competition, so I'm not really familiar with how it works.


React
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
kirito83
Posted a month ago

· 419th in this Competition

last two of all your submissions


Reply

React
VijaiKurianMathew
Posted a month ago

· 3061st in this Competition

The Setup (like a chess ladder) Imagine a chess club with 6,000 players. You don't play everyone — you get matched against players near your skill level. Win → your rating goes up. Lose → it goes down. That's the ladder, and your rating is your score. Your bot plays ~100 games automatically over 3 days. That's how it earns its rating. The 5-per-day, 2-active rule

5 submissions/day = you can upload a new bot version up to 5 times daily. Think of it like: you can register 5 new players per day.
Only your latest 2 stay on the ladder. Upload #3? It kicks upload #1 off. Your two newest bots are the only ones playing games and earning rating.
⚠️ The trap: every new upload starts at rating ~600 (bottom). It takes 72 hours / 100 games to climb to its true strength. So uploading carelessly throws away a climbing bot.

Which one counts for final scoring? Here's the key thing for sim competitions: there is no "pick your final submission" button. Your final leaderboard position = whichever of your 2 active bots has the best rating when the deadline hits (Sept 30). So "final scoring" = the last snapshot of the ladder. If your two active bots are rated 2700 and 2500, you're ranked as if you were the 2700 player.

Your Strategy (what we're already doing)

Treat each submission as a 3-day investment. Don't upload unless it's a genuinely better bot (proven in local testing) or a fix.
Keep both slots occupied by your strongest bots, uploaded at staggered times so they're never both re-climbing at once.
Freeze experiments by Sept 23. Final week = no new code, just let ratings converge. Maybe one deliberate re-roll of your single best bot if it stalled.
By Sept 30: your 2 active slots should hold your 2 best agents, both fully converged (~2700+).
One-liner: Upload rarely, only better bots, let them climb, and make sure your 2 most recent uploads are also your 2 best bots when the clock runs out.


Rahul Balakrishnan Adhi · 6293rd in this Competition · Posted a month ago
Regarding Deadline
It says deadline is 24th September but if we look at the timeline, it is mentioned that the final submission has to be done before 30th September so which is it?


React
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Addison Howard
Kaggle Staff
Posted 25 days ago

· 556th in this Competition

The Entry deadline is when you must sign up for the competition and accept the rules. The submission deadline is when your final submissions must be made by.


Reply

React
Will
Posted a month ago

· 1008th in this Competition

The 24th September deadline is for team merge I think.


Rustam Bazarbayev · 1031st in this Competition · Posted a month ago
How many days need to ensure your agents score?
How many days are needed to ensure your agent's score remains stable?How many days need to ensure your agents score is stable?


React
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
destbreso
Posted a month ago

· 1059th in this Competition

The measurement that works for me is in episodes rather than days, because the episode rate is not constant. Across four of my own submissions it ranged from 0.7 to 7.2 episodes per hour, a factor of ten, so one day was about 17 episodes for one agent and about 170 for another. Wall clock and evidence are only loosely related.

So I sample the pair (episodes completed, score) and look at the drift in points per episode:

def convergence(samples, threshold=1.0):
    """samples: (episodes_completed, score) for ONE submission, in time order."""
    steps = [(s2 - s1) / (n2 - n1)
             for (n1, s1), (n2, s2) in zip(samples, samples[1:])
             if n2 > n1]                       # <- the important filter
    if not steps:
        return None, 0, False
    drift = sum(steps) / len(steps)
    flips = sum(1 for a, b in zip(steps, steps[1:]) if a * b < 0)
    return drift, flips, abs(drift) <= threshold and flips >= 1
Two subtleties in those few lines, and both changed my answers when I had them wrong.

The if n2 > n1 filter matters more than it looks. The leaderboard updates in batches, so most probes come back with a new timestamp and the same episode count: on one of my series, 31 of 36 probes showed no new episode. Keeping those averages a lot of zeros into the drift and makes a rating that is still moving look converged.

And the series has to be keyed by submission id. Tracking "my best submission" instead will eventually compute a delta between two unrelated ratings and divide it by a difference of unrelated episode counts, which is not a quantity that exists.

The part I find genuinely interesting is that "stable" may not be the right target at all. A rating measures you against the field of that moment, and the field turns over, so the number moves even when the agent cannot: I have one that fell 182 points over 135 episodes while byte-identical. That makes two readings of the same agent taken days apart non-comparable, and it means comparing two of my own agents only works when both are live in the same window.

I wrote the whole thing up with the code and four real sampled series here, in case it is useful: https://www.kaggle.com/code/destbreso/rating-convergence-episodes-not-hours


Reply

1
VijaiKurianMathew
Posted a month ago

· 3061st in this Competition

~3 days / 100 games (70% in first 6h, flat after 24h).

Full EDA + tiered holds here: https://www.kaggle.com/code/vijaikm/kaggriculture-score-convergence-2026

— upvote if it helps you time your next submit!


那个男人 · 1153rd in this Competition · Posted a month ago
RL seems to have a very low ceiling and is extremely prone to noise interference.
Right now, using BC can reach a medium level, but adding PPO and trying more BC data actually makes things worse. Solving the noise in RL learning seems to be a big issue at the moment. Not sure if anyone has successfully used PPO or other methods before. …


React
6 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Paritosh Kumar Tripathi
Posted a month ago

· 1158th in this Competition

Almost all past agent competitions' top solution were RL based. Maybe something wrong with the rewards in PPO.


Reply

React
EUGENEYEUNG
Posted a month ago

· 605th in this Competition

I think a rule-based approach is still the best solution at this point


Reply

React
Wiz
Posted a month ago

· 3709th in this Competition

yes rn top lad are all heuristic. but when the compt get into latter stages, if aiming for top it could be good to try fine tuning wiht rl. look at past competitions.


Reply

React
yuanzhe zhou
Posted a month ago

· 1368th in this Competition

What do you think are the noises? I have no idea yet.


Reply

React
那个男人
Topic Author
Posted a month ago

· 1153rd in this Competition

Right now, for me, atomic action BC tends to perform poorly due to error accumulation. High-level BC works moderately well, but both end-to-end PPO and high-level PPO are quite bad. I'm currently looking for solutions too.


Reply

React


liuhc1017 · 3785th in this Competition · Posted a month ago
Evaluation time longer
Recently, I've realised that the competition evaluation takes longer, the agents are matched up only every hour or so even though the agent is still always winning. Previously, the agents were almost always playing matches.


React
9 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
kay.liechtenstein
Posted a month ago

· 188th in this Competition

Seems that the match frequency declines to ~twice per hour after 4 hours from submission, while before this point the match happens almost every ~4 minutes.


Reply

React
dzjiann
Posted a month ago

· 1108th in this Competition

I submitted an agent that, in local testing, can beat all the public notebooks with a win rate of over 55% against each one and an average win rate above 75%. However, it’s been almost a full day, and its score is still only 1900.


Reply

React
nofreewill42
Posted a month ago

· 1131st in this Competition

try submitting it again a few times


Reply

React
Michael Timbs
Posted 24 days ago

· 1326th in this Competition

a couple of unlucky losses can really derail the climb once the volume drops. Very sensitive to outliers once you get above the 2400 mark


Reply

React
brightest66
Posted a month ago

· 1289th in this Competition

Oh my goodness, I kept thinking my strategy was just not effective enough, yet I didn’t want to waste my five daily submissions.


Reply

React
liuhc1017
Topic Author
Posted a month ago

· 3785th in this Competition

Its quite impossible to use up five submission in a day, but they only grade the latest 2


Reply

React
Marko Rupnik
Posted a month ago

· 2195th in this Competition

They have probably shifted compute to the Pokémon competition final evaluation period. I might be wrong though!


Reply

React
liuhc1017
Topic Author
Posted a month ago

· 3785th in this Competition

Possible, hope this improves when the pokemon competition ends.


Reply

React
c-number
Posted a month ago

· 1960th in this Competition

The pokemon competition had a similar problem during Orbit War's evaluation period. There, the frequency of matches recovered when Orbit War ended.



Yan Zhou · 38th in this Competition · Posted a month ago
Any High-Ranking Entries Using RL?
I started following this competition pretty recently, so I’m not too familiar with the current leaderboard. Are there any high-ranking entries using RL-based methods?


React
7 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Rishi Gottumukkala
Posted a month ago

· 1075th in this Competition

Nope purely heuristics for now, I’ve got plans to work on RL though


Reply

2
Rishabh Shetye
Posted a month ago

· 3627th in this Competition

I am new too, didnt spend much time going over it, but from what I can see is that entries involving very specific methods definitely have used RL to find optimized initial states.


Reply

1
NNMax
Posted a month ago

· 675th in this Competition

I'm not using RL on my submissions (for now)


Reply

1
Michael Timbs
Posted a month ago

· 1327th in this Competition

You can just download all the episodes from top of the leaderboard and see they are all basically fixed policy and all from the same pool of moves. Every day or two there seems to be a new lineage of the 720 moves but within 24 hours everyone converges on it again with a few alterations.


Reply

1

1
Ricky
Posted a month ago

· 887th in this Competition

I'm not using RL.


Reply

1
fufufukakaka
Posted a month ago

· 1611th in this Competition

Without RL now


Reply

1
Rustam Bazarbayev
Posted a month ago

· 1031st in this Competition

Without RL you can reach to 2400+.


Krzysztof Gonia · 4028th in this Competition · Posted a month ago
Does intentionally placing impossible tasks to make replays harder to copy count as unfair play?
I noticed in some replays that agents, either because of imperfect implementation or possibly on purpose, submit orders that cannot be fully executed. For example, trying to buy 3 animals when only 1 can actually be bought.

Would intentionally submitting such orders to make the replay harder to copy be considered unfair play, even if it does not change the actual game outcome compared with a normal implementation?


2
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Michael Timbs
Posted a month ago

· 1327th in this Competition

its just very hard to get a model that only plays legal moves. much easier to get one that is robust to illegal moves


Reply

React
nofreewill42
Posted a month ago

· 1131st in this Competition

everyone's trying to eventually just end up higher on the final leaderboard I guess, so I don't think that making your solution harder to copy while you also just wanna see how you perform on the leaderboard is unfair


nofreewill42 · 1130th in this Competition · Posted a month ago
Claude Code
It's so different and fascinating to work on a kaggle comptition with AI than it was a few years ago without it. I would have stopped a "long" time ago thinking about and work on this competition (long time lol, i started yesterday:D) but … just telling it the strategy and it produces me an html and i can just look at whats going on and just ahh … :D

at the same time its soo annoying when it just doesnt get it and i have to explain. but i mean, i would not even be here without it so…

any thoughts? we are probably gonna be living in weird times pretty soon so any thought is welcome


React
11 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
stnick
Posted a month ago

· 2974th in this Competition

I’m the same. Just started participating in kaggle comps to test out the models.

I’m finding claude is good at coming up with grand plans, but implementation is riddled with bugs that codex is great at finding. Codex is extremely detail oriented, in contrast to claude, which makes it good at running experiments but quite annoying when you want to try out vastly different ideas b/c it just will not make a big leap.

I was also pleasantly surprised by gemini 3.7 fast today - it is seriously fast, though a bit sloppy in implementation like claude


Reply

React
Wiz
Posted a month ago

· 3708th in this Competition

could try grok in cursor. its both great in making leaps and implementation.


Reply

1
Dread Development
Posted a month ago

· 4408th in this Competition

So I’ve not entered into this specific comp yet (will be shortly) From the competitions I have, it’s a game changer for sure ! Being able to send out a whole slew of AI allows me to focus on specifics and not have to dump tens of hours into researching.

I’ve learned to not just trust blindly & am now utilizing several different models & forcing adversarial fact checking.

Has been working very well, currently participating in 18 different comps & alone that would not be possible !


Reply

React
nofreewill42
Topic Author
Posted a month ago

· 1130th in this Competition

How do you manage that many competitions? I can barely manage this one alone :!


Reply

React
Dread Development
Posted a month ago

· 4408th in this Competition

Look I’ve got a whole team of Agents running around… Claude Code is my main, with a secondary Claude code in CLI & Codex so on average I have 3-6 agents working 24/7/365


Reply

1
nofreewill42
Topic Author
Posted a month ago

· 1130th in this Competition

I mean there is a lot of nuances that CC just doesn't wanna go there on its own, I have to guide it a lot to get something actually done. It's still a lot of work, but at least I'm doing it..

i just have to tell it to implement things in cpp and cuda to make things faster and it just does it lol


Reply

React
qihuaz
Posted a month ago

· 2780th in this Competition

LOL same feeling here.

I wouldn't be joining this competition without AI assistance. These competitions are very draining and exhausting. With ai I can focus more on the strategy part and not the coding part.

That said, my three days experience with CC so far is very frustrating. Jeez it is very bad at making strategic decisions, often fight and push back my proposal with ungrounded invented theory.


Reply

React
Dread Development
Posted a month ago

· 4408th in this Competition

What has worked for me, is having a secondary set of agents go re confirm or deny deterministically.

Having a second set has saved me a lot of headache!


Reply

React
FBadger
Posted a month ago

Joined this competition to play around with a few things and try them in practice, including AI assistance. Would not have done it without it. The amount of coding required for analysis tooling alone would have sucked out all the fun.


Reply

1
nofreewill42
Topic Author
Posted a month ago

· 1130th in this Competition

I am playing around with RL right now, trying to make a much much smaller problem and see what it comes up with. Based on the findings I guess I'll have to come up with a curriculum or sth.


Reply

React
Wiz
Posted a month ago

· 3708th in this Competition

whcih claude model r u speaking to. prob not opus right. btw, could try grok in cursor. its both great in making leaps and implementation.


Reply

React
nofreewill42
Topic Author
Posted a month ago

· 1130th in this Competition

it was opus but i realized codex is much better to work with

Georgy Mamarin · 871st in this Competition · Posted a month ago
The Daily Top Episodes dumps and my API-crawled corpus stopped overlapping on Aug 9 (measured)
The Daily Top Episodes index and the corpora people build through the episode API (competitions.EpisodeService/ListEpisodes) look like two routes to the same games. I measured mine against them, and since Aug 9 they share no games at all.

Method: dump files are named by episode id, so kaggle datasets files gives each day's id list without downloading 20 GB. I intersected all 22 dumps (Jul 30 through Aug 20, 16,031 unique episodes) with an API-crawled corpus of 47,351 episodes (kaggriculture-episodes, collected nightly since early July).

dumps	episodes	shared with my corpus
Jul 30	864	726 (84%)
Jul 31	928	206 (22%)
Aug 1-8	5,939	231 (4%)
Aug 9-20	8,300	0
The middle band is not smooth, to be clear: Aug 1-3 were already zero, overlap flickered back on Aug 4-8 (190 of the 231 came on Aug 5 alone), and died for good on Aug 9. Twelve dumps in a row since then with zero shared ids.

Scale first, because it surprised me: Meta Kaggle's Episodes table says this ladder plays about 140,000 Public episodes per day. Every corpus in this thread is a sliver of that. The dumps hold ~700 games a day (0.5%); my crawl indexes 800-4,000 a day (0.5-3%), rate quota permitting. On Jul 30 those two slivers coincided: 84% of that dump sat in my corpus. Since Aug 9 they are disjoint.

Zero is not what a coincidence looks like here. If the dumps were drawn independently of my crawl's slice, the expected number of shared episodes over Aug 9-20 is about 147 (per-day dump size times my per-day count, divided by the day's ladder volume, summed); observed is zero. Independence is the assumption to poke at: if the dumps' top-rating rule and my quota-limited, recency-first crawl pick anti-correlated slices, the true expectation drops. But it would have to be driven essentially to zero to explain twelve straight days of nothing, and this same crawl shared 84% of the Jul 30 dump and 190 ids with Aug 5's, so the two selections were not separated by design. My crawl was also alive and dense in the same id space: the Aug-12 dump spans ids 92,138,670 to 92,472,865, and my corpus holds 3,477 episodes inside that exact span, almost all ending Aug 12. (Episode ids are global across Kaggle, so a span can also contain other competitions' games.)

Where the dump games do exist: all 16,031 dump ids are present in Meta Kaggle's Episodes table as ordinary Type=Public episodes of this competition (as are all 777 of my Aug-20 ids, the control), and the replay CDN serves the ones I spot-checked like any ladder game (a made-up id 404s). They are real ladder episodes. The 8,300 from Aug 9 on just never appeared in any ListEpisodes response my crawl collected, nor in full fresh queries of three submissions, including both teams from the game below.

One concrete case: the Aug-20 dump has episode 94735084, Michael Timbs vs lucaskna, a complete 720-step game on engine 1.32.7. ListEpisodes for the latest submission of each team that I can query returns games through Aug 16 and Aug 19 respectively, nothing on Aug 20, and no dump ids anywhere. The endpoint rejects teamId, so I cannot ask about a submission my roster never met (at least one of the two teams plausibly resubmitted). The 147-vs-0 arithmetic above does not rest on this one case.

The pinned Daily Top Episodes thread describes the dumps as each day's episodes ordered by average agent rating, which I read as sampling the same pool the API lists, and on Jul 30 the numbers agreed with that reading (84%). They broke on Aug 1, flickered on Aug 4-8, and died on Aug 9. @bovard, did the dump selection or the episode listing change around Aug 1, and again around Aug 9? Is there a slice of the ladder that per-submission ListEpisodes does not expose, and if so, how are the dump episodes drawn from it?

Practical consequences, each scoped to what I measured:

The dumps and my API-crawled corpus are complementary since Aug 9: the dumps add ~700 episodes per day of top-rated play that my crawl never reached. If you do imitation learning / behavior cloning (IL/BC), that is the slice you want.
Merging the two needed no dedup for recent weeks against my corpus (zero shared ids), but does need it against the Jul 30 - Aug 8 dumps: 1,163 episodes sit on both sides. Your crawl may differ; the snippet below checks yours.
Since Aug 9 there is no episode-level leakage between "train on dumps" and "evaluate on my API-crawled corpus". At least some of the same agents play on both sides, so distributions overlap; the games themselves do not.
Neither source is anywhere near the full ladder (the dumps are 0.5%, my corpus 0.5-3% of ~140k games a day), so treat both as biased samples of the meta, not the meta itself.
The three dump replays I opened (Aug 9, 15, 20) all carry module_version like any replay (1.32.6, 1.32.6, 1.32.7), so they split by balance patch the same way.
Reproduce against your own ids:

kaggle datasets files kaggle/kaggriculture-episodes-2026-08-20 --page-size 200
# filenames are the episode ids; take "Next Page Token" from each response and
# repeat with --page-token until it runs out - four pages cover the day
Code that reads the API-side corpus is in What 2600+ Farms Do Differently.


Tommy Mancino · 3620th in this Competition · Posted a month ago
Discussion of the education value of my Kaggle experience.
I wanted to share and discuss the educational value of Kaggle challenges. My ego is as large as everyone's, so I was disappointed in my recent Pokémon experience, but not deterred. While I am currently luckily doing well in this game (which may or may not last), I do know I have learned a good amount, which is really the point (unless you are a good enough/professional ML researcher to consistently win money), most importantly:

1) the importance of tooling and measurement - I now have an entire custom agent harness that ensures my agents (all created with various AI tools) are composable, and each new submission candidate is validated in multiple ways before being submitted. This includes a token authorization system (for the time I randomly used all my submissions ;( ). The time I lost because of this in the past is measured in weeks, not days! Additional tooling around speeding up the Kaggle harness, etc. to improve testing/training throughput. Write things that you can re-use in future challenges.

2) Striving to understand the underlying ML processes/techniques and when and why to use each. This was a big 'win' for me so far, as I took the experiences from the Pokemon competition and applied them to this challenge. I quickly realized BC wouldn't work the same way (everyone was correctly scripting at first), so I adjusted my approach.

3) Not getting locked into a short-term gain but focusing on the endgame win conditions - without getting overly locked into a particular approach. In this game, I think it is/was possible to just copy scripts from top players and do well via optimzation, but I don't think that will hold the entire competition as well (although may do better than other games with more RNG) I have been using GA to great effect, as this game has no hidden information (outside the contents of the opposing player's barn - but even that is easily predicted), and very few random effects (weeds/town buildings).

4) Writing a composable harness system that can be reused between challenges saved me a lot of time and hardship (see above). I wanted to remind myself that no matter how well or poorly I am doing, I am learning a ton. I have never had a CS class in my life, and failed high school math ;) That was a long time ago, but the advent of coding agents that use English as the primary programming language has opened up a world of fun and learning. Congratulations to everyone here for taking advantage of it. I only wish I were 20-something again!


1

1
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
KiZins
Posted a month ago

Thanks for sharing! Good luck in the rest of the competition!


Foodle Jang · 8716th in this Competition · Posted a month ago
RL model release (working link)
github link -> https://github.com/diffmap/kaggicultureRL

For the beginners interested in RL


dzjiann · 1110th in this Competition · Posted a month ago
Inferring Opponent Inventory Quantity and Uncertainty from Public State — for Quantitative Trading Factor Modeling
I tested whether opponent inventory can be inferred from Kaggriculture's public state and used as an additional quantitative trading factor.

For commodity i, let

S_i : total loose stock of both players M_i : public market inventory H_i : public production / harvest C_i : observable consumption D_i : deterministic town consumption F_i : sales hidden by the $1 price floor L_i : private loss (DROP / overflow)

Then

ΔM_i = sell_nonfloor_i - buy_i - D_i

ΔS_i = H_i - C_i + buy_i - sell_all_i - L_i

so the player-specific trades cancel:

ΔS_i = H_i - C_i - (ΔM_i + D_i) - F_i - L_i

and therefore

opponent_total_i = S_i - own_total_i

The point estimator uses F=L=0; uncertainty bounds are widened when floor selling, overflow, DROP, or ambiguous farm transitions make the state non-identifiable.



Some commodities are almost fully recoverable:

CARROT MAE 0.008 TOMATO MAE 0.000 EGG MAE 0.000

MILK/WOOL are much noisier because concentrated selling can hit the $1 floor, after which stock can leave private inventory without appearing in market.inventory.

This is a genuine identifiability issue, not just estimator error. Shed vs carried inventory, DROP/overflow, price-floor sales, and some end-of-day transitions cannot always be uniquely reconstructed from public state.

For an ML trading policy, I think the useful features are therefore not just

opponent_inventory_estimate

but something closer to

opponent_inventory_estimate lower_bound upper_bound uncertainty_width floor_risk private_loss_risk

per commodity.

So the hypothesis is straightforward: estimated opponent supply + estimation uncertainty may provide useful quantitative trading factors beyond price and public market inventory alone.


Rayk Kretzschmar · 1790th in this Competition · Posted a month ago
How path dependent is the current leaderboard rating?
I submitted two byte-identical agents approximately two hours apart. The first submission is currently around 1700, while the second, submitted 2h later, has climbed >3000. Because the submitted code is identical, this difference appears to come from matchmaking, seeds, player positions, and the order of early results, not agent quality. In particular, early losses seem to make subsequent climbing extremely slow.

A gap of roughly 1400 points between identical agents suggests that the current rating may be highly path-dependent, especially during the initial games. It may even incentivize repeatedly submitting the same agent in hopes of receiving a better early trajectory.

Has anyone else tested duplicate submissions or observed similar rating divergence? Does the rating system eventually converge given enough games?


React
9 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Rayk Kretzschmar
Topic Author
Posted a month ago

· 1790th in this Competition

I want to add that this is especially frustrating when an early loss happens because of a random weed spawn that only affects the own side. If early results strongly influence the subsequent rating trajectory, a single piece of bad RNG can have an outsized and persistent effect.


Reply

React
Victor Mercklé
Posted a month ago

· 3521st in this Competition

In particular, early losses seem to make subsequent climbing extremely slow.

I think this is the biggest factor. It was less an issue when any new agents you'd submit would beat everyone except the top1. Now with more randomness it shouldn't be possible. You can measure how many hours you need to reach top1 by winning every game.

Also a big part of the pool currently is stale agents (for the old engine).


Reply

React
evnchn
Posted a month ago

· 4015th in this Competition

Also a big part of the pool currently is stale agents (for the old engine)

Indeed, those are dropping out as we speak.

I wonder if all-reset-to-600 is more productive when a patch lands like https://www.kaggle.com/competitions/kaggriculture/discussion/735311 than leaving stale entries in the leaderboard to linger.

One might argue that increases the cost to a patch, but I'd say that's just the cost of a patch you're paying implicitly over the span of 14 days so it seems less impactful to issue the patch but doesn't mean the underlying impact isn't there to begin with.


Reply

React
Steve421471
Posted a month ago

· 532nd in this Competition

I think we're starting to develop a stratification problem. Last week I would submit an agent and it would win 30 matches in a row and break into the top 50 in 4 hours. Now I have agents that could compete at the top but are too specialized and can't win enough to get there. It'll be interesting to see where things go from here. I've not done a 2 identical agent experiment, but I do submit 2 at a time and the one I think is stronger sometimes ranks much worse.


Reply

1
destbreso
Posted a month ago

· 1054th in this Competition

I've been digging into this question, and I think the answer could be more nuanced than simply saying that the leaderboard is path-dependent.

My research suggests that the competition does not behave like a collection of independent players submitting isolated agents. That part is actually fairly obvious from simply observing the matches. What is less obvious is how those interactions shape the leaderboard and the dynamics that emerge from them.

Some of the things I've been able to observe are:

Emergent behavior from "interspecies" interactions: agents don't evolve in isolation. Their performance and adaptation are shaped by the population they repeatedly encounter.
A natural drift in results: an fixed agent can tend to move backward in the leaderboard over time, even without any change to its own code, as the surrounding population changes.
Reproduction and mutation: agents appear to be copied and adapted, creating lineages that can sometimes be traced through their replay behavior.
Strong specialization at the top: the dominant agents are highly specialized, but they don't appear to emerge from nowhere. They continue to operate on top of some underlying baseline that can often be traced back through their lineage.
I've written up some of this analysis here:

Dissecting the Top Two
A DNA Test for Agents
Mutants at the Top: Genetic Potential of a Replay
The Leaderboard Is a Habitat Gradient
So, regarding the specific observation of two byte-identical agents diverging by ~1400 points: yes, I think this is very plausible, but I would interpret it less as noise in the rating system and more as a consequence of the population dynamics and matchmaking path.

One analogy I've been using is that of a habitat. Imagine two genetically identical lions with exactly the same capabilities. One is born on a large grassland with abundant prey and a path to increasingly favorable territory; the other is born on an island separated from that ecosystem by a lake. The lion on the island may be just as capable, but it may never reach the same fitness; not because it is a worse lion, but because the path available from its starting point does not allow it to reach the same region of the landscape.

I think something similar may be happening on the leaderboard. An agent can have the same underlying "genetics" as a highly ranked ancestor, yet fail to reach that ancestor's rating because the sequence of opponents and results it encounters puts it in a different part of the landscape. Once the surrounding population adapts, some paths become effectively inaccessible: the agent may no longer have the adaptations required to cross into the next favorable region of the leaderboard.

In that sense, the leaderboard is not just measuring an agent's intrinsic strength. It is also recording the trajectory through an evolving ecosystem. Two identical agents can therefore start with the same potential but end up in very different places because they entered the habitat through different paths.

The more interesting question, in my view, is not whether the rating is path-dependent, but how much of that path dependence is generated by the evolving ecosystem of agents itself. My current evidence suggests that this appears to be a significant part of what we're seeing


Reply

React
evnchn
Posted a month ago

· 4015th in this Competition

Another issue which the path-dependent leaderboard rating causes, is all the false "this notebook gets a 3k score" in the Code section, which is wildly over-claimed.

And that's with me already putting aside the fact that, had everyone used that same notebook, then nobody gets 3k.


Reply

React
evnchn
Posted a month ago

· 4015th in this Competition

Very. IMO the initial few matches should not have such high weight.

I have a gap of 300 for identical agents, don't have as big as 1400, but the ideal, assuming a well-tuned ELO matching algorithm, should be a gap of 0 within reasonable time.

My approach to try and self-improve is to look at the rate of change of the part after the initial rush. It's not good that the competition now needs a proxy-metric to go forward. However, I do see compute-bound being the limiting factor here.


Reply

React
evnchn
Posted a month ago

· 4015th in this Competition

Under the current leaderboard system, there can exist (though I wish not to point fingers), a group of people who repeatedly submit before rating truly settles, gambling on the initial rush for a high rating.

The rating definitely needs more than 24/5 = 4.8 hours to settle. I've seen 3k drop into 2k over the span of 4 days.

It can be safe to assume that, unless a patch is made, that because that group of people can exist, that everything should be taken with a grain of salt.


Reply

React
Belati Jagad Bintang Syuhada
Posted a month ago

· 2642nd in this Competition

To be honest, I see no point (except for temporary satisfaction) of submitting repeatedly to get a lucky start and reach the top faster. In the end, once the competition's submission deadline has passed, all of the agents will start over from 600 ELO and have to climb back up.


Reply

3
This comment has been deleted.

Rayk Kretzschmar
Topic Author
Posted a month ago

· 1790th in this Competition

Do they start over? I read that they will "continue to run". Even if they start over completely, I think it's interesting to know if an approach is worth to keep improving or if it should be rejected. I like to iterate fast and don't want to wait a week to see where my agent ends up.


Reply

React
Belati Jagad Bintang Syuhada
Posted a month ago

· 2642nd in this Competition

At least from my past experience with simulations competition (FIDE Chess Challenge), they will reset all the players ELO to 600 after the submission deadline and rerun the whole scoring system with more games per day. It happened with Orbit Wars, and probably will happen with Pokemon TCG too, so I don't doubt that they will start over in this simulation competition.

It sucks to have to wait, but these simulation competitions take a lot of their compute resource too so this is the best that they can do.


Reply

React
Mahog
Posted a month ago

· 6960th in this Competition

They didn't do the reset with Orbit Wars if I remember correctly


Reply

React
Belati Jagad Bintang Syuhada
Posted a month ago

· 2642nd in this Competition

My bad then. If that's the case, it will most likely not reset from 600.


Reply

React
evnchn
Posted a month ago

· 4015th in this Competition

Indeed there's absolutely no point other than temporary satisfaction to repeat-submit and leverage the chance of initial win streak for a higher rating.

That rating simply doesn't belong to the agent and will be slowly removed from the agent through the span of a few days (4 days, in the case of 3k->2k agent I've seen)

If you would like to actually deliver a good agent, repeated submissions should NOT be done.


Reply

React
Temitayo Gbolahan
Posted a month ago

· 2070th in this Competition

Pokemon TCG submission deadline was few days ago, did you check if it was reset???


Wiz · 3708th in this Competition · Posted a month ago
Eligibility for Participant under 18
Hi @Bovard Doerschuk-Tiberi @Domino Weir @María Cruz ! I am a high school student, residing in China. I’m currently 17 and will be under 18 through the final submission deadline. Yet this competition sounds super fascinating and meaningful to be. It will be such an impactful thing to me to be able to take part in and compete.

General Rules 3.1 allows entry where the Competition Sponsor agrees and appropriate parental/guardian consent has been obtained. My parent is willing to provide consent.

Two questions: (1) What's the process for obtaining sponsor agreement and submitting guardian consent? Any required files or preperations? (2) If sponsor agreement isn't in place, does that affect leaderboard placement and medal eligibility, or prize eligibility only?

Happy to take this to email if that's more appropriate. Thanks!

And btw thank you for hosting such an interesting event!


React
5 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Bovard Doerschuk-Tiberi
Kaggle Staff
Posted a month ago

· 9025th in this Competition

https://www.kaggle.com/guardian-consent-minor-use and then https://www.kaggle.com/consent-minors-process


Reply

1
Wiz
Topic Author
Posted a month ago

· 3708th in this Competition

Thank you!!!!! I'll do it immediately. Super grateful~


Reply

React
Navneet
Posted a month ago

Thank you for the eligibility information. @williamzhou001


Reply

1
This comment has been deleted.

Wiz
Topic Author
Posted a month ago

· 3708th in this Competition

Thank you very much for this! alr!


VijaiKurianMathew · 3060th in this Competition · Posted a month ago
🌾 Complete EDA & Modular Agent Framework for Kaggriculture (with Market Price Elasticity Curves)
Author: @vijaikm
Tags: eda, tutorial, beginner, simulation, starter, reinforcement-learning, python, data-visualization
Notebook Links:

📊 EDA & Market Price Elasticity Analytics
🚜 Modular Agent Framework & Diagnostics Arena
Hi Kagglers,
To help everyone get up to speed with the game mechanics and build robust agents for the Kaggriculture competition, I have published two comprehensive, modular, and fully documented notebooks:

1. 📊 Kaggriculture: Complete Simulation EDA & Market Analytics
#eda #simulation #data-visualization #game-theory

This notebook does a deep dive into the mathematical mechanics and economic fundamentals of the game:

Market Price Elasticity Modeling: Formulates and visualizes the piecewise inventory index curves ($I_0 = 10,000$) across all 9 commodities. Demonstrates why Wheat absorbs massive volume gluts ($24\%$ max drop) while Melon, Strawberry, Milk, and Wool crash rapidly to the $\$1$ floor.
Crop Agronomic & Unit Economics: Compares seed costs, growth durations, watering risks, gross margins, and daily ROI ($\$/\text{day}$) across single-harvest and ongoing crops.
Livestock Payback & Care Compounding: Payback period modeling for Goose, Cow, and Sheep under daily wheat feed costs, highlighting the $+1$ care bonus multiplier.
Fibonacci Labor Wage Scaling: Visualizes the marginal vs cumulative daily cost curve of hired hands ($\text{fib}(1,1,2,3,5,8\dots)$).
Interactive Replay Trajectory Analyzer: A reusable SimulationReplayAnalyzer class to visualize bank trajectories, market sales volumes, and action distributions for any match.
👉 Notebook URL: https://www.kaggle.com/code/vijaikm/kaggriculture-simulation-eda

2. 🚜 Kaggriculture: Modular Agent Framework & Diagnostic Benchmarker
#starter #tutorial #architecture #clean-code #python

This notebook provides an object-oriented, clean architecture framework to build, debug, and benchmark agents:

Modular Single-Responsibility Architecture:
ObservationWrapper: Clean, typed dataclass parser for raw Kaggle JSON observations.
SpatialNavigator: Manhattan distance routing and obstacle-aware directional navigation.
CropManager: Maturation-aware scheduling prioritizing watering and harvesting before planting.
MarketBroker: Safe order aggregator strictly enforcing the 10 orders/turn limit and cash solvency.
"Sustainable Farmer" Baseline: A transparent, robust baseline agent that reliably beats Starter and Random bots.
Invariant & Legality Verification Suite: Automated checks for order limits ($\le 10$), action formatting, shed capacity ($\le 100$), and stateless reset invariants (step == 0).
Diagnostic Head-to-Head Arena: Evaluates agents across multiple seeds and both seats (Seat 0 & Seat 1) against built-in opponents, reporting win rates and latency distributions ($<3\text{ ms/turn}$).
1-Click Standalone submission.py Exporter: Ready for direct submission to the leaderboard.
👉 Notebook URL: https://www.kaggle.com/code/vijaikm/kaggriculture-modular-agent-framework

💬 Discussion & Questions for the Community
What primary crop rotations (Wheat vs Carrot vs Melon) have given you the highest early-game capital velocity?
How are you scheduling labor hiring across the season to avoid the exponential Fibonacci wage trap?
How do you balance inventory holding for town shop multipliers against the 100-item shed capacity limit?
Looking forward to your thoughts and feedback! If you find these notebooks helpful, please consider giving them an upvote! 🌾🚀

Exploratory Data Analysis
Beginner
Data Visualization
Python
Reinforcement Learning


istinetz · 132nd in this Competition · Posted a month ago
Am I getting this right?
This is my understanding of what is going on in this competition:

Kaito submitted a public code solution, which is pretty strong
Everyone is cloning it, and doing very, very minor tweaks then publishing again
Everyone at the top of the leaderboard are using this lineage of solutions
The solution is approximately deterministic - in that it is prerecorded, it doesn't care at all what your opponent does or what shops are open, and only has minor flex for weeds and sell order
This is performing perfectly fine, though, because the interactivity in this competition is very very limited and the stochastic elements are not very exploitable
if you open 2 random top replays, you're going to see more or less the same game
… Am I missing anything? What are we doing here?


1

2
4 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Phương Doan
Posted a month ago

· 4494th in this Competition

It is too early to conclude anything at the moment, people having an edge won't reveal their result this early.


Reply

React
evnchn
Posted a month ago

· 4016th in this Competition

This is performing perfectly fine, though, because the interactivity in this competition is very very limited and the stochastic elements are not very exploitable

More on https://www.kaggle.com/competitions/kaggriculture/discussion/734000


Reply

React
Michael Timbs
Posted a month ago

· 1325th in this Competition

That is a correct reading. Speaking as one of the people in the top who did just that (I never saw the notebook but i extracted the play directly from episode corpus). It makes getting diverse data for training by mining the leaderboard really tricky.

I think you will see some more diverse play in the coming week(s). You don't want to give too much away too early. I suspect a lot of teams are sitting on much better solutions but still iterating before submission so as not to reveal too much.


Reply

React
evnchn
Posted a month ago

· 4016th in this Competition

Well I played CTF before, and two related things which everyone remembers:

"flag hoarding" (stashing solved challenges until the end to catch others by surprise) is highly discouraged
systematic measures like "breakthrough points" (more points for earlier solves) are employed to prevent it
It is interesting that, Kaggle decided to make all agent traces public, thereby systematically incentivizing hoarding of techniques until the last day. Not sure if this is intentional, though.

However, short of making all traces private, which makes debugging hell, I can't name a mechanism to anti-hoard for such a competition… Sorry for raising a problem without a solution 🙇. Do you have any ideas?


Reply

React
istinetz
Topic Author
Posted a month ago

· 132nd in this Competition

"flag hoarding" (stashing solved challenges until the end to catch others by surprise) is highly discouraged

well, it might be discouraged, but it will happen nonetheless.

If we make the assumption that the winning solution will be a prerecorded recipe or a small set of recipes:

it is ~hard to develop a better solution
it is ~trivial to 'distill' a better solution that someone used in the public leaderboard
∴ if I do find a better solution, and publish it, it will be instantly stolen, copied, disseminated, and people will implement their own 0.1% improvements on top of it

∴ it makes no sense to publish such a solution, if you want to win. Game theory says you should keep it in secret and submit it the last hour of the competition


Reply

React
evnchn
Posted a month ago

· 4016th in this Competition

Game theory says you should keep it in secret and submit it the last hour of the competition

I agree with your conclusion, but the one-step-ahead is HMW change the game so that game theory then says one should NOT keep it secret.

Just like breakthrough points. Once you get so much point with an early solve and so little point with a late one, flag hoarding is eliminated systematically.


Reply

React
Michael Timbs
Posted a month ago

· 1325th in this Competition

I don't think this is strictly hoarding. I only gave up on self play neural networks very recently so while i seem to be on a promising track at the moment i want to wait and see on some more holdout eval. I'm hoping to submit a novel submission thats still top 10 either today or tomorrow but will have to wait and see what results say.

I imagine a bunch of other teams also really struggled with self play and probably made no progress there (or if they are it requires a lot of compute that takes time). Competition is still young


Reply

React
qihuaz
Posted a month ago

· 2779th in this Competition

technique hoarding is definitely real, but it is also double sworded. if you hoard techniques, you risk under developing your technique and be blind to its weak spot


VijaiKurianMathew · 3060th in this Competition · Posted a month ago
🌾 [Dataset Release] 500+ Competitive Match Replays & Action Trajectories for Kaggriculture (EDA / BC / Price Elasticity)
Hello Kaggriculture Competitors & ML Researchers! 👋

To help the community explore behavioral modeling, exploratory data analysis (EDA), and econometric market dynamics, I've compiled and structured a clean, comprehensive tabular dataset containing 537 complete 720-step ladder matches (over 250,000+ per-turn actions and market transactions).

🔗 Dataset Link: Kaggriculture: Match Replay Corpus & Action Trajectories (500+ Games)

📦 What's Inside the Dataset?
The dataset is partitioned into 4 clean, analysis-ready CSV files:

File	Rows	Description	Key Use Cases
matches_meta.csv	537	Final scores, winner, seat 0/1 assignments, victory margin	Meta analysis, win-rate by quadrant spawn
market_orders.csv	250,000	Turn-by-turn commodity buy/sell quantities, hire orders	Price elasticity curve fitting, liquidity modeling
farmer_actions.csv	250,000	Grid action breakdown (MOVE, TILL, PLANT, WATER, HARVEST)	Behavioral Cloning (BC), Decision Transformers
town_shop_schedules.csv	19	Base and peak demand multiplier profiles across town shops	Demand arbitration, inventory holding optimization
🚀 30-Second Python Starter Code
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load match metadata & market transactions
df_meta = pd.read_csv('/kaggle/input/kaggriculture-match-replay-corpus/matches_meta.csv')
df_orders = pd.read_csv('/kaggle/input/kaggriculture-match-replay-corpus/market_orders.csv')

print(f"Total Matches Analyzed: {len(df_meta):,}")
print(f"Total Market Orders Recorded: {len(df_orders):,}")

# 2. Commodity Order Distribution
top_commodities = df_orders[df_orders['order_type'] == 'SELL']['item'].value_counts()

plt.figure(figsize=(10, 4.5))
sns.barplot(x=top_commodities.index, y=top_commodities.values, palette='viridis')
plt.title("Commodity Sales Volume Distribution Across 500+ Matches")
plt.xlabel("Commodity Name")
plt.ylabel("Total Sell Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
💡 High-Impact Research Questions for This Dataset
Price Elasticity & Supply Glut Decay: How steep is the price depression curve for premium crops (Strawberries, Melons) compared to high-volume staples (Wheat) as market inventory grows from $I_0 = 10,000 \rightarrow I_0 + 600$?
Behavioral Cloning (BC) & Action Policy Distillation: Can a spatial ResNet / ConvNet trained via supervised imitation predict top player farm movements with $>90\%$ intent accuracy?
Quadrant Spawn Asymmetry: Does Seat 0 (NW quadrant spawn) hold an inherent expansion speed advantage over Seat 1 (SE quadrant spawn)?
📜 Feedback & Collaboration
If this dataset helps your EDA, feature engineering, or ML training pipelines, please feel free to drop an upvote and share your findings in the comments below! 🌟

Happy Farming and Best of Luck on the Ladder! 🚜🌾

Data Visualization
Exploratory Data Analysis
Reinforcement Learning

React

Midterm full evaluation
Hi, dear Kaggle team!

Is it possible that we run a midterm private evaluation simulation in addition to current ELO system?

ELO is nice, but it has some significant flaws imho


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Bovard Doerschuk-Tiberi
Kaggle Staff
Posted a month ago

· 9024th in this Competition

We won't be running a midterm eval. However if you look at posts in past competition the BT scores are usually very similar to the final ratings. The scores your submissions converge towards are a useful signal.



bruyantq · 5659th in this Competition · Posted a month ago
Farming strategies (I'm new)
Hi everyone,

I've been working on submissions for this competition, and it has been fun :). I've finally coded down most of the functions, but I'm not sure how to progress if I don't rely on manual input. Also, as you can tell by my submissions, I haven't really used any strategies, and I'm wonder what some techniques or theories at higher levels would look like.

I'm really new to all of this, so I'm open to any ideas!


React
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Thomas Tschinkel
Posted a month ago

· 243rd in this Competition

Biggest jump for me was testing locally instead of submitting and guessing:

pip install "kaggle-environments>=1.32.6"

An episode runs in about 8 seconds, so you can play 40 in a minute and actually measure a change against your last submission.

Also read kaggle_environments/envs/kaggriculture/kaggriculture.py directly, the docs disagree with the engine in places, and most of my ideas came from _process_market and _end_of_day rather than from thinking about farming.

One strategy note: the market book is shared, so ask whether an idea also helps your opponent. Anything that lifts both players prices wins you nothing.


Reply

React
evnchn
Posted a month ago

· 4017th in this Competition

pip install "kaggle-environments>=1.32.7" per https://www.kaggle.com/competitions/kaggriculture/discussion/735311

Last version


dzjiann · 1802nd in this Competition · Posted a day ago
My RL Won, But Also Failed: Two Days of Training on a 196-Core Server
I spent the last three days running reinforcement learning on a 196-core server.

In one sense, it worked surprisingly well.

After RL training, the agent could beat the public scripts with nearly a 90% win rate. Compared with the initial policy, the improvement was very obvious, and for a while I thought RL might be the key to pushing much further.

But then the improvement basically stopped.

Even after adding self-play, the agent quickly reached a plateau. More training did not seem to produce meaningfully stronger strategies.

The more interesting problem was that its performance against strong players barely improved.

Despite being extremely good at beating the public scripts, the RL agent could only reach around the top 100 at best. More surprisingly, against high-scoring players, it was actually weaker than several of my earlier approaches that were based purely on mathematical reasoning and dynamic programming.

I still think RL has potential here, but simply throwing more compute and more self-play at the problem does not seem to be enough.

Maybe the real challenge is not optimizing the policy harder, but creating a training population and objective that actually force the agent to discover more general strategies.

Would be very interested to hear how others would approach this.




React
8 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Aaweg Bhaladhare
Posted 19 hours ago

· 27th in this Competition

bro how did you get 196-Core Server….I'm so slowed by compute on 64cores🥲


Reply

React
dzjiann
Topic Author
Posted 19 hours ago

· 1802nd in this Competition

That’s really impressive—you achieved such a high ranking with so little compute.


Reply

React
DECEM
Posted 21 hours ago

· 1st in this Competition

Getting Better and Better


Reply

1
OmerZalman
Posted 2 hours ago

· 557th in this Competition

what RL did you use?


Reply

React
Gerardo Del Toro
Posted 19 hours ago

· 6506th in this Competition

Did RL approach went for a step by step micro level decisions or at a higher level policy RL? Sparse win/loss reward was enough?


Reply

React
dzjiann
Topic Author
Posted 19 hours ago

· 1802nd in this Competition

a higher level policy.spare reward is enough.


Reply

React
shiba-inu
Posted 7 hours ago

· 3720th in this Competition

Wow, so you're training with sparse…

Are you using self-play, or are you training against publicly available agents?

In my case, I've been using self-play against the current policy and its past checkpoints. My agent can reach scores close to 100k in self-play, but it still can't beat the public agents at all…


Reply

React
dzjiann
Topic Author
Posted 7 hours ago

· 1802nd in this Competition

I mix with self-play and public agents


Reply

1

1
OmerZalman
Posted a day ago

· 557th in this Competition

did you use PPO?


Reply

React
dzjiann
Topic Author
Posted a day ago

· 1802nd in this Competition

Yes, but during training I found that not reusing old trajectories from the previous rollout actually made training more stable, and the policy improved faster as well.


Reply

React
OmerZalman
Posted 19 hours ago

· 557th in this Competition

how many games did you do?


Reply

React
dzjiann
Topic Author
Posted 19 hours ago

· 1802nd in this Competition

About one million of games

game theory died years ago. just need more core and more core…

RL discussion
Can you share your experience with RL or PPO and how well it did and tips for noobs?




Yujin Cha · 1455th in this Competition · Posted 2 days ago
Six things I wish I'd known before trusting my local win rates
I spent a few days building a local evaluation setup for Kaggriculture. Most of what I learned is about measurement, not strategy: how easy it is to fool yourself with head-to-head numbers. Sharing in case it saves someone a bad submission.

All numbers come from the fast local simulator plus the community episode dataset (georgymamarin/kaggriculture-episodes). Big thanks to its maintainer, and to destbreso for the stream_hashes normalisation.

1. Outcomes cluster by seed, so 3 seeds is noise
In this game, the seed decides much more than the seat. Swapping seats on the same seed usually gives the same score pair to within a few points. So "3 seeds × both seats = 6 games" is really closer to 3 independent samples.

A concrete case: one agent scored 2/6 against a strong lineage on seeds 0–2. Adding seeds 3–5, it went 6/6 on the new ones, 8/12 overall. The conclusion flipped completely.

Rule of thumb: use at least 6 seeds, and treat the seed (not the game) as your unit of evidence.

2. Head-to-head against your current best is a trap
The game is strongly non-transitive. The public v7 shop-router lineage is a good example:

v7 vs …	result
hybrid2965 lineage	12/12 (+11k margin)
V53 lineage	0/12 (−4.9k)
2945 lineage, herd-safe family, wonderful-life family	0/6 each
If your gate is "the candidate beats the current champion", v7 can look like a champion while losing to most of the ladder. I did exactly that once. The fix that worked for me:

Build a pool per lineage, with 2 representative agents each.
Weight each lineage's win rate by how often you'll actually meet it (see #3).
Add "walls": lineages you must not lose to. Judge a wall by its weakest agent, not the lineage average. An easy sibling can hide a 0/6. That happened to me with V53 (0/6) and K0013 V46 (6/6), which share the same opening.
When I checked the weighted score against real ladder ratings, the order matched. A lineage-weighted gauntlet put hybrid (≈2640 on the ladder) far above v7 (≈1650); head-to-head alone had them the other way round.

3. Who you meet depends on your rating, so build the pool for the band you're aiming at
Matchmaking pairs you with nearby ratings, so the opponent mix changes completely between rating bands.

At 1500–1900, two lineages (the a1-t31/hack family and utils-v1) are almost half of all opponents (24% + 23%).
At 2450–2850, neither of them shows up in any meaningful way. A different handful of large public lineages dominates instead, with a long tail of small (often private) agents.
So if you tune against the opponents in your own replays, you are tuning for the band you're in, not the band you want to reach.

How to measure it (this sidesteps the dataset's replay-coverage bias):

Label each submission with its most common stream_h48 over whatever replays of it are stored. Replay coverage drops to ~0% for the newest day, but a handful of games is enough to label a submission.
Count opponents over the full episodes.csv index, filtered to your target rating band, and map each opponent submission to its label.
4. Opening fingerprints work, but the opening depends on the opponent
stream_h48 (a sha256 of the first 48 actions) is a great lineage ID. You can compute it for your local files and join them straight to ladder seats. But the opening is not always independent of the opponent.

It is independent of the seed and the seat.
But hybrid2965 plays one opening against v7 and a different one against V53 or herd-safe agents, probably because it reacts to the opponent's turn-0 market orders.
If you fingerprint every agent against a single reference opponent, you can mislabel a lineage as two different agents (I did). Fingerprint against 2–3 different opponents and keep the set of hashes.

5. A "mirror" matchup is decided by sale timing
Several top public agents are forks of the same tape. In one such pairing, both farms were identical, with the same crops and animals on days 10, 20 and 29 and money within a few coins through day 16. The game was then decided entirely by when and how much each side sold on days 17–25, mostly wool, whose price swung from 226 down to 31 and even 1 when both dumped at once.

If you fork a popular tape, your edge against its siblings lives almost entirely in the market layer. Test sale-logic changes against those siblings specifically, not only against a broad pool.

6. A negative result: splitting endgame bulk sales made things worse
v7's endgame route issues SELL <item> 1000 orders from day 27 on, dumping the whole shed at once. That looked like an obvious leak, so I wrapped it to sell in even per-turn slices instead.

Result over 6 seeds: own score dropped by ~1000 against both V53 and hybrid, and v7's gap to V53 didn't close (−4.9k → −6.2k). Late-season prices seem to reward getting stock out early. And v7's problem against V53 is ~5k deep, well before the endgame.

Small practical tips
kaggle kernels list --competition kaggriculture only returns a few dozen kernels. Keyword --search finds many more public agents.
In Python, read JSON written by PowerShell with encoding="utf-8-sig". A UTF-8 BOM silently broke my daily pipeline on a cp949 system.
Happy to answer questions about the method. I've kept this post to things that help everyone measure better. Good luck on the ladder!


Cauã Freitas · 9365th in this Competition · Posted 3 days ago
Qual estratégia a ser utilizada nessa reta final da competição?
Olá!! Percebi que algumas estratégias utilizam apenas dois tipos de produtos na fazenda: um para cultivo e outro para estabilidade. Nessa reta final, é válido manter a mesma estratégia ou vocês perceberam alguma outra que poderia compartilhar comigo, por favor?


React


dzjiann · 1800th in this Competition · Posted a day ago
My RL Won, But Also Failed: Two Days of Training on a 196-Core Server
I spent the last three days running reinforcement learning on a 196-core server.

In one sense, it worked surprisingly well.

After RL training, the agent could beat the public scripts with nearly a 90% win rate. Compared with the initial policy, the improvement was very obvious, and for a while I thought RL might be the key to pushing much further.

But then the improvement basically stopped.

Even after adding self-play, the agent quickly reached a plateau. More training did not seem to produce meaningfully stronger strategies.

The more interesting problem was that its performance against strong players barely improved.

Despite being extremely good at beating the public scripts, the RL agent could only reach around the top 100 at best. More surprisingly, against high-scoring players, it was actually weaker than several of my earlier approaches that were based purely on mathematical reasoning and dynamic programming.

I still think RL has potential here, but simply throwing more compute and more self-play at the problem does not seem to be enough.

Maybe the real challenge is not optimizing the policy harder, but creating a training population and objective that actually force the agent to discover more general strategies.

Would be very interested to hear how others would approach this.




React
8 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Aaweg Bhaladhare
Posted 19 hours ago

· 27th in this Competition

bro how did you get 196-Core Server….I'm so slowed by compute on 64cores🥲


Reply

React
dzjiann
Topic Author
Posted 19 hours ago

· 1800th in this Competition

That’s really impressive—you achieved such a high ranking with so little compute.


Reply

React
DECEM
Posted 21 hours ago

· 1st in this Competition

Getting Better and Better


Reply

1
OmerZalman
Posted 2 hours ago

· 557th in this Competition

what RL did you use?


Reply

React
Gerardo Del Toro
Posted 19 hours ago

· 6588th in this Competition

Did RL approach went for a step by step micro level decisions or at a higher level policy RL? Sparse win/loss reward was enough?


Reply

React
dzjiann
Topic Author
Posted 19 hours ago

· 1800th in this Competition

a higher level policy.spare reward is enough.


Reply

React
shiba-inu
Posted 7 hours ago

· 3718th in this Competition

Wow, so you're training with sparse…

Are you using self-play, or are you training against publicly available agents?

In my case, I've been using self-play against the current policy and its past checkpoints. My agent can reach scores close to 100k in self-play, but it still can't beat the public agents at all…


Reply

React
dzjiann
Topic Author
Posted 7 hours ago

· 1800th in this Competition

I mix with self-play and public agents


Reply

1

1
OmerZalman
Posted a day ago

· 557th in this Competition

did you use PPO?


Reply

React
dzjiann
Topic Author
Posted a day ago

· 1800th in this Competition

Yes, but during training I found that not reusing old trajectories from the previous rollout actually made training more stable, and the policy improved faster as well.


Reply

React
OmerZalman
Posted 19 hours ago

· 557th in this Competition

how many games did you do?


Reply

React
dzjiann
Topic Author
Posted 19 hours ago

· 1800th in this Competition

About one million of games


Franklyn Rosario MBA-ITM · 3957th in this Competition · Posted 5 hours ago
Eligibility of MIT-licensed public agent code under Rules 3.6(c) and 3.14(a)
If an entrant submits substantially the same code as a publicly shared, MIT-licensed Kaggriculture notebook, preserving the author and license notice, is that entry eligible for final judging and prizes under General Rules §§3.6(c) and 3.14(a)? Does the winner license affect the answer? We would appreciate a ruling before September 30.



デワンシュ · 338th in this Competition · Posted 2 days ago
Slow Rank Climb-up
Is it just me or the rankings are moving more slowly compared to a week ago?

│                          │ Games │ Win % │ Rating │ Median rating of last 20 opponents │ Win % in those 20 │

│ V21                      │ 105   │ 60%   │ 2522   │ 2443                               │ 45%               │
│ V28                      │ 129   │ 88%   │ 2029   │ 2098                               │ 90%               │
│ V29                      │ 85    │ 92%   │ 1887   │ 2008                               │ 90%               │

1
6 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Setu Chokshi
Posted 2 days ago

· 625th in this Competition

Agreed, the game matchups are happening maybe once or twice an hour


Reply

React
Alex Paul
Posted 2 days ago

· 1570th in this Competition

Yes, I noticed it too. Earlier submissions used to take usually 5 hours, sometimes up to 8 hours, to converge; now, it sometimes takes more than a day


Reply

React
デワンシュ
Topic Author
Posted 12 hours ago

· 338th in this Competition

The issues has been resolved now!


Reply

React
Omkar Kadam
Posted 2 days ago

· 2521st in this Competition

How to see this info for my submissions if i want to see ?


Reply

React
デワンシュ
Topic Author
Posted 2 days ago

· 338th in this Competition

This is not available directly, what you can do is, scrape the replay logs of three runs of your agent and then run a script to calculate and get those stats.


Reply

1
デワンシュ
Topic Author
Posted 2 days ago

· 338th in this Competition

noticed the slow rating updates starting some time between 14:43 and 19:03 UTC on Sept 23.


OmerZalman · 557th in this Competition · Posted 2 days ago
Question for M & M & P & Q and Boey
Around a week ago, you guys were at the top, and then both of you guys dropped dramatically low, I think I saw M & M & P & Q obtain a negative score. Why did you guys do this and not just continue having the best score? Was it so that top players could not train against you?


1


Hole Neckles · 8676th in this Competition · Posted 2 days ago
Scoring Formula or conditions
Hello. I’d like to ask something: according to the competition rules, agents that do not lose and achieve high scores in the game within the Kaggle environment earn a high ranking on the leaderboard. I tested an agent that holds a high leaderboard rank; it scored only 6 points in the game (despite its 1700 leaderboard score), whereas my agent never loses and its game score never drops below 33,000. I have utilized all the game features, yet my agent's leaderboard score is only 282. Am I misunderstanding something about the rules?


React
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Yusuke Hayashi
Posted 2 days ago

· 523rd in this Competition

https://www.kaggle.com/competitions/kaggriculture/leaderboard?search=Neckles&submissionId=56540011 is your agent's action. Even if you achieve a score of 33,000, if your score is lower than your opponent's, you will lose and your rating will drop. In addition, your opponent's score also fluctuates depending on your own actions and the seed, so an agent that can achieve a high score does not necessarily always achieve a high rating. However, you can pretty much assume that an agent that only scores 6 points will lose, so if that agent truly only scores 6 points every time, a rating of 1700 would probably not be possible. It might just be that it drops to 6 points under certain conditions, or that it fails to reproduce the agent's true potential.


Reply

React
Hole Neckles
Topic Author
Posted 2 days ago

· 8676th in this Competition

Thanks for answer. But if one agent sometimes loses how can be gain high score than agent which never losses and every time guaranteed score minimum 33000.


Reply

React
Yusuke Hayashi
Posted 2 days ago

· 523rd in this Competition

If you truly never lost a single time on Kaggle, your rating would exceed 3000 and rise to the 1st spot. Your agent actually loses frequently and has a low rating. By the way, matches between strong agents often result in a score of around 100,000.


千早爱音 · 211th in this Competition · Posted 3 days ago
Why there are still public notebook being shared？
Shouldnt it be forbidden since 23rd ？


4
5 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Sayaka Miki
Posted 3 days ago

· 7th in this Competition

Existing notebooks can still be updated after the deadline…Don't know why kaggle hasn't fix this bug.


Reply

React
千早爱音
Topic Author
Posted 3 days ago

· 211th in this Competition

OMG^^ thats really annoying…


Reply

React
CHEN Xiang
Posted 3 days ago

· 921st in this Competition

I know your team… July 7th was sunny. Suddenly, it began to snow heavily. I dare not open my eyes. I hope it's just my imagination… Still Going…


Reply

5
千早爱音
Topic Author
Posted 3 days ago

· 211th in this Competition

I stood at the edge of the Earth……


Reply

React
CHEN Xiang
Posted 2 days ago

· 921st in this Competition

Nan Beng…


Reply

React
Zotar
Posted 3 days ago

· 378th in this Competition




Debmalya · 1819th in this Competition · Posted 3 days ago
[Tool] A byte-identical Rust simulator for Kaggriculture: ~550k steps/s, parallel tournaments, self-play data
I'm releasing an open-source simulator and evaluation toolkit for this competition, in case it saves others the time it saved me.

GitHub: https://github.com/debmalyaroy/kaggriculture-simulation (Apache-2.0)
Kaggle dataset (static Linux binary + Python package, ready for notebooks): https://www.kaggle.com/datasets/debmalya84/kaggriculture-simulation
What it is
A Rust port of the official Kaggriculture interpreter (kaggle-environments==1.32.7) that produces identical game state at every step, plus tooling around it:

kagg serve / kaggsim.env: a step-by-step environment (gym-style reset / step) your Python agents or RL code can drive.
kagg tournament: your main.py against a panel of agents (other main.py files, recorded tapes, built-in fixtures), across many worlds, in parallel. You get per-opponent, per-world and per-seat scores with confidence intervals, and a paired A/B verdict (McNemar) between two builds.
kagg selfplay: labelled self-play data (features, and labels such as outcome and discounted return) streamed to a JSONL file or to any program that reads stdin, so you can plug in your own feature extractor.
Tapes: replay to action stream, splice, validate, turn a tape into a runnable main.py, and batch-play thousands of tape pairs.
Replay tools: reproduce any replay exactly, continue it from any step with different actions, and break down where each player's money came from.
How "byte-identical" is checked
The differential suite drives the official interpreter and the Rust engine with the same actions and compares a digest of the full state after every step: both banks as IEEE-754 bit patterns, every field of every tile, both players' private blocks (shed, seeds, carried items), market inventory and prices, and the unlocked shops. The episodes come from synthetic policies (random soup including illegal actions, observation-aware random play, a scripted farmer, a last-turn seller) in both seats. CI runs 50 episodes per push and 500 nightly on fresh seeds. Games played by Python agents through the tournament runner are also checked against the official runner's final banks.

Engine details worth knowing (these apply to any simulator you write)
719 actions, not 720. The official runner asks for actions at steps 0..718 and scores the step-719 state. A driver that applies a 720th action (and the extra end-of-day it triggers) changes the bank of any agent that acts on the last turn.
Empty [] entries are positional. Market orders settle one order index at a time, in lockstep across both players, and hands[i] goes to hand i. Dropping an empty entry changes which orders settle together, and which hand does what.
The world is realized by play. Weeds and shop unlocks draw from the same per-day RNG, and weeds take one draw per empty tile. So the shops you get depend on the seed and on both players' actions. The first shop is fixed by the end of step 71 and the second by step 143.
Check your engine version. 1.32.7 changed CARROT/TOMATO/EGG scarcity pricing (the "hinge" curve). An older kaggle_environments left in a user site-packages directory silently prices on the old curves. The toolkit hashes the engine file and refuses anything but the pinned release.
Call agents like the official runner. Truncate (obs, configuration) to the agent's argument count, give each seat its own fresh observation copy containing only its own private block, and pass an attribute-accessible configuration.
Speed (indicative, measured on a loaded desktop with 1 to 2 workers)
step function, 1 thread	~550,000 steps/s (~770 full games/s)
batch of tape pairs, 2 threads	~850 games/s
same 20 games with Python agents: official env.run	~2.5 s/game
same 20 games: kagg tournament, 2 workers	~0.15 s/game (about 16x), identical banks
memory, 1,000 games on 2 workers	~7 MiB
Quick start in a notebook
import os, shutil, sys
DS = "/kaggle/input/kaggriculture-simulation"
shutil.copy(f"{DS}/kagg", "/kaggle/working/kagg"); os.chmod("/kaggle/working/kagg", 0o755)
os.environ["KAGG_BIN"] = "/kaggle/working/kagg"; os.environ["PYTHONPATH"] = DS
sys.path.insert(0, DS)

from kaggsim.serve import run_match, load_agent
print(run_match(load_agent("/kaggle/working/main.py"), load_agent("/kaggle/working/main.py"), seed=3))
Limitations
Default configuration only (no custom marketParams).
Tape-based tools are open loop: a recorded stream doesn't react to a different opponent.
Python agents still run in Python. The engine is fast, but a slow agent is still slow.
The repository contains no competition agents or strategy, only the engine, the tools and synthetic test fixtures. Bug reports, especially any divergence from the official engine, are very welcome: python -m kaggsim.fidelity diverge a.py b.py --seed N prints the first step where the two engines disagree.

Not affiliated with Kaggle. The engine is a port of the Kaggriculture environment in kaggle-environments (Apache-2.0).


2
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Syed Asad Ali
Posted 3 days ago

· 39th in this Competition

Thanks for sharing this, and especially for the step-by-step differential testing against the official interpreter. The "719 actions" and "empty entries are positional" notes are exactly the kind of details that are easy to get wrong.

Nice work

Why aren't these agents planting in the southeast?
I was watching some of the top agents and noticed they weren't planting anything in the southeast.


React
8 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Georgy Mamarin
Posted 3 days ago

· 577th in this Competition

The thread has already settled whether they do, so here is what it costs.

The unlock order is fixed: LAND_ORDER = ["NE", "SW", "SE"], LAND_PRICES = [1000, 2000, 4000], and _do_buy_land always takes the next entry. Reaching the southeast therefore costs 7,000 coins, not the 4,000 on its own price tag, and the farm that gets there owns 100 tiles instead of its starting 25, all of them needing cover.

Caveat: my test bed is a naive carrot bot against the starter, so it says nothing about what the top of the leaderboard manages. Twelve paired seeds, same opponent, only the farm plan moving:

25 tiles, one farmer, all of it free land: -930 ± 432 against the 6-tile baseline
12 tiles, 3 hands sharing one job list: -601 ± 320
12 tiles, 3 hands each owning a slice: +3,871 ± 990
50 tiles, 6 hands, after buying NE: +1,217 ± 619
Ground on its own is worth less than nothing to a bot that cannot cover it. Bare ground at nightfall tracks the bank far better than ground per worker does: the two middle arms both work three tiles per worker and finish about 4,500 apart. Sharing one list, every unit takes its next job off the top of that list and they converge on the same tile, leaving five or six of the twelve bare at day's end against almost none when each owns a slice.

Dipam's last clause has a size. The hire ladder is Fibonacci from one coin and resets every morning along with the crew, so the climb is paid again each day instead of compounding across the season. My six-hand arm paid 20 coins a day, 600 for the season, against the 1,000 the quadrant cost it. Ten hands a day would be 143. That arm still finished ahead after paying for both, though well behind the 12-tile farm that stayed on free land.


Reply

1
destbreso
Posted 4 days ago

· 1229th in this Competition

The top of the leaderboard is planting in the fourth quadrant under certain conditions  


Reply

3
xaxipiruli
Posted 5 days ago

· 6134th in this Competition

I checked, and there are games in which those agents plant in the southeast.




Reply

React
Ahmet Yasin Tat
Topic Author
Posted 5 days ago

· 2271st in this Competition

yeah there are, but not many


Reply

React
Jack
Posted 5 days ago

· 26th in this Competition

Number one on LB is actively using SE quadrant lol


Reply

React
Dipam Chakraborty
Posted 5 days ago

· 86th in this Competition

Its not clear that you can make more money with it in 30 days, and you need more hires to manage it effectively, cost of hires keeps increasing a lot.


Reply

React
Rekh_Sharath_Chandra
Posted 3 days ago

· 8581st in this Competition

They can plant in the Southeast, but reaching it is expensive.

Unlock order: NE → SW → SE Costs: 1,000 + 2,000 + 4,000 = 7,000 coins


dzjiann · 1797th in this Competition · Posted 4 days ago
How long does RL training usually take for agents?
I’ve been training a reinforcement learning agent for the game,but it improves slowly, and I’m curious about people’s real-world experience with training time. Hours, days, millions of games, hundreds of millions of game? I’m a bit worried that I won’t have enough time left to train a model that’s actually strong enough.

I’d also be very interested to hear how many games it took you to reach a certain win rate against a strong public opponent. Even rough numbers would be really helpful for setting expectations.


React
6 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
OmerZalman
Posted 4 days ago

· 555th in this Competition

i did like 50B steps I think


Reply

1
Steve421471
Posted 4 days ago

· 2920th in this Competition

I think I did about half a billion steps total across multiple attempts over 3-4 weeks. I can't speak for the people who have been successful with it, but my best attempt was about 4 days on a 3060 just to produce an agent that could beat its own base script most of the time. The meta moves so fast that it was already inferior before it was finished.

With the right architecture and some rented compute you could probably get something good in a day or less. The right architecture is what I have failed to figure out.


Reply

1
Gerardo Del Toro
Posted 4 days ago

· 6588th in this Competition

So your current approach is not RL based?


Reply

React
Steve421471
Posted 3 days ago

· 2920th in this Competition

Correct. Most of my submissions have been based on improving public code or replay distillation.


Reply

React
Brahim
Posted 4 days ago

· 3845th in this Competition

Short answer: depends on a lot of factors, in my case ~tens of millions steps, detailed answer below.

Action space : a big one. A stricter action space can remove useless actions or simplify agent possiblities, and speeds up training since your policy will have less things to explore over. Tradeoff here is that it limits what it can express, which can cap it's final performance, or end in a sort of local optimal.
Reward design comes next. Ideally you'd use a sparse reward and let the policy figure out how to win on its own. But if it never discovers the chains of actions that lead to winning, it gets no signal and stays at zero. A dense reward helps with that, but depending on what you reward, you can end up with a lot of reward hacking. One way to get the best of both is a curriculum: you start with a dense shaping to get signal early, then anneal it toward the sparse objective so the policy stops optimizing your proxy and optimizes actually winning.
Observations: once the action space and reward are in place, the observations need to be rich enough to guide actions toward that reward. That's what makes credit assignement work.
Opponents: with those three components done properly, training objective becomes the next bottleneck. Training against a single fixed policy just teaches your agent the best way to beat that one opponent, which is basically the equivalent of overfitting in RL. Train against a mix of opponents instead. Self-play is the next step up, but it brings its own problems.
In my experience, with a setup close to this, beating a single opponent takes tens of millions of steps (Only beating some of them so far). Generalizing without breaking things is where I'm still making progress, seeing improvements there but not sure if i'll make it in time. Note that i'm not taking the hierarchical way, spliting high level intent and low level macro executions, which would make things faster. I'm more interested in taking the challenge in making the full end to end work than hunting the medal, to see what strategy and adaptations it would learn if it had more freedom in a sense.

Some random tips:

Shorter runs to debug each of the above and check that what you expect is actually happening.
Watch what the agent does, not just the return. I've had runs where a lower final return was more interesting behaviourally for the next runs than a higher one.
It's easy to collapse into a single strategy, so keep an eye out for it.

Reply

3
dzjiann
Topic Author
Posted 4 days ago

· 1797th in this Competition

Thank you for your share!


Reply

React
Gerardo Del Toro
Posted 4 days ago

· 6588th in this Competition

You are not DP or RL based then?


HyperNeonByte · 7436th in this Competition · Posted 4 days ago
If you tried BC at the micro level, how did your agent perform?
I've been trying RL at the micro level, and am experimenting with warming up the weights using BC. After hours of training on my 16-core M4 Max, I can definitely see it learning (the action prediction loss keeps decreasing), yet the agent is still pretty useless and struggles to reach even $1k in terminal cash.

I did see successful BC implementations in other competitions produce agents good enough to rank in the top 10% (like mentioned here: https://www.kaggle.com/competitions/google-football/discussion/200709)

There are definitely a lot of things I could try, like feature engineering, changing my model structure, or training longer. But I’m curious: for people who have tried BC, or successfully trained RL agents afterward, how did your BC agent perform? Is there anything you could share about how to gauge the effectiveness of BC at the micro level in this competition?

Thanks!


React


Avineesh Arora · 981st in this Competition · Posted 4 days ago
What actually predicted the ladder, and 15 things that didn't
My first local evaluator correlated with the real Kaggriculture ladder at r = +0.014. I checked it on 51 boards where I had real results to compare against. That is not a weak instrument. It measures nothing. Every verdict I drew from it for a week was noise.

This post collects everything I have measured since, including a few things I learned in the last two days that I haven't seen written down anywhere. The full method, with runnable code, is in my notebook (linked at the bottom). This is the short version with the numbers.

The opponent is part of the environment
Prices move with how much has been sold, so an opponent that trades moves your prices. starter, random, pass and frozen replays barely trade. Against them you are farming an uncontested market, which is a different game.

The same agent on the same boards:

vs starter locally: mean bank $121k

on the real ladder: mean bank $81k

A live opponent was costing about $40k a game, and none of my local numbers knew it.

The fix was a league of strong public agents that actually trade, played on real ladder boards. The board seeds come from your own episodes (competitions.EpisodeService/GetEpisode returns the seed). Checked against my real results, that league reached corr(bank) +0.458 and corr(margin) +0.533, up from +0.014.

The local engine reproduces the ladder to the coin
This is the one I wish I'd known in week one. kaggle-environments 1.32.7 is deterministic for a fixed seed and a fixed pair of agents, and it matches the ladder exactly. My submission's validation game (self-play, seed 0) banked 71,345 / 72,013 on Kaggle and 71,345 / 72,013 locally.

So any of your own ladder games can be replayed exactly. You can check your harness against real outcomes, and you can test "what if my new agent had played that exact game?" instead of guessing.

Win rate, not margin
The final standing is a single Bradley-Terry fit on win/loss (Kaggle staff, final evaluation post). One competitor lost a game 103,148 to 103,147 and took a full rating penalty for it.

This changed which agent I shipped. Two candidates, 384 paired games each:

Agent A: margin +$27,682, win rate 91.7%

Agent B: margin +$25,715, win rate 97.7%

Head-to-head on identical boards, B beat A by +6.0 pp [95% CI +2.9, +9.4] while banking $1,967 less. B wins more often, by less.

It matters even more near the top. In 100 of my games against opponents rated 2250+:

the median gap between the two players was $177, on banks around $98k;

40% of games were decided by under $100, and 78% by under $1,000;

seat made no measurable difference (44% vs 43% wins).

At that level, a change worth a few dozen dollars a game flips a real share of results. A change worth thousands in games you already win is worth nothing.

Pair everything, and look per opponent
The harness rules I added only after being burned without them:

Identical (seed, opponent, seat) triples for every candidate, and both seats. Pairing cancels board luck.

A bootstrap CI on the paired difference, plus a floor below which you call it a no-op. Identical paired deltas give the bootstrap no spread, and an exact no-op once reported "BETTER" to me on a $1 delta.

A per-opponent breakdown, not just a pooled number. Strong public agents here are not transitive. Among the current strong public agents I measured, three form a clean cycle: A beats B in 100% of games, B beats C 85%, and C beats A 100%. The pooled win rate hides all of that, and it changes which pair of agents you should keep.

Your agent has to survive the climb, not just the band you're aiming for
This one cost me a submission this week.

I built a league to look like the 2250+ band, then replayed candidates on the exact boards of my own 2250+ games. One candidate scored 82–84% on both. On the ladder it stalled near 1,800 after 85 games, winning only 56.5% against opponents below 2000. It never reached the band where it was strong.

A different candidate, submitted a minute earlier, won 93% below 2000 and was past 2,080 and still rising seven hours later.

Every new submission starts near 600 and has to beat the field on the way up. If your league models only where you want to finish, it cannot see an agent that loses on the way there. Check your league against a live submission's record in every band it passes through, not only the top one.

Crash-screen before you believe a number
Most agents wrap each turn in try/except and return PASS on failure. An agent that throws on every turn therefore plays a legal, silent game and banks about the $3,000 starting money. That looks like a result. It isn't.

It caught me three times. Now any bank near the starting money is a crash until proven otherwise, and I time the first move of a freshly loaded file, when a 1 MB agent is still building itself. Going past the 60-second overage bank forfeits the game.

How to read your score
New submissions overshoot. Mine have peaked at 1233 and settled near 950, and peaked at 1815 then fallen to 1539. Never quote the peak.

A rating needs 40–70 games to settle. Don't judge or replace a submission before that.

Bucket your games by the opponent's rating. The band where you win about 50% is your real level. The headline number lags it.

How the final ranking actually works (verified this week)
Only your latest 2 submissions are tracked, and they are your final pair (Overview → Evaluation). Your leaderboard score is the better of the two.

Each new submission retires the older of the two active ones. Order matters: submit the agent you want to keep last. I made exactly this mistake. Replacing a weak submission retired my strong one, because the strong one was older by one minute.

The Bradley-Terry fit uses "all episodes ever played between submissions that are still active" (Addison Howard, Kaggle staff, 22 Sep, in the "Tournament Question" thread). Games you play now count, but games against opponents who later swap out do not. So a good agent gains from being submitted early.

What failed
I measured 15 changes against opponents that trade, on real ladder boards, paired, in both seats. Two worked:

Repairing a blocked action (queue it, clear the blocker, replay it): +$4,373 margin, CI [+3,345, +5,339].

Removing a deep copy on the first callback: first move 292–423 ms → 1 ms. That protects against timeouts rather than raising the score.

The rest were nothing or worse:

Selling earlier: −$80k.

Splitting large sales across turns: −$60k to −$80k.

Holding stock while the price is depressed: −$2,330.

Handing the endgame to a tuned online controller: −$7,087, and it lost on every board.

Guards ported from stronger agents that never fired: exactly $0.

The sale schedule sits in a narrow feasible band. Sell later and the shed fills, so the next delivery fails. Sell earlier and you're selling goods that haven't arrived. The full table with CIs is in the notebook.

Do's and don'ts
Do

Check your harness against your own real episodes before trusting one verdict from it.

Pair everything: same seeds, same opponents, both seats.

Report win rate, per opponent, with a CI.

Replay your own ladder games exactly. The engine lets you.

Write down your prediction before you submit.

Don't

Measure against starter, random, pass or a frozen replay and call it an improvement.

Trust a title, a badge or a headline score. One well-regarded public agent measured worse than mine; another was in a different class.

Replace a submission that's still climbing, or submit your keeper first.

Believe a bank near $3,000.

What I'm not claiming

These numbers come from one competitor's games and agents. The correlations are clearly better than +0.014, but that doesn't make my harness a validated simulator, and I wouldn't defend their third decimal. The ordering of the two setups is the claim. Section 5 shows a well-validated league can still miss what matters. If your measurements disagree with mine, I'd genuinely like to see them.

Notebook, with the harness, the ladder-check code and the full failure table: Your Local Evaluator Is Probably Measuring a Different Game

Credits: the Kaggle team's final-evaluation posts (María Cruz, 31 Jul; Addison Howard, 22 Sep). destbreso's community agents dataset, which made a realistic league possible. Georgy Mamarin's episode dataset. busyaprime's public work on end-of-game waste. The agents I submit are forks of public Apache-2.0 notebooks, with their notices intact. The farming logic in them is not mine.


Tiago OliveiraLL · 9532nd in this Competition · Posted 6 days ago
Tips for beginners getting started
Hi everyone! I’m new to Kaggle simulation competitions and I’m just getting started with Kaggriculture.

For those who have already submitted an agent, what would you recommend as the best first steps? For example, should a beginner first focus on building a simple and reliable baseline strategy, learning the market behavior, or analyzing replays from other agents?

I’d also appreciate any advice on common mistakes to avoid, especially regarding crop/animal maintenance, market orders, and testing the agent locally before submitting. Thanks!


React
3 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
xaxipiruli
Posted 6 days ago

· 6134th in this Competition

Three things I'd suggest, from my own experience. Take them as one path, not the only one.

1- Nerf your opponent to your level.

When I started, I kept running into the same wall: public agents are all roughly the same strength, so I was training and tuning at either 0% or 100% win rate, no signal either way. What worked for me was taking a public notebook and capping how many workers it can hire. Their own logic resizes to the cap, so they stay coherent but beatable. That gave me a gradient to work against.

2- Shrink the game.

I also reduced the universe, fewer tiles, fewer days, fewer hours per day, because a smaller game is faster to iterate in and easier to measure. What I ran into: most public notebooks collapse when you shrink the game. Same reason capping workers works and throttling turns doesn't, as far as I can tell: they're plan executors, not reactive policies. So I ended up shrinking in parallel with the nerf, and accepting that most public agents weren't usable as reference points inside the reduced game. That was the price of having a lab I could actually learn in. Also, learning how to fit a set of rules to the smaller universe.

One thing I noticed along the way, in case it's useful: going back to the full game hasn't been automatic for me. The shorter horizon seems to be a different game, not just an easier version of the same one. The strategy shifts, and a policy tuned small doesn't transplant cleanly. So I've been treating each scale as its own problem rather than assuming the small one rolls up.

3- Look at the public notebooks before writing your own.

Before I wrote anything, what helped me most was reading the public notebooks and noticing something: they all follow pre-established plans, and they match each other on most unit actions and game states. The 96.5% figure I've measured is just that. The community is essentially submitting an itinerary with small variations on the same script.

So my suggestion: submit a main.py from some public solution as-is, just to see how the competition actually performs. Not to win, to understand the terrain. How it scores, how it loses, where the margins sit, who it plays against. That gives you a baseline and a feel for the ladder before you invest time in your own approach.

Once you've done that, the question becomes how you want to attack it. A few directions I've seen people take:

Improve the plan directly: same script, better constants, better sequencing.

Add a global planner on top: search over the plan instead of hand-tuning it.

Go straight to ML: learn the policy, treat the script as a baseline to beat.

Mix both: keep the scripted part for the situations where it's clearly right, and add adaptability plus learning on top, sampling the engine distributed across the competition.
I don't think one of these is obviously correct. It depends on what you want to spend your time on and how much compute you have. But the itinerary approach has the advantage that it's already been iterated on by a lot of people, so it's a solid floor to build from.


Reply

React
Yang Kuang Ou
Posted 4 days ago

· 1236th in this Competition

I’d start with a tiny valid baseline and a replay loop. Learn the mechanics from the official docs, then change one decision at a time. For each change, keep the opponent and seed fixed, swap both player seats, compare terminal cash, and inspect the replay. One or two seeds are useful for debugging; use more seeds and more than one opponent before drawing strength conclusions.

One easy-to-miss detail: farm actions resolve before market orders, so same-turn sale proceeds can’t fund a planting action that has already been processed. Plan harvest timing and the final selling window together.

I made a small public starter/evaluation notebook with a copyable one-plot wheat agent, a two-seed seat-swapped runner, and a bank/market replay plot: https://www.kaggle.com/code/yangkuangou/kaggriculture-agent-lab-copy-replay-compare

The four-game example is a debugging template, not a leaderboard-strength estimate.


Reply

React
Yujin Cha
Posted 4 days ago

· 1451st in this Competition

Update the champion every time among the laptops released.
Contact the disclosed community agent laptop among the disclosed laptops.
Refer to the discussion to identify and update the hidden rules of the game.
Learn the champion model of 1 using 2.
Identify opponents and revise strategies while watching my Dalian video from time to time.
Watch the No. 1 Dalian video from time to time and find something to learn from the No. 1 (or opponent who wins the No. 1) strategy.
Most of them are based on script rules, responsive types have extremely few success stories, and most of the top ranks are believed to borrow responsive types (PPOs).
The principle that beginners should keep is not to lift the fourth land, but to focus on profitable milk and strawberries, and Jungsu takes a price-driven strategy by recognizing the weaknesses of the genealogical model used by the other person.
Master seems to have his own game philosophy. What we still understand is that the last-minute reversal is amazing.
Ultra-high numbers pioneer their own path (response type) without relying on tape or public code, which is the method used by most people, and it is understood that there is agent code sharing between the top ranks.


dzjiann · 1798th in this Competition · Posted 6 days ago
BUG？I had more coins but was marked as the loser
At the end of this match, my final coin count was higher than my opponent's, but the game still marked me as the loser.  According to the final coin totals shown in the replay, I had 866 more coins than my opponent, but the game awarded the win to my opponent.

Could you please check whether there is an issue with the winner determination/scoring logic? If there is another win condition or tiebreaker that caused this result, it would also be helpful if that could be shown clearly in the result screen.


1
6 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
オグリキャップ
Posted 4 days ago

· 116th in this Competition

其实是浏览器bug Your message must have at least 10 characters.


Reply

React
wsc-MISX
Posted 5 days ago

· 26th in this Competition

Maybe TLE? (over extra 60s)


Reply

React
dzjiann
Topic Author
Posted 4 days ago

· 1798th in this Competition

I condidered it. but My notebook always runs in 20 seconds.


Reply

React
Michael Timbs
Posted 4 days ago

· 135th in this Competition

would be nice if this was visible though. Te first time i noticed this was teh first time i added inference time search to my submission so its possible that it was happening.


Reply

React
wsc-MISX
Posted 4 days ago

· 26th in this Competition

You can download the agent logs from your own submission to check whether it timed out.

The format looks something like this: [[{"duration": 2.065672, "stdout": "", "stderr": ""}], [{"duration": 0.545747, "stdout": "", "stderr": ""}], [{"duration": 0.205041, "stdout": "", "stderr": ""}], ….]




Reply

React
Michael Timbs
Posted 5 days ago

· 135th in this Competition

I'm also seeing this on my most recent submission


Reply

React
KawattaTaido
Posted 6 days ago

· 11th in this Competition

I checked this on my side, both in the browser replay and by downloading the match JSON.

It looks like this might be a replay/display issue rather than a problem with the winner determination. The match shown in your browser seems to be different from the one in the JSON, so the replay may not be reflecting the correct match.

You might want to check the downloaded JSON as well.




Reply

React
dzjiann
Topic Author
Posted 6 days ago

· 1798th in this Competition

Thank you! I found the seed in your screenshot is different from mine. I check the replay again and it's change to be same to yours. Maybe display system has some bug.

Tournament Question
Following up on the two unanswered questions above about the final tournament.

Is the Bradley-Terry fit computed over all episodes a submission has ever played, or only over episodes played during the two weeks after the September 30 deadline?

It matters for planning. If it uses full history, episodes banked now count toward the final rating. If it uses post-deadline episodes only, current ladder position is informational and only the frozen agent matters.


React
1 Comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Addison Howard
Kaggle Staff
Posted 5 days ago

· 1540th in this Competition

It will run over all episodes ever played between submissions that are still active. So if your agent had played 1000 matches at the end of two weeks, but only 637 of those were against submissions still active on the leaderboard only those 637 will count.


xaxipiruli · 6135th in this Competition · Posted 7 days ago
Neurosymbolic RL for Kaggriculture: what actually moved the needle [WIP]
Update. The code is now public: https://github.com/frapercan/kagsym (MIT). This revision splits the post in two — Part I is what the agent is, Part II is the eleven-plus tricks, which is how it should have been written the first time — and brings the architecture section up to date, because the answer to "how many numbers does the policy emit" changed from 14 to 64 since the first version, and that change is the main result of the last stretch.

In one paragraph, without the jargon
A commenter said this post uses a lot of fancy words, and that is fair. So, plainly: the game gives you a farm, 720 turns and an opponent selling into the same market. Some of the decisions have a right answer you can compute — the shortest path to a tile, which unit should go where, what the 12th unit of wheat will sell for, whether a crop still has time to ripen. Those I calculate exactly and never let a neural network guess. The rest — how much land, which crop, how many animals, when to dump produce on the market — has no right answer you can write down, because it depends on what the other player does. Those a network learns. The whole project is an attempt to find, by measurement rather than by taste, where the line between the two sits. Most of what follows is the measurements that told me I had put the line in the wrong place.

A thank-you that isn't a formality
Every single number in this post is measured against agents somebody else published and explained — v48-fast-routes, v16-rc5-high-score-8c-4s-premium-market-lead, the-2945-farm-96-vs-the-top-10-public-bots, shop-router-0909, and the rank-your-agent notebook that made head-to-head evaluation trivial. I did not just use them as a leaderboard to climb. I used them as opponents strong enough to make a measurement mean something, as teachers to clone from, and as the external thermometer that caught my own training loop lying to me (Trick 8). When I needed a difficulty ladder and there wasn't one, I built it by handicapping their agents, because their internal logic is good enough to resize itself sensibly when you constrain it (Trick 7).

The discussion threads did something different and just as necessary: they framed the problem before I had any data of my own. The thread asking how the top agents minimise time and maximise profit at the same time is what made me stop treating this as an economics problem and start treating it as an action-budget problem — which is the frame that eventually produced the crop-density result in Part II. Someone publishing that their JAX pipeline ran at ~10k steps/s is why I knew my own throughput number was worth chasing rather than being quietly satisfied with it. And the general consensus in the threads that RL is hard in this environment turned out to be correct for reasons nobody had written down yet — most of Trick 6 and Trick 8 are me discovering why, the expensive way.

Reading those threads before writing code saved me from at least two of the dead ends below, and pointed me straight at a third.

A self-play loop can convince you that you're winning while your real strength collapses. The only thing that reliably stopped that here was a fixed, strong, publicly-shared opponent sitting outside my training loop. So: thank you to everyone who published a working agent and wrote up how it worked. This post is downstream of that, and several of its results only exist because you did.

With that said — what follows is mostly negative results from building an end-to-end learned agent. I think they're more useful than another "here's my architecture" post, and they're certainly more honest about how the time was spent.

Part I — the project
The setup
Exact engine clone. Instead of reimplementing the rules, I call the real interpreter on a duck-typed state object. It's exact by construction and never desyncs when the engine updates. Runs at ~38,500 steps/s versus the full kaggle_environments wrapper.

Neurosymbolic split. The network decides strategy; exact arithmetic handles mechanics.

Symbolic (derivable from the engine, stays hand-written): legality of operations, routing distances, Hungarian assignment of units to tiles, marginal-price arithmetic, final liquidation value.
Neural: a daily macro vector (how much of each thing), and a per-tile head emitting a value plus one logit per legal verb.
The key idea: never let the network guess something you can compute exactly, and never hand-code something that depends on the state in a way you can't write down.

What this is actually an experiment about
Eleven tricks with no thesis is a list. Here is the thesis, and what each moving part is for — because two of them are instruments, not competitors, and reading them as competitors is how I misread my own results for a week.

The question. Not "can I win this competition". It is: where exactly is the line between what should be computed and what must be learned, and how do you find that line by measurement instead of by taste? I have an exact clone of the engine, so anything derivable — legality, routing, assignment, marginal prices, liquidation — I can compute perfectly. Everything else is a candidate for learning. The interesting claim is that the line is discoverable, and that most people (me included) put it in the wrong place by intuition.

What CEM is for: it is the control, not a rival. CEM searches for the best fixed 14-number vector — a strategy that cannot look at the state at all. So whatever it achieves is a measurement of how much of this game is solvable without conditioning on anything. That makes it the denominator for the only question that matters here: anything a learned policy gains over CEM is, by construction, the value of state-dependence. Nothing else.

This is why "PPO does not beat CEM" is the central result of the project rather than a disappointment. It is a clean ablation reporting that the state-dependence I am paying for — the whole network — is currently earning nothing. A negative result from a well-built instrument is still a measurement.

What PPO is for: the hypothesis CEM cannot test. The bet is that the optimal strategy is not one fixed vector — that it should shift with the day, with prices, with what the opponent has already dumped on the shared market. A fixed vector cannot express that by construction. PPO is the candidate for that part. The bet is currently unpaid, and I want to be exact about the status: not refuted, unmeasured in its favour.

What the public agents are for — three jobs, and conflating them is an error I made.

External thermometer. Fixed, strong, entirely outside the training loop. This is the only thing that ever caught my self-play league congratulating itself while sitting on its starting cash (Trick 8).
Difficulty ladder. Not by throttling them — that shatters them (Trick 7) — but by capping hiring, because their own logic resizes to the unit count.
Tightness check on the upper bound. See below. This is the job I only discovered at the end, and it is the most valuable.
What they are not: teachers (cloning failed twice at ~99.5% agreement, Trick 4), and opponents at any scale but the full game (they are 719-step tapes with persistent internal state; shrink the horizon and they score $0–30).

The natural law I am actually hunting. The cost of the three transitions: inaction -> minimum viable movement -> the global maximum, even a conditional one. That gets its own section, next.

The four numbers that make any of this sayable. This framing is the part I would keep if I threw away everything else:

inaction                 $3,000    policy-independent floor, any horizon
CEM (best fixed vector)  $55,350   LOWER bound: best found without state
a real public agent     $145,080   where a good policy actually lands
relaxed problem         $195,532   UPPER bound: no policy can exceed it
(Full game. The relaxed bound ignores distances and inter-unit coordination, so nothing can beat it, though nothing need reach it.)

Two things only exist because of that fourth number. First, the bound is tight: a real published agent reaches 74% of it, so the relaxation is not fantasy. Second, we are at 28% — which means the CEM ceiling I had been treating as the target all along is 38% of what a real agent already achieves in the same game. There is 2.6x of demonstrated headroom, not conjectured.

That also resolves something I could not answer before: how do you tell "this scenario is exhausted" from "my search is stuck"? You cannot, against a lower bound — "I found nothing better" is what both look like. Against an upper bound you can, because achieved / bound is a fraction with a meaning.

The natural law: what it costs to start moving
Inaction is an absorbing state with a known, horizon-independent value
Doing nothing keeps exactly the starting cash — $3,000, standard deviation zero, at every horizon I have tested. Not approximately. The strategy vector of all zeros returns 3,000 on every seed.

That is a gift and I did not appreciate it for weeks. It means there is a free, exact, policy-independent baseline at every scale, which is what lets you say "this policy is inert" in one glance instead of inferring it from a win rate. It is also why every number in this post is quoted as a multiple of it.

But it is an absorbing state. Every action in this game costs up front and repays later: hiring costs Fibonacci money, seed costs money, feed costs money, and movement costs actions, which are the genuinely scarce resource. You must go down before you can go up. If the horizon does not let the investment repay, the optimal policy is literally to sit still.

The phase diagram, measured
Best achievable money by scenario, as a multiple of inaction. Found by search, not asserted:

 2h x 13d   1.000      3h x  8d   1.000      3h x 13d   1.000
 3h x 21d   1.000      5h x  5d   1.000      5h x  8d   1.000     <- IMPOSSIBLE
 5h x 13d   1.073      6h x  6d   1.080      8h x  8d   1.248     <- thin
 5h x 21d   1.815      8h x 13d   5.113      8h x 21d   6.304     <- comfortable
13h x 13d   8.838     13h x 21d  10.109     24h x 30d  18.450     <- the real game
The top block is not "hard". It is impossible: no policy in the search space beats sitting still, because there is no horizon in which the first hire pays for itself. That is a fact about the economy, not about the optimizer.

And the axis is not total turns, which surprised me. Compare equal-length games:

 3h x 21d =  63 turns  ->  1.000          5h x 21d = 105 turns  ->  1.815
 5h x 13d =  65 turns  ->  1.073          8h x 13d = 104 turns  ->  5.113
 8h x  8d =  64 turns  ->  1.248
At a fixed number of turns, hours-per-day dominates. The mechanism is clean once you see it: a worker is hired per day at a fixed cost, but works hours per day. So hours-per-day is the productivity of the investment and days is the time to repay it, and they are not interchangeable. Sixty-four turns as 8x8 is a different economy from sixty-three turns as 3x21.

The three transitions, and what each costs
This is the actual research programme, and I state it as three costs because that is how it is measurable:

1. Inaction -> first profitable action. What is the smallest bundle that repays? It is not a single lever. At 8h x 13d you need enough workers and the right crop, and getting the crop wrong scores 0.39x — 61% worse than doing nothing. So the first viable move is a conjunction, and most of its neighbourhood is worse than the floor. That is the barrier.

2. First profitable action -> the best fixed strategy. This is what CEM measures, and it is a lot: 5.113x at 8h x 13d, 18.450x at full scale. All of it achieved by a strategy that never looks at the state.

3. The best fixed strategy -> the global maximum, which may be conditional. This is the open one, and the relaxed upper bound says it is the biggest of the three: we are at 28% of the bound, a real agent is at 74%. Whether that last leg requires conditioning on state is exactly the unproven premise of the project.

Cost 1 is a threshold. Cost 2 is search. Cost 3 is the bet. I had been conflating all three under the word "training".

The ladder, and the thing that is not a ladder
Two structures, two purposes. Conflating them cost me most of a week.

Reduced horizons are a laboratory, not a curriculum
I assumed shorter games were an easier curriculum you could graduate from. Trick 9 already said they are a different game. Measured directly, it is worse than that — transplanting one scenario's optimum into another, as a percentage of the destination's own ceiling:

   origin    ->  destination     money   % of destination ceiling
 8h x  8d    ->   8h x 13d         886        5.8%
 8h x  8d    ->   5h x 21d          18        0.3%
 8h x 13d    ->  24h x 30d         727        1.3%
24h x 30d    ->   8h x 13d       1,608       10.5%
 5h x 21d    ->  24h x 30d      21,398       38.7%
Inaction is 3,000. In eight of the twelve transplants I ran, carrying over a neighbouring scenario's optimum leaves you worse off than doing nothing. Not weak transfer — actively harmful. There is no sense in which solving the small game moves you toward the big one.

So what are they for? They are where the mechanism is visible. At 8h x 13d an episode costs 20 ms against 1 s at full scale, and the paired standard deviation is roughly 150x smaller, so you can resolve effects there that are permanently invisible in the real game. Trick 11 exists only because a full axis sweep is seconds of compute at that scale. Use them to see, not to graduate.

The actual ladder is the opponent, at full scale
The game stays identical — same horizon, same board, same economy — and the only thing that varies is the opponent's hire cap, which works because their logic resizes itself to its unit count (Trick 7). Same search vector throughout, no training:

hire cap     ours      v48     margin    wins
       3   62,556    4,229  +1379.2%   12/12
       5   52,174   27,882     +87.1%   12/12
       8   49,106   58,765     -16.4%    5/12    <- the crossover
      11   39,990  110,859     -63.9%    0/12
    none   37,673  124,276     -69.7%    0/12
This is a curriculum in the way the horizon axis is not: monotone in difficulty, a genuine 50/50 crossover point, and — crucially — nothing learned at one rung is invalidated at the next, because it is the same game throughout.

When to promote
The question I could not answer before the relaxed bound existed: how do you distinguish "this rung is exhausted" from "my search is stuck"? Against a lower bound you cannot — "I found nothing better" is what both look like.

Against the upper bound you can, because achieved / bound is a fraction with a meaning. Promote when that fraction stops climbing, not when you win. Winning is what promoted a policy that sat on its starting cash through four leagues (Trick 8); a fraction of an upper bound cannot do that, because inaction scores 1.5% of the bound and says so.

The honest caveat: the relaxed bound is verified tight only at full scale, where a real agent reaches 74% of it. At reduced scales there is no live agent to check it against, and an unvalidated bound is exactly the mistake I made once already — an analytical bound ranked 2h x 13d as promising, and 145 updates of training there drove the policy to 0.82x, destroying value.

The interface, concretely
A commenter asked what actually connects purchases, pickup, routing, placement and maintenance, and whether the executor keeps persistent jobs. Writing the answer was more useful than anything else I did that week, so it goes in the post rather than the thread.

Everything is recomputed every turn. No jobs, no reservations.

n_units = max(len(hands), target_workers(macro))    # PLANNED, never the live count
free    = sustainable_tiles(n_units) - already_planted
values, op_logits = micro_head(obs)                 # 10x10, and 15x10x10
assign  = assign_units(obs, free, values, op_logits,
                       previous=yesterdays_destinations,   # the only surviving state
                       macro=macro)
orders  = concat(cat() for cat in order_by(macro.priorities))[:10]
The only state crossing the turn boundary is yesterday's assignment, used as a soft stickiness bonus whose weight the policy sets. Measured, with the search optimum fixed: stickiness 0.00 gives $23,793, 0.25 gives $27,177 (+14%), 1.00 gives $22,755. Interior optimum, so it cannot be reasoned to a constant.

Persistent jobs would lock in an arbitrary choice — unit ordering is meaningless and greedy assignment strands units. But recomputing means nothing enforces multi-turn commitment either, and one scalar is a blunt instrument for it. That is an unresolved tension in my design, not a solved problem.

The 14 numbers the policy actually emits
This is the part I never spelled out, and spelling it out changed what I think the problem is. The network emits 14 reals in [0,1] per day, plus the per-tile map. The executor turns those 14 into exact quantities:

#	name	resolver	what it really is
0	tiles	int(v * min(arable, n_units * hours * 0.5))	integer
1	animals	int(v * (n_units * hours - planted) / 3)	integer
2	workers	int(round(v * 15))	integer
3	sell_horizon	max(1, int(round(v * 2 * hours)))	integer
4	crop	viable[int(v * len(viable))], sorted by profit/day	categorical
5	expand	float threshold	continuous
6	stickiness	2.0 * v	continuous
7	fertilize	3.0 * v	continuous
8–13	six priorities	softmax(3v), only the ordering is read	one of 6! = 720 orderings
Three things fall out of writing that table honestly.

Twelve of fourteen outputs are discrete, and I gave all fourteen the same Gaussian head. That is a parameterization mismatch, not a tuning problem.

The priorities are the most quantized part of the vector, not the least. I had assumed the softmax made them continuous. It doesn't: softmax is strictly monotone, so sorting by softmax is identical to sorting by the raw value, and the only consumer reads the ordering. Six reals collapse to one of 720 orderings. The function's own docstring claims it returns a budget split between categories; grep says nothing in the codebase consumes those fractions.

The crop index is ambiguous across time. The viable list shrinks as days run out, so the same value means different crops on different days.

The three boundaries
boundary	symbolic (exact)	neural
movement	routes and distances	—
assignment	Hungarian over the matrix	the value map that feeds it
market	marginal prices, legality	how much, and in what order
The head decides what and how much. Never how or where to go. Movement is not a verb the network can emit — routing is exact, so asking for NORTH/SOUTH would be guessing something computable. PASS is not a logit either: the executor emits it when a unit has no legal options.

The verb vocabulary was 15 operations at the time of writing (it is 19 now, one PLANT per crop — see the update below):

PLANT  WATER  HARVEST  FERTILIZE  DIG  FEED  CARE  COLLECT_FERTILIZER
PLACE  BUILD_COOP  BUILD_PASTURE  PICKUP_ANIMAL  PICKUP_WHEAT
PICKUP_FERTILIZER  DROP
PICKUP is split by object because the quantity depends on the object. Treating it as an argument-less verb emitted 1 every time, where the heuristic takes min(hungry_animals, wheat_in_shed). Livestock ate at half speed. Fixing it raised that mode's ceiling from $26,536 to $40,763.

What the policy emits today: 64 numbers, not 14
The table above is what the first version of this post described, and its three conclusions are exactly what drove the redesign. Here is the current vector:

  8   levels        how much of each thing (tiles, animals, hands, selling,
                    crop bias, expansion, stickiness, fertilising)
  6   priorities    what gets sacrificed when cash does not cover everything
 36   exposed       the constants that used to be hand-written, borderless
  9   market        one multiplicative factor per product over its sale value
  5   turn rule     coefficients of a rule EVALUATED EVERY TURN (see below)
 --
 64   reals in [0,1], emitted once per day
plus the per-tile map, which is now 1 + 19 channels over 10x10 = 2,000 Gaussian dimensions: one value channel and one logit per verb, with one PLANT verb per crop rather than a single PLANT whose crop a hand-written function chose.

That last change is not cosmetic. With a single PLANT verb the network could choose whether to plant and never what, and no downstream head could repair it: the market head cannot sell what was never produced — measured, moving the strawberry factor with a single plant verb does not change a single dollar.

The daily/per-turn split, which is how you get per-turn reactivity for one forward pass a day. One RL step is a day: the network is called once and the symbolic layer plays 24 turns. That makes credit assignment tractable and it fits a competition with one second per turn. The cost is that everything learned is constant within the day — including when to sell, which is the one decision that genuinely depends on the turn.

So the policy emits a rule, not a level:

factor_p(t) = level_p * exp( w_price*x_price(t) + w_rival*x_rival(t)
                           + w_shed*x_shed(t)   + w_season*x_season(t)
                           + w_cash*x_cash(t) )
Five signals, dimensionless and centred on zero (expected price drop, share of the imminent flow that is theirs, storage pressure, how far the season has run, how much wealth is tied up in goods). The daily pass emits the five weights; the rule is evaluated against each turn's state. Weights default to 0, so at f = 0.5 the factor collapses to the level and the behaviour is exactly the previous one.

One mode, on purpose
There used to be three ways of combining the map with the heuristic valuation (residual, direct, ops) so they could be measured against each other. They are measured: the one where the network emits value and verb is the only one with complete learning freedom, and it is the only one left. Deleting the other two, the greedy assigner, the route assigner and a verb-sampling path left the result identical to the dollar on a 30-day two-rung probe. Dead code that runs is worse than dead code that does not: it is surface for a bug to hide in, and it is what made a league opponent silently weaker than it looked (see the meta-lesson).

Nothing guessed: the part that changed since the first version
The first version of this post said the policy emits 14 numbers. It emits 64, and the extra 50 are not a bigger network — they are constants that used to be written by hand in the symbolic layer and are now learned. That turned out to be the highest-paying single thing in the project, so it deserves its own section.

The rule. Any value that cannot be derived from the engine is a candidate for learning. Not "any value that looks important" — any value. A threshold, a multiplier, a reserve, a floor, a softmax temperature. If the engine does not force it, somebody chose it, and "somebody chose it" is the definition of a guess.

What it paid, measured in three passes:

exposing 14 module constants               cell ceiling:  $939 -> $1,258   (+34%)
exposing 4 literals inside function bodies two of them worth +-22% each
exposing 8 structural decisions            four live, between +23% and +71%
exposing 5 valuations inside `tile_task`   what a feeding, a trip, a watering is worth
Why grep is not enough, and what to use instead. Searching for ^[A-Z_]* = finds SAT_HIGH = 0.85. It does not find a min() that is an impassable ceiling, a loop that splits a budget by weight and throws away the remainder, or a hand-written preference order. Those are shapes, not numbers. So the audit walks the AST and prints every decision site — thresholds, min/max/sorted, and any arithmetic against a float literal — for manual classification. On the current tree it reports 65 sites across ten modules, and engine facts (spec.*, numerical guards) are exempted by name so the list stays readable. tools/audit_decisions.py

Borderless parameterization, which is the part I would steal. The obvious encoding for a learned constant is value = lo + (hi - lo) * f. That is two more hand-set numbers per parameter — 72 of them, for the 36 I have — and, worse, a hard floor and ceiling: if another league or another opponent needs a value outside, the model cannot even express it. Measured: one parameter pinned itself to the floor in 5 of 8 learned vectors, which is the signature of a wall, not of an optimum.

positive   value  = default * exp(logit(f))             # (0, +inf)
fraction   value  = sigmoid(logit(default) + logit(f))  # (0, 1)
additive   weight = logit(f)                            # (-inf, +inf)
f = 0.5 returns the exact previous default, so exposing a constant is behaviour-preserving by construction and any change is attributable. And there is no scale constant left over: since the head emits macro_mu and everywhere f = sigmoid(macro_mu), logit(f) == macro_mu exactly, so the multiplier that would sit in front is 1 because sigmoid and logit cancel, not because somebody picked it.

Two failure modes, in opposite directions, both found by audit and not by reading.

A live constant nobody is learning. Two parameters were exposed in the dataclass, given a slot in the vector and emitted by the network every single day — and the function that writes parameters into the symbolic layer never wrote those two. The softmax temperature over the priorities stayed pinned at 3.0 and the seed floor at 2.0 for the whole project. The network was paying to emit two dimensions that decided nothing, and two hand-set constants survived the "nothing guessed" rule by being almost exposed.

A learned dimension nobody is reading. The mirror image: residual_cap was emitted, resolved, written to a module global — and nothing read that global any more, since the mode it belonged to had been removed. A dead dial costs a dimension of policy entropy and a row of the KL budget, forever, invisibly.

The general form is worth stating once: exposing a constant is not the same as wiring it. Check both ends. Reading the code will not tell you — perturb the value and measure whether a dollar moves.

Where it stood at the first version
Honest numbers as of the first version of this post, so nobody has to infer them. Deterministic, 24 matched seeds, both seats, full game, against v48-fast-routes uncapped:

                        seat     ours       sd      v48    margin   wins
net (PPO)                  0   36,695   16,099  123,032   -70.2%   0/24
net (PPO)                  1   38,489   14,769  123,333   -68.8%   0/24
executor + search macro    0   38,011   18,560  123,037   -69.1%   0/24
executor + search macro    1   41,226   19,086  125,474   -67.1%   0/24
inaction                   0    3,000        0  145,080   -97.9%   0/24
Three things I have to own.

The learned policy does not beat the derivative-free search over the same 14 numbers — 36.7k/38.5k against 38.0k/41.2k, inside the noise. Conditioning on state bought nothing measurable over one fixed vector. The entire premise of the project is that it should. That premise is still unmeasured in its favour.

Against the uncapped public agents, zero wins. Against the handicapped ladder in Trick 7, comfortable wins at caps 3 and 5 and a true crossover at 8.

Seat makes no difference, and I had never checked until someone asked.

Where it stands now
Two measurements, both current, both against opponents outside the training loop.

Against an uncapped v48-fast-routes, full game, 8 fixed seeds, the external yardstick that exists precisely because self-play margin is not comparable across time:

checkpoint          upd     ours      v48    margin   wins
best by return      340   48,035  115,305   -58.3%    0/8
latest              900   46,342  139,972   -66.9%    0/8
560 updates of training moved neither number outside the noise on our side, and the opponent's own money moved more than ours did — which is the shared-market effect again: what changes their score most is how much product we keep off the market.

Where the money is missing, same opponent, 4 seeds, gross sales per product:

product        ours $    v48 $      gap
STRAWBERRY     13,853   53,023  +39,170
WOOL           11,482   31,110  +19,628
MILK           21,786   30,814   +9,028
FERTILIZER      9,904   18,336   +8,432
MELON          10,556   16,646   +6,091
WHEAT          11,269   13,099   +1,830
EGG             9,099        0   -9,099   <- we out-sell them
TOTAL          89,022  165,226  +76,203
77% of the gap is two products. That is the same shape as the measurement that motivated the market head in the first version — then it was strawberries and milk at 84% — and milk has closed from a third of the gap to $9,028 since the portfolio stopped being monoculture. Strawberries have not moved.

It is worth being exact about what this says: the gap is production, not timing. We plant about as much as they do and keep a third of the live plants, so the market head cannot fix it — there is nothing in the shed to sell.

Part II — the tricks
Eleven of these were in the first version; 12-14 are new. The numbering is kept so the comments below still line up.

Trick 1: marginal prices, not nominal
Three separate times I lost 40-66% of final money to the same bug class: valuing a batch at the nominal price. Each unit you sell moves the price of the next one.

Valuing 26 eggs at $50 each made animals look profitable when they weren't. With nominal pricing the agent bought animals on day 14 and money went from $4,310 to $345. The same bug bit the fertilizer bonus and the DROP action.

If you value anything in bulk, sum the marginal prices.

Trick 2: the hour-0 trap
len(farm["hands"]) is always 0 at hour 0 — workers are cleared overnight and rehired in hours 0-3. If you plan your day at hour 0 (which is natural), every capacity calculation that uses your current worker count is computing with 1 unit.

This bit me eight separate times in different files. Symptoms: a farm that couldn't grow past 12 tiles no matter what; rival statistics reporting "1 unit" for an agent hiring nine; and an observation encoder where 31 of 88 global features had zero variance, because they are all zero at that exact moment.

Measured at hour 0 versus every hour:

hour   workers   items carried
  0      0.00        0.00
  1      7.90        3.87
 12      9.33       33.17
If you sample state, declare which hour you sampled at.

Trick 3: paired comparison, or don't bother
Per-seed standard deviation of final money is about $9,000. Almost every A/B you run is under-powered.

Clone the state, run both branches with the same seed and the same opponent, and difference them. Measured variance reduction: 2.2x in sd, roughly 4.8x fewer samples for the same precision.

This is how I found the biggest single result in the project — and one I did not expect.

And there is a stronger version I only found at the end. When both things you want to compare can live in the same episode, put them there. A commenter asked whether I had evaluated on both seats — i.e. as player 0 and as player 1 — and I hadn't. My first attempt ran my agent in each seat against a fixed opponent in the other: two separate experiments, seed variance in both, paired standard error ~3,300 on an effect I was hoping was ~2,000. Useless.

The right design puts the same policy in both seats of one episode. Now the seed, the board and the market are literally shared, not merely matched:

                           paired sd     what it can resolve
two experiments, matched      ~15,000     nothing under ~30,000
same episode, both seats        2,566     down to ~1,000
Same question, 6x more resolving power, same compute. The answer, over 60 seeds: +228 +- 331. No seat advantage. Thirteen of the sixty tie to the dollar, which is what tells you the asymmetry is divergence rather than bias.

One more thing, and it is the reason this trick exists. My first twelve seeds said +1,497. Sixty fresh seeds said +228. The small sample I looked at first inflated the effect 6.5x. This happened to me while writing the reply to that comment, after having written this section.

The result that reframed everything
I swept my crop-density lever with paired comparison over 8 seeds, against the same opponent throughout:

density   my money   opponent   plantings   paired delta
 0.004     62,416     13,852        0            —
 0.100     20,780     33,460       55       -41,637 +- 4,941   (8.4 sigma)
 0.500     12,202     33,008       59       -50,214 +- 4,695   (10.7 sigma)
Farming cost me 41-50k, at 8-11 sigma. Not a bug — economics. Crops displace the animal economy: without farming I sold 831 units of product (fertilizer/eggs/milk/wool); with farming, 316. Moving, watering and planting eat roughly 68% of actions to produce less.

So my CEM search wasn't broken when it drove crop density to zero. It found the true optimum of my executor. Every number I had measured before that was ceilinged by a strategy that doesn't farm.

Trick 4: imitation accuracy does not predict performance
I tried cloning the top public agents. Twice, with two different architectures.

Behavior cloning, per-tile verb: 99.4% held-out accuracy (52.7% baseline), two minutes of GPU. Resulting agent: $3,036-6,727 — worse than picking a random legal verb.

DAgger, per-unit policy, 103k samples, 12 rounds, beta annealed to 0 so the policy drives and the expert only labels: 99.67% agreement. That is textbook Ross-Bagnell against distribution shift. Resulting agent: -99% margin, 0 wins in 24 games.

Correction, added after a comment asked the right question. That 99.67% is measured on the aggregated DAgger buffer — every round pooled, including round 0, which is pure expert — not on fresh autonomous rollouts of the final policy. I originally wrote "on its own states," and that is misleading.

Worse, it is the accuracy of one head. The loss supervises four targets (op_target, crop_target, item_target, market_target) and the only accuracy I ever logged was acc_op, the per-unit operation. Market loss was logged as a loss and never as an accuracy, so hiring and purchasing accuracy were never measured at all — which is exactly where other people report their first divergences. Given that this section's whole argument is that agreement measures the wrong thing, breaking it down per head was the obvious next step and I skipped it.

Near-perfect imitation, near-zero money, twice, by independent routes.

Diagnosis of the first one: 86% of actions were PASS, because the network chose PLACE on 95% of tiles and nobody was carrying the animal. Agreement-with-expert measures the wrong thing — you nail the marginal label and lose the chain.

Trick 5: calibrate your floor before training anything
Three baselines are worth having at every horizon. Measure them against the opponent you will actually train against — see the note below, because I got this wrong myself.

do nothing (keep starting cash)          $3,000
fixed random verb ranking                  $397
random LEGAL verb, re-picked each turn   $8,692
hand-written heuristic                  $30,065
Two things fall out. First, there is real gradient from scratch: random-legal is 2.9x doing nothing, so RL is not starting blind. Second, and more useful: a fixed ranking scores $397 and re-picking each turn scores $8,692, 22x apart. The correct operation depends on state in a way no fixed ordering captures — which is exactly what a hand-written heuristic is. That's a measured argument for learning the verb, not an aesthetic one.

Caveat, and it's my own mistake. The middle two rows were measured against a weak scripted opponent and the last row against a strong public agent. That makes the column not strictly comparable — the exact error this post warns about at the end. The 22x contrast between the two random policies is internally valid because both were measured the same way; the absolute levels across rows are not.

Trick 6: three bugs that made PPO not work at all
These cost me most of a night, and all three were invisible in win-rate and money curves.

Importance ratios were pure noise. The micro head emits 1+15 channels over 100 tiles = 1,614 Gaussian dims, but only ~40 influence any action. All 1,614 entered exp(logp - logp_old). Measured: 99.4% of ratios saturated at the +-10 clamp after one gradient step. Masking to action-relevant dims: 0.1%. Dimensions that cannot change the action must contribute exactly zero — that is not a design choice, it is a bug.

How the mask is built, since a commenter asked and it is the part that makes it practical: the symbolic layer already knows. It is the executor that enumerates the legal operations of each tile, so while it plays the day it records two things per tile — whether the value channel was read at all, and which verb logits were actually compared against each other. A verb's logit only matters if there was something to compare it with, so a tile with one legal option contributes its value channel and no verb dimension. The mask comes back with the rollout and multiplies the per-dimension log-probs before they are summed. No heuristic, no threshold: the mask is a by-product of the legality enumeration that had to happen anyway.

The critic was mis-scaled, not mis-trained. smooth_l1_loss(value, returns) with beta=1.0, on returns with mean ~20 and sd ~8. Every error above 1 unit sits in the pure-L1 regime: gradient +-1, carrying no magnitude information. Toy regression with a perfectly linear signal at that scale: R2 = -16.6 raw versus +0.83 with a normalized target. Normalize your value target.

The critic and the policy fought over a shared trunk. I lowered the trunk LR to stop the critic yanking the policy — and the critic's R2 went from 0.675 to -0.405, because it lives on those same now-frozen features. Then I raised it and the policy collapsed below do-nothing in 25 updates. The fix was a KL-targeted LR controller: measure KL per dimension each epoch, cut LR 30% if over target, raise 10% if under. Stop hand-tuning a number you are already measuring.

After all three, critic R2 went -0.405 to +0.698, and money passed the hand-written heuristic for the first time.

That last clause needs qualifying, and the qualification is the interesting part. It passed the hand-written macro, which plants — and by this post's own headline result, planting costs 41–50k. Against a derivative-free search over the same 14 numbers, it did not pass. See "Where it ended up" below.

A fourth instance of the same bug, found much later. The masking fix above applies to the per-tile head. The 14-number macro head has the identical problem and I never noticed, because I was looking at the head that had already burned me. Sweeping each macro axis independently at one rung, 8 of the 14 dimensions are exactly flat — they cannot change the action, they carry no gradient, and every one of them was entering the importance ratio as noise.

The general form, which is the part worth taking away: any dimension that cannot change the action must contribute exactly zero to the ratio. Having fixed that once in one head does not mean you have fixed it. Check every head.

Trick 7: build a ladder, because there isn't one
The public agents are all roughly equal strength, so you train at either 0% or 100% win rate — no gradient either way.

Throttling them does not work: making an agent PASS on 20% of turns drops it from $179,514 to $312. These are tightly-coupled plan executors, not reactive policies — drop one turn and the unit is in the wrong place, the plant dies, the animal starves.

Capping how many workers they can hire does work, because their own logic sizes itself to the unit count:

hire cap    money vs passive
    3            16,049
    5            43,094
    8            80,932
 none           179,514
That gives a real ladder with a genuine crossover point.

And I never ran my own best agent against it, which I only noticed when a commenter asked about final evaluation. The ladder had been sitting there for weeks. Using the search-optimum vector, training nothing, 12 seeds:

hire cap     ours      v48     margin    wins
       3   62,556    4,229  +1379.2%   12/12
       5   52,174   27,882     +87.1%   12/12
       8   49,106   58,765     -16.4%    5/12    <- the crossover
      11   39,990  110,859     -63.9%    0/12
    none   37,673  124,276     -69.7%    0/12
So the ladder works, and cap 8 is a real 50/50. Note also that my money barely moves across it (62.5k to 37.7k) while the opponent's moves 30x. Capping them both weakens them and frees market for me — which is the shared-market effect again, and a reminder that a handicap changes both sides of a shared economy, not one.

Trick 8: self-play can converge on doing nothing
This one is worth the whole post. I built a league that promoted on win rate against a frozen snapshot of itself. It ascended through four leagues with a win rate near 1.00.

Actual money at every league: $3,000. Starting cash. Exactly.

The frozen opponent was making $2,588 — worse than inaction. So beating it required doing nothing, and automatic promotion propagated that upward, league after league. An external check against the fixed public agents showed real margin going -82.7% to -98.3% while self-play reported winning.

Two guardrails I would now consider mandatory:

Log money relative to doing nothing. It is free to compute, and 1.0 means your policy is inert. Four separate collapses would have been caught in one glance.
Keep a fixed external opponent entirely out of the training loop and measure against it on a timer. Self-play money is relative; it tells you nothing absolute. Mine caught the collapse in 20 minutes.
Trick 9: horizon is not a difficulty axis
I assumed shorter games were an easier curriculum. They are a different game. The CEM-optimal worker count by horizon:

 5 days   0.057
 8 days   0.610
30 days   0.378
Non-monotonic. At 5 days a hire never repays its Fibonacci cost; at 8 it does and you hire hard; at 30 the optimum rebalances toward livestock. A horizon specialist beats a transplanted 30-day policy by +31% at 5 days and +70% at 8.

Worse, my time features were day / N_DAYS and step / EPISODE_STEPS — both normalized by the current episode length. A 5-day game and a 30-day game produce the same 0-to-1 signal. Sequential horizon training just averages incompatible strategies over identical inputs.

Two changes are needed, and I want to be precise about which does what. Adding an absolute horizon feature (EPISODE_STEPS / 720) makes the horizon identifiable. Mixing horizons within the same batch rather than in sequence makes it worth using. I tested the first one alone, keeping the curriculum sequential, and got the identical -98.3% — because sequential training forgets regardless of what the policy can see. Nothing in the gradient asks it to remember.

Trick 10: your sample yield is probably terrible
per episode:  17,280 engine steps  ->  30 policy decisions
per update:   4 full-batch gradient steps, then the data is discarded
The bottleneck is not steps per second, it is how many independent terminal outcomes you extract per unit of compute. Shorter episodes do not reduce engine cost per decision — 24 turns either way — but they do double your terminals per second, and with per-seed sd around $9,000, terminals are the scarce resource.

Trick 11: sweep one axis at a time — the diagonal lies
I swept the straight line in strategy space from "do nothing" to the search optimum, 48 seeds per point, and got a clean and dramatic picture: a flat plateau for 95% of the path, then 1.13x -> 5.11x in a single step. A cliff. I was one paragraph away from concluding that the reward landscape is piecewise-constant and gradient methods are structurally blind here.

Then I swept one axis at a time from the same optimum, and the picture was completely different (values are multiples of doing nothing):

workers    1.00 1.50 1.37 2.29 2.75 3.16 3.59 3.59 4.83 4.83 5.10 ...  10 improving steps
crop       1.00 0.39 0.39 0.39 1.04 1.04 1.08 1.08 1.03 ... 1.03 5.10  the actual cliff
tiles      0.70 1.16 4.30 5.10 4.98 ... 2.37 0.00 0.00 0.00            a cliff downward
animals    5.10 2.73 1.85 1.73 1.53 ...                                monotone worse
sell_horizon, fertilize, all 6 priorities: 5.10 flat, ONE level
A diagonal moves every coordinate at once, so what it draws is a curve, not the landscape. Worker count has ten improving steps — there is plenty of gradient. The cliff is one variable, the crop choice, and it is a categorical decision encoded as a scalar: viable[int(v * len(viable))]. Crossing 0.75 flips one crop to another and the money goes 1.139x -> 4.841x. Planting the wrong crop scores 0.39x, which is 61% worse than doing nothing.

My first write-up of this said the cliff was the worker count going 8 to 9, because that is what changed a couple of grid points later. It contributes 0.26x of the 3.97x jump. I attributed 93% of an effect to the wrong variable because I read a one-dimensional slice of a fourteen-dimensional object.

If you take one thing from this post, consider taking this one: it is cheap, it is mechanical, and it would have saved me a day.

Trick 12: dead dials, in both directions
Covered above under "nothing guessed", stated here as a trick because it is the cheapest check in this list:

for every learned parameter, grep the global it writes and confirm something reads it;
for every hand-set constant, confirm it is actually written by the resolver;
then perturb it and confirm a dollar moves.
Reading the code catches neither direction. In this project one dead dial survived months because the mode it served was deleted around it, and two live constants survived because they had a dataclass field and no wiring, which looks like being learned in every diff you read.

Trick 13: a default argument is how a rename becomes a silent no-op
The per-turn selling rule reads its five weights like this:

return {k: _logit(getattr(macro, "w_" + k)) for k in TURN_WEIGHTS}
It used to be getattr(macro, "w_" + k, 0.5). With the default, renaming a field and forgetting the key tuple makes the lookup fall back to the neutral value: the whole per-turn rule switches itself off, no error, no log line, and the training curve keeps looking plausible because 0.5 is exactly the value that reproduces the old behaviour. It cost a bisection down to a single turn (SELL CARROT 19 against 23) to find.

The fix is one character: drop the default. An AttributeError is the correct outcome of a rename you did not finish.

Trick 14: the code that is running is not the code on disk
A 15-minute search starts; you keep editing the executor while it runs. The workers imported their modules when they were spawned, so they are measuring a world that no longer exists, and the vector that comes out is the optimum of a version of the code that is gone. Nothing in the output looks wrong.

Two cheap defences, both in the repo:

A fingerprint of the files that decide how the game is played, stored next to every vector and every checkpoint, printed at startup. Two of them, actually: one over the game files and one over the learning files, kept separate so a CEM vector stays comparable when the network changes — the game has not — while two checkpoints do not.
Loud checkpoint loading. The usual pattern — {k: v for k, v in sd.items() if k in cur and cur[k].shape == v.shape} — silently drops every tensor whose shape moved and leaves it randomly initialised. That cost half a session once: the two dropped tensors were the global encoder and the summary vector, so per-seed money ranged from $19 to $40,667 and the same checkpoint gave different answers in different processes. Migration should be explicit and it should raise.
There is a corollary I hit while removing the dead dial above. If you ever remove a dimension from a vector the network emits, every row after it in older checkpoints now means something different. Growing a head is routine; shrinking one has to delete that specific row before growing, or the load silently reinterprets 28 dimensions. New checkpoints now carry the field list itself, so no width is ever guessed by position again.

The meta-lesson
Of the confident diagnoses I made in one session, five were wrong, and measurements killed all five:

capping units does not speed anything up (cost scales with tiles, not units)
shrinking exploration sigma cancels out under a KL budget
cloning experts does not transfer
short horizons are not easier
my "validated" league opponent was silently crippled by a global mode flag that the training loop had set
the reward landscape is a flat plateau with one needle (it is not — that was a diagonal slice; see Trick 11)
I had never beaten a public agent (I had, comfortably, under the handicap I built myself and never used)
The habits that actually paid:

Assert your patch matched before writing it.
Verify by symmetry — run the same policy on both sides and check the wiring is live. I wrote here that mine tied "to the dollar"; measured properly, only 13 of 60 seeds tie exactly. Identical strategies still diverge, because the two farms occupy different positions and the market couples them. An exact tie proves the wiring; a failure to tie proves nothing on its own.
Log the thing that would explain a failure, not just the thing that is the failure.
Never compare money measured against different opponents. The same agent varied 2x for me depending on who it played. In a shared-market game that is not a strong enough rule: measured, v48 earns 123k against my active policies, 145k against inaction and 158k against the farming one. My own behaviour moves my opponent's score by 28%, because selling less product keeps their marginal prices high. So margin-vs-opponent is not comparable across my own arms either. Report absolute money against a policy-independent baseline — I use multiples of doing nothing.
Write the success criterion down before looking at the result.
Glossary
Neurosymbolic split. Exact arithmetic for anything derivable from the engine (legality, routing, assignment, prices, liquidation); learning for anything that depends on state in a way you can't write down. The test is not "is this complicated" but "can I compute this exactly?"

Borderless parameterization. Encoding a learned constant as default * exp(logit(f)) (or the sigmoid form for fractions) instead of lo + (hi-lo)*f. f = 0.5 reproduces the default exactly and the extremes reach the whole domain, so exposing a constant cannot change behaviour by itself and no hand-set range is introduced along with it.

Decision site. Anything in the code that picks a number or an order: a threshold, a min used as a ceiling, a sorted used as a preference, an arithmetic scale. The unit the AST audit enumerates, because grep only finds the ones that happen to be named constants.

The per-turn rule. The policy is called once a day, so anything it emits is constant within the day. For selling — the one decision that really depends on the turn — it emits the coefficients of a rule instead of a level, and the rule is evaluated against each turn's state. Reactivity without 24x the forward passes.

Macro / micro. Macro: a daily strategy vector — 64 reals: how much of each thing to aim for, plus the constants that used to be hand-written. Micro: a per-tile head emitting a value plus one logit per legal verb. Macro says how much, micro says what, where.

Hungarian assignment. Optimal one-to-one matching of units to tiles given a value matrix. Greedy fails in a specific way: the first unit takes a task another was equally close to, stranding it — and unit ordering is meaningless, so that loss is pure arbitrariness.

Marginal price. The price of the k-th unit sold, not the first. Any bulk valuation must sum marginal prices. Getting this wrong cost me 40-66% of final money, three separate times.

CEM (Cross-Entropy Method). Derivative-free search: sample N candidates, keep the best K, refit a Gaussian to them, repeat. Good for the 14-number macro vector, where no gradient reaches. Its ceiling is that it finds one fixed vector and cannot condition on state.

PPO. On-policy gradient method: reuse a batch for a few epochs, then discard it, because once the policy moves the old data is invalid. That is why sample yield matters so much here.

Importance ratio. exp(logp_new - logp_old). It is a product over sampled dimensions, so dimensions that cannot affect the action do not cancel — they multiply the noise.

Critic / R2. The value function predicting returns; its accuracy is what turns raw returns into low-variance advantages. Negative R2 means it is worse than predicting the mean, and PPO degenerates to REINFORCE with no baseline.

Potential-based shaping. Adding gamma*Phi(s') - Phi(s) leaves the optimal policy unchanged for any Phi — but only over full episodes. Under truncation Phi becomes the terminal value, and an optimistic Phi teaches the wrong thing.

BC / DAgger. Behavior cloning is supervised learning of expert actions. DAgger is the standard fix for distribution shift: your policy drives, the expert only labels. Both hit ~99.5% agreement here; both produced near-zero money.

Common random numbers (paired comparison). Run both branches from the same cloned state, same seed, same opponent, and difference them. Seed variance cancels instead of being averaged over — 2.2x less sd, roughly 4.8x fewer samples.

Terminal. One completed episode: one unbiased outcome. With per-seed sd around $9,000, terminals are the scarce resource — not steps, not transitions.

Self-play with a frozen snapshot. The opponent is a copy of you from K updates ago, so "winning" is meaningful rather than 0.5 by construction. Only if the snapshot is better than doing nothing — mine wasn't, and the league happily promoted a policy that sat on its starting cash.

Happy to go deeper on any of these in the comments.

References
The techniques this post leans on, in the order they appear.

Hungarian assignment. Kuhn, H.W. (1955), The Hungarian method for the assignment problem, Naval Research Logistics Quarterly 2(1-2).

Common random numbers / paired simulation. Standard variance-reduction technique in discrete-event simulation; see Law & Kelton, Simulation Modeling and Analysis, ch. 11. The idea is older than RL and underused in it.

Cross-Entropy Method. Rubinstein, R.Y. (1997), Optimization of computer simulation models with rare events, EJOR 99(1); and De Boer, Kroese, Mannor & Rubinstein (2005), A tutorial on the cross-entropy method, Annals of OR 134.

Behavior cloning and covariate shift. Ross, S. & Bagnell, J.A. (2010), Efficient reductions for imitation learning, AISTATS. The quadratic-in-horizon error compounding result is here.

DAgger. Ross, S., Gordon, G. & Bagnell, J.A. (2011), A reduction of imitation learning and structured prediction to no-regret online learning, AISTATS.

PPO. Schulman, J., Wolski, F., Dhariwal, P., Radford, A. & Klimov, O. (2017), Proximal policy optimization algorithms, arXiv:1707.06347.

Generalized advantage estimation. Schulman, J., Moritz, P., Levine, S., Jordan, M. & Abbeel, P. (2015), High-dimensional continuous control using generalized advantage estimation, arXiv:1506.02438.

Potential-based reward shaping. Ng, A.Y., Harada, D. & Russell, S. (1999), Policy invariance under reward transformations, ICML. The policy-invariance guarantee — and the full-episode assumption that quietly breaks under truncation.

League training and frozen opponents. Vinyals, O. et al. (2019), Grandmaster level in StarCraft II using multi-agent reinforcement learning, Nature 575. The main/exploiter/league structure, and why a single frozen snapshot is not enough.

Catastrophic forgetting. McCloskey, M. & Cohen, N.J. (1989), Catastrophic interference in connectionist networks, Psychology of Learning and Motivation 24; French, R.M. (1999), Catastrophic forgetting in connectionist networks, Trends in Cognitive Sciences 3(4).

Further reading, informed the design but isn't in the post
These came out of a literature pass while debugging the critic and the imitation failures. I have not independently verified every one, so treat them as pointers rather than endorsements.

Value target scaling. van Hasselt, H., Guez, A., Hessel, M., Mnih, V. & Silver, D. (2016), Learning values across many orders of magnitude (PopArt), NeurIPS. Relevant because bootstrapped targets make naive normalization unsafe.
Categorical value heads. Farebrother, J. et al. (2024), Stop regressing: training value functions via classification for scalable deep RL, ICML.
Decoupling value and policy. Raileanu, R. & Fergus, R. (2021), Decoupling value and policy for generalization in RL (IDAAC), ICML; Cobbe, K., Hilton, J., Klimov, O. & Schulman, J. (2021), Phasic policy gradient, ICML. Both are about the shared-trunk interference described in Trick 6.
Value-based imitation. Garg, D., Chakraborty, S., Cai, C., Zhang, B. & Ermon, S. (2021), IQ-Learn: inverse soft-Q learning for imitation, NeurIPS; Al-Hafez, F. et al. (2023), LS-IQ, ICLR, which documents and corrects its reward bias.
Search with an exact simulator. Silver, D. et al. (2018), A general reinforcement learning algorithm that masters chess, shogi and Go through self-play, Science 362; Danihelka, I., Guez, A., Schrittwieser, J. & Silver, D. (2022), Policy improvement by planning with Gumbel, ICLR. Worth reading before reaching for a learned world model when you already have the real one.
Entity-based architectures. Vinyals et al. 2019 (above) for the transformer over units; Lee, J. et al. (2019), Set Transformer, ICML.

3

3
4 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Syed Asad Ali
Posted 6 days ago

· 36th in this Competition

Thanks for sharing the negative results and the implementation details. The BC/DAgger section particularly resonated with our experiments.

We recently trained a recurrent BC policy on 32 games from one public teacher. It reached 92.7% whole-turn agreement on training replays and 69.7% on held-out replays, but autonomous bank retention averaged only 25.8% across 16 fresh games against a fixed, responsive opponent. First divergences included omitted hiring and seed purchases. Earlier, a single-game overfit reproduced all 719 turns autonomously—so passing that sanity check clearly wasn’t enough.

A few details from your approach would be especially valuable:

DAgger’s 99.67% agreement: Was that measured on fresh autonomous rollouts of the final policy or on the aggregated dataset? Did it include market decisions, and how accurate were hiring, purchasing and placement specifically?

Neural-to-symbolic interface: What connects purchases, pickup, routing, placement and subsequent maintenance? Does the executor retain persistent jobs or reservations, or recompute assignments each turn?

Action-relevant PPO dimensions: How do you determine the mask? In particular, how do you handle unselected tile scores that can still influence which assignment wins?

Final evaluation: After the PPO fixes, how did the final checkpoint perform against the named strong public agents on matched seeds and both seats?

Even pseudocode for the interface or relevance mask would be helpful. These seem like the details that could distinguish a coherent learned policy from high agreement that fails to preserve the underlying plan.


Reply

React
xaxipiruli
Topic Author
Posted 6 days ago

· 6135th in this Competition

@Syed Asad Ali — thank you. Your numbers (92.7% train / 69.7% held-out / 25.8% autonomous retention) are the same shape as mine, and checking your four questions against the code rather than my memory turned up three things I had wrong in the post. Short answers here; I've expanded the post with the detail.

1. The 99.67%. Aggregated buffer, not fresh autonomous rollouts — all rounds pooled, including round 0, which is pure expert. The post said "on its own states"; that was wrong and I've fixed it. And it's one head: I supervised four targets (op, crop, item, market) and only ever logged accuracy for the per-unit op. Market was logged as a loss, never as an accuracy, so hiring and purchasing accuracy were never measured at all. I can't give you the breakdown you asked for because I didn't record it — which, given that the whole section argues agreement measures the wrong thing, is a bit of an indictment.

2. The interface. Recomputed every turn, no persistent jobs, no reservations. The only state that survives the turn is yesterday's assignment, used as a soft stickiness bonus whose weight the policy sets (measured interior optimum: 0.0 → $23,793, 0.25 → $27,177, 1.0 → $22,755). Market orders are sequence-dependent and truncated at 10/turn, and the dropped ones fail silently — my BUY_LAND sat at the end of the list and never executed for weeks. Full pseudocode and the three symbolic/neural boundaries are now in the post under "The interface, concretely".

3. The mask. I don't derive it, I record it during play — which sidesteps exactly the problem you spotted. Every tile that entered the assignment gets its value dimension marked, winners and losers alike, because a losing tile was still in the cost matrix and did influence the outcome. A verb logit is marked only when there were ≥2 legal options at that tile; with one option the argmax is unconditional and the logit cannot change anything. Code is in the post.

4. Final evaluation. Against uncapped v48, 24 matched seeds, both seats: 0/24, margin −70%. Seat effect is null (and I had only ever played seat 0 until you asked — thank you). Two harder admissions: the learned policy does not beat a derivative-free search over the same 14 numbers, so conditioning on state bought nothing measurable; and I had written "never beat a public agent", which is false — against the handicap ladder I built in Trick 7 and then never used, the same vector wins 12/12 at hire cap 3 and 5, with a genuine crossover at cap 8.

One thing that may be worth more to you than any of the above. I'd written that the reward landscape here is a flat plateau with a single needle, based on a sweep from "do nothing" to the optimum. That sweep moved all 14 dimensions at once, so it drew a curve, not the landscape. Sweeping one axis at a time, the same optimum shows ten improving steps in one variable, a genuine cliff in another, a cliff downward in a third, and eight dimensions exactly dead. I had also attributed the cliff to the wrong variable — 93% of it was a categorical crop choice, not the worker count I named. It's now Trick 11 in the post, and it's the cheapest thing in there.


Reply

1
Sheeesh---
Posted 6 days ago

· 3115th in this Competition

either I'm dumb or you are using a lot of fancy words making this hard to understand


Reply

React
xaxipiruli
Topic Author
Posted 6 days ago

· 6135th in this Competition

Not you, me.

That's fair and I'd rather fix it than defend it. The post grew out of my own notes and kept the vocabulary of the notes.


Reply

React
Sheeesh---
Posted 6 days ago

· 3115th in this Competition

yeah, it's just that when people see posts like these they think it's way too complicated and get demotivated, but hey, thank you and i respect that you are trying to help and i don't mean what i say in any bad way


Reply

React
xaxipiruli
Topic Author
Posted 6 days ago

· 6135th in this Competition

Well, this problem is as complex as you want to make it, and honestly it's been helping me reflect on a lot of concepts. Let's see if I can update with results, metrics, and a bit more structured documentation in the coming days.


Rayk Kretzschmar · 1612th in this Competition · Posted 2 months ago
How path dependent is the current leaderboard rating?
I submitted two byte-identical agents approximately two hours apart. The first submission is currently around 1700, while the second, submitted 2h later, has climbed >3000. Because the submitted code is identical, this difference appears to come from matchmaking, seeds, player positions, and the order of early results, not agent quality. In particular, early losses seem to make subsequent climbing extremely slow.

A gap of roughly 1400 points between identical agents suggests that the current rating may be highly path-dependent, especially during the initial games. It may even incentivize repeatedly submitting the same agent in hopes of receiving a better early trajectory.

Has anyone else tested duplicate submissions or observed similar rating divergence? Does the rating system eventually converge given enough games?


React
10 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Rayk Kretzschmar
Topic Author
Posted 2 months ago

· 1612th in this Competition

I want to add that this is especially frustrating when an early loss happens because of a random weed spawn that only affects the own side. If early results strongly influence the subsequent rating trajectory, a single piece of bad RNG can have an outsized and persistent effect.


Reply

React
Victor Mercklé
Posted 2 months ago

· 35th in this Competition

In particular, early losses seem to make subsequent climbing extremely slow.

I think this is the biggest factor. It was less an issue when any new agents you'd submit would beat everyone except the top1. Now with more randomness it shouldn't be possible. You can measure how many hours you need to reach top1 by winning every game.

Also a big part of the pool currently is stale agents (for the old engine).


Reply

React
evnchn
Posted a month ago

· 4443rd in this Competition

Also a big part of the pool currently is stale agents (for the old engine)

Indeed, those are dropping out as we speak.

I wonder if all-reset-to-600 is more productive when a patch lands like https://www.kaggle.com/competitions/kaggriculture/discussion/735311 than leaving stale entries in the leaderboard to linger.

One might argue that increases the cost to a patch, but I'd say that's just the cost of a patch you're paying implicitly over the span of 14 days so it seems less impactful to issue the patch but doesn't mean the underlying impact isn't there to begin with.


Reply

React
Steve421471
Posted a month ago

· 2919th in this Competition

I think we're starting to develop a stratification problem. Last week I would submit an agent and it would win 30 matches in a row and break into the top 50 in 4 hours. Now I have agents that could compete at the top but are too specialized and can't win enough to get there. It'll be interesting to see where things go from here. I've not done a 2 identical agent experiment, but I do submit 2 at a time and the one I think is stronger sometimes ranks much worse.


Reply

1
destbreso
Posted a month ago

· 1228th in this Competition

I've been digging into this question, and I think the answer could be more nuanced than simply saying that the leaderboard is path-dependent.

My research suggests that the competition does not behave like a collection of independent players submitting isolated agents. That part is actually fairly obvious from simply observing the matches. What is less obvious is how those interactions shape the leaderboard and the dynamics that emerge from them.

Some of the things I've been able to observe are:

Emergent behavior from "interspecies" interactions: agents don't evolve in isolation. Their performance and adaptation are shaped by the population they repeatedly encounter.
A natural drift in results: an fixed agent can tend to move backward in the leaderboard over time, even without any change to its own code, as the surrounding population changes.
Reproduction and mutation: agents appear to be copied and adapted, creating lineages that can sometimes be traced through their replay behavior.
Strong specialization at the top: the dominant agents are highly specialized, but they don't appear to emerge from nowhere. They continue to operate on top of some underlying baseline that can often be traced back through their lineage.
I've written up some of this analysis here:

Dissecting the Top Two
A DNA Test for Agents
Mutants at the Top: Genetic Potential of a Replay
The Leaderboard Is a Habitat Gradient
So, regarding the specific observation of two byte-identical agents diverging by ~1400 points: yes, I think this is very plausible, but I would interpret it less as noise in the rating system and more as a consequence of the population dynamics and matchmaking path.

One analogy I've been using is that of a habitat. Imagine two genetically identical lions with exactly the same capabilities. One is born on a large grassland with abundant prey and a path to increasingly favorable territory; the other is born on an island separated from that ecosystem by a lake. The lion on the island may be just as capable, but it may never reach the same fitness; not because it is a worse lion, but because the path available from its starting point does not allow it to reach the same region of the landscape.

I think something similar may be happening on the leaderboard. An agent can have the same underlying "genetics" as a highly ranked ancestor, yet fail to reach that ancestor's rating because the sequence of opponents and results it encounters puts it in a different part of the landscape. Once the surrounding population adapts, some paths become effectively inaccessible: the agent may no longer have the adaptations required to cross into the next favorable region of the leaderboard.

In that sense, the leaderboard is not just measuring an agent's intrinsic strength. It is also recording the trajectory through an evolving ecosystem. Two identical agents can therefore start with the same potential but end up in very different places because they entered the habitat through different paths.

The more interesting question, in my view, is not whether the rating is path-dependent, but how much of that path dependence is generated by the evolving ecosystem of agents itself. My current evidence suggests that this appears to be a significant part of what we're seeing


Reply

React
Talvenn
Posted 4 days ago

· 498th in this Competition

I know this was discussed a while ago, but I can confirm it's still very much the case. Yesterday I submitted the same agent twice, a few minutes apart. 16 hours after submission, one copy was at 2678 and the other at 2374. The difference came from a single early loss: in its 10th game, the lower copy lost by 88 coins to an agent that had been submitted just minutes before, so its rating hadn't settled yet. That's roughly 300 points between two byte-identical agents, so yeah, the leaderboard is very much path-dependent!


Reply

React
evnchn
Posted a month ago

· 4443rd in this Competition

Another issue which the path-dependent leaderboard rating causes, is all the false "this notebook gets a 3k score" in the Code section, which is wildly over-claimed.

And that's with me already putting aside the fact that, had everyone used that same notebook, then nobody gets 3k.


Reply

React
evnchn
Posted a month ago

· 4443rd in this Competition

Very. IMO the initial few matches should not have such high weight.

I have a gap of 300 for identical agents, don't have as big as 1400, but the ideal, assuming a well-tuned ELO matching algorithm, should be a gap of 0 within reasonable time.

My approach to try and self-improve is to look at the rate of change of the part after the initial rush. It's not good that the competition now needs a proxy-metric to go forward. However, I do see compute-bound being the limiting factor here.


Reply

React
evnchn
Posted a month ago

· 4443rd in this Competition

Under the current leaderboard system, there can exist (though I wish not to point fingers), a group of people who repeatedly submit before rating truly settles, gambling on the initial rush for a high rating.

The rating definitely needs more than 24/5 = 4.8 hours to settle. I've seen 3k drop into 2k over the span of 4 days.

It can be safe to assume that, unless a patch is made, that because that group of people can exist, that everything should be taken with a grain of salt.


Reply

React
Belati Jagad Bintang Syuhada
Posted a month ago

· 3006th in this Competition

To be honest, I see no point (except for temporary satisfaction) of submitting repeatedly to get a lucky start and reach the top faster. In the end, once the competition's submission deadline has passed, all of the agents will start over from 600 ELO and have to climb back up.


Reply

4
This comment has been deleted.

Rayk Kretzschmar
Topic Author
Posted a month ago

· 1612th in this Competition

Do they start over? I read that they will "continue to run". Even if they start over completely, I think it's interesting to know if an approach is worth to keep improving or if it should be rejected. I like to iterate fast and don't want to wait a week to see where my agent ends up.


Reply

React
Belati Jagad Bintang Syuhada
Posted a month ago

· 3006th in this Competition

At least from my past experience with simulations competition (FIDE Chess Challenge), they will reset all the players ELO to 600 after the submission deadline and rerun the whole scoring system with more games per day. It happened with Orbit Wars, and probably will happen with Pokemon TCG too, so I don't doubt that they will start over in this simulation competition.

It sucks to have to wait, but these simulation competitions take a lot of their compute resource too so this is the best that they can do.


Reply

React
Mahog
Posted a month ago

· 6588th in this Competition

They didn't do the reset with Orbit Wars if I remember correctly


Reply

React
Belati Jagad Bintang Syuhada
Posted a month ago

· 3006th in this Competition

My bad then. If that's the case, it will most likely not reset from 600.


Reply

React
evnchn
Posted a month ago

· 4443rd in this Competition

Indeed there's absolutely no point other than temporary satisfaction to repeat-submit and leverage the chance of initial win streak for a higher rating.

That rating simply doesn't belong to the agent and will be slowly removed from the agent through the span of a few days (4 days, in the case of 3k->2k agent I've seen)

If you would like to actually deliver a good agent, repeated submissions should NOT be done.


Reply

React
Temitayo Gbolahan
Posted a month ago

· 2758th in this Competition

Pokemon TCG submission deadline was few days ago, did you check if it was reset???


Reply

React


Ana Riquele · 9283rd in this Competition · Posted 9 days ago
How do you decide which crops to plant?
Hello! Kaggriculture is my very first Kaggle competition, and I’m trying to understand which factors are the most important when deciding which crops to choose. I’ve thought about considering variables like selling price, productivity, seed cost, and growth time. However, I’m still unsure about how to balance all of this to find a method that truly maximizes returns. Which conditions or features do you consider the most important for this decision?


React
2 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Yang Kuang Ou
Posted 4 days ago

· 1234th in this Competition

One detail to include in the market part of your comparison: Kaggriculture quotes sales unit by unit. Selling changes the next quote, and same-turn sellers share the market state, so quantity × current price can misstate revenue—especially near the $1 floor. Compare the units you can realistically harvest and sell by summing the marginal quotes, then subtract seed/input costs and account for land time, labor, and the remaining season.

I made a small CPU-only, pure-Python Kaggriculture Price Lab with all nine public price curves, checks for all 36 published price anchors, and a reusable simulator for one or multiple same-turn sellers. It helps calculate the market-price part; it does not determine the best full crop plan or predict leaderboard strength.


Reply

React
Zukas F.
Posted 9 days ago

· 5836th in this Competition

I would start by estimating the profit each crop can generate and the resources needed to obtain it. The variables you mentioned are a good starting point, but I would also consider labor, market demand, and the time remaining in the season.

The main factors I would evaluate are:

Expected net profit: estimate the revenue from the yield you can realistically harvest and sell, then subtract seed costs and any additional spending on fertilizer or workers.

Land occupation: compare profit per tile per day. A crop with a high selling price may occupy the land long enough for several cycles of another crop to become more profitable.

Work required: include planting, watering, harvesting, and movement. A profitable crop is only useful if your workers can maintain it and collect its production on time.

Market conditions: estimate the price when you expect to sell. Town demand and both players’ production can change the return, especially when selling large quantities.

Cash and remaining time: keep enough money for ongoing operations and allow time to grow, harvest, and sell before the season ends.

As a first method, I would calculate expected profit per occupied tile-day, then check whether the planting plan fits the available labor and budget. If labor is the main constraint, profit per worker action becomes particularly relevant.

I would also compare crop combinations across several seeds and opponents. The aim would be to identify which crops work best under different conditions and adjust the planting plan as those conditions change.


Alex Paul · 1569th in this Competition · Posted 19 days ago
how much time does it take for submission to converge?
The previous top 1's discussion threads claim that 90% of games converge in the first 5 hours; some say it takes 48 hours.What is the actual number to be used to balance iteration speed too


React
9 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Georgy Mamarin
Posted 3 days ago

· 576th in this Competition

say4n is counting in runs and nouvya in hours, and those two units are further apart than they look. A fresh submission plays about fifteen games an hour for its first five hours and under three after that, so the five-hour mark is roughly seventy games, not five.

The curve behind that: every submission in the public episode record with at least sixty ladder games, 811 of them, 224,523 submission-games, through 23 September. Call the mean of a submission's last ten games the level it settled at, then ask how far it still was after each game:

after 5 games: the median is 718 points away
after 10: 338
after 20: 222
after 40: 145
At five hours the median submission is 123 points from where it ends up, and a quarter are still more than 400 away. So a hundred-point gap between two submissions at that point is smaller than the movement still to come.

Steve421471's "I don't think you can put a single number on it" is what the data backs. Split that 145 by how many games the submission eventually played: the ones that stopped between 60 and 100 games are 78 points from settled at game 40, the ones that reached 400 or more are 542. One curve over two populations, and any single answer averages them.


Reply

1
千早爱音
Posted 17 days ago

· 209th in this Competition

it depends. If you lose accidentally in a very low mark (like around 1000), this will really hurt your score and I recommend you to submit your agent again.


Reply

React
say4n
Posted 18 days ago

· 3327th in this Competition

Anecdata: I see it happening after ~5-10 runs unless it keeps climbing, then it takes longer.


Reply

React
nouvya
Posted 18 days ago

· 3316th in this Competition

Based on my experience, 5 hours should be enough to see roughly which position your agent is at. Though it's true that the agent may still increase its position on the board, but the score increment is diminishing if you are over 4 - 5 hours. So checking around 5 hours should be reasonable.


Reply

React
Steve421471
Posted 19 days ago

· 2919th in this Competition

I don't think you can put a single number on it. I've had agents that kept climbing for 4 days and I've had agents that peak after 4 hours and then fall continuously for 3 days.


Reply

1
This comment has been deleted.

Liu Classmate
Posted 19 days ago

· 1010th in this Competition

我认为差不多 24 小时之内就会收敛，你可以看胜率和最高战绩，多提交几次，很快就能验证的，如果数据分析你不敢下结论，你或许可以求助于 model


Reply

React
Mohit
Posted 16 days ago

4 hours probably


Reply

React
Pand
Posted 16 days ago

· 933rd in this Competition

5 hours is a good timestamp i'd say, even tho later on its kinda chaotic


Takamichi Toda · 1312th in this Competition · Posted 8 days ago
🪰 I let a fruit fly's brain play Kaggriculture
https://www.kaggle.com/code/takamichitoda/flyfarmer-connectome-plays-kaggriculture

Inside is real wiring from the Janelia MaleCNS v1.0 connectome (728 neurons, 35,704 synapses) with no learning at all. Farm chores go into the left eye, market opportunities into the right, and weeds plus the rival's cash lead arrive as a looming threat on the visual projection neurons (LPLC2 / LC4). The left/right difference of the descending neurons decides whether the fly looks at its farm or at the market.

Highlights:

The Giant Fiber (DNp01), normally the escape circuit, triggers panic selling. This fly only sells when it gets scared.
Shuffle the weights and the excitation/inhibition balance breaks, turning it into a farmer that sells every single turn.
The best earner is the brain-dead variant with all descending neurons silenced. It plants strawberries and waits.



7
3 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Rairo Mukamuri
Posted 6 days ago

· 601st in this Competition

This is an interesting approach. Well done.


Reply

React
Nakul Maurya
Posted 7 days ago

· 1483rd in this Competition

no way i just thought to make that one I thought it would be funny you already made it


Reply

1
Jules
Posted 7 days ago

· 1386th in this Competition

Wow, this is one of the most inspiring approaches I have ever seen.


María Cruz · Posted 2 months ago
·
Kaggle Staff
How to get started + Competition's Official Discord
Information for newbies
New to machine learning and data science? No question is too basic or too simple. Feel free to start your own thread, or use this thread as a place to post any first-timer clarifying questions for the Kaggle community to help you with!

New to Kaggle? Take a look at a few videos to learn a bit more about site etiquette, Kaggle lingo, and how to enter a competition using Kaggle Notebooks. Publish and share your models on Kaggle Models!

Looking for a team? Express your interest in joining a team through our Team Up feature.

Remember: Kaggle is for everyone. Whether you're teaming up or sharing tips in the competition forum, we expect everyone to follow our Kaggle community guidelines.

Competition's Official Discord
In addition to this competition forum, you can continue the discussion in our official Kaggle Discord Server here:

discord.gg/kaggle
The Discord is a great place to ask getting started questions, chat about the nuances of this competition, and connect with potential team mates. Learn more about Discord at our announcement here. Here are a few things to keep in mind though:

1. Discord Competition Channels are 'Public' - Don't Share Private Information

Discord channels for specific competitions are considered 'public' spaces where you are allowed to talk about competition details. Please remember that private sharing of competition code or data outside of your team is, as always, not permitted. Code sharing must always be done publicly through the Kaggle forums/notebooks.

2. Discord Competition Channels are Not Monitored by Staff - Keep Important Information on the Kaggle Forums

Kaggle Staff and Hosts running competitions will not monitor Discord or be available to answer questions in Discord. This is intended to be a more casual space to discuss competitions and help each other. Please keep important questions, insights, writeups, and other valuable conversation on the Kaggle forums.

Enjoy Kaggriculture!


React
11 Comments
1 appreciation comment
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Moksh Jain
Posted 2 months ago

what are the supported models we should be using for inference ? should we use the kaggle models, are we allowed/ is it recommended to use external inference API's from openai or something ?


Reply

React
Moksh Jain
Posted 2 months ago

are we even allowed to use llm's here , or is it more like a proper coded model that we are following ?


Reply

React
Ahmed Jendoubi, Ph.D.
Posted 2 months ago

Excited to join Kaggriculture!

Hello everyone,

I am joining this competition with a strong interest in exploring how AI can help us understand and improve agricultural systems.

What attracted me to this challenge is that agriculture is not only about prediction — it is about asking the right questions:

How do we balance resources and outcomes?
How do we make intelligent decisions under uncertainty?
How can AI help create more sustainable farming practices?
In many machine learning problems, the most important step happens before choosing a model: understanding the environment, discovering patterns, and asking better questions.

Looking forward to learning from everyone here, especially from beginners and experienced Kagglers sharing their ideas. This looks like a wonderful opportunity to explore AI beyond traditional prediction tasks.

Good luck to everyone, and happy experimenting!


Reply

1

4
Arjun Bainade
Posted 2 months ago

do i have to make my own environment or there is competition environment already given?


Reply

React
Bovard Doerschuk-Tiberi
Kaggle Staff
Posted 2 months ago

· 9374th in this Competition

you can install the kaggle-environments pip package which contains the https://github.com/kaggle/kaggle-environments


Reply

React
Vib
Posted a day ago

· 2339th in this Competition

Could Kaggle clarify the permitted use of public episode replay data in submitted agents?

Competition replays expose state/action trajectories and are available to participants through Kaggle's replay tools. We understand that these can be used for analysis, benchmarking, and learning from public gameplay.

Where is the boundary if an agent derives deterministic behavior from those trajectories—for example, an opening book, imitation-learned policy, or hard-coded sequence derived from a public replay?

Specifically, is it permissible for a submitted agent to execute action trajectories substantially or exactly derived from another team's publicly available episode replay, even though that team's underlying source code has not been publicly shared?

We want to make sure we distinguish correctly between permitted use of public replay data and Rule 6.b's provisions concerning publicly shared Competition Code.


Reply

React
okuary
Posted a month ago

一开始该使用哪种开始呢？baseline，也要像原先的做法一样开始吗


Reply

React
Sandeep063
Posted a month ago

· 4736th in this Competition

is there any thing for learning courses, like how people actually doing


Reply

1
AmirHossein Motaharpour
Posted a month ago

· 5143rd in this Competition

How could we setup requirements for our agents? we must zip a code with requirements.txt !? or other method we should to follow?


Reply

React
大山
Posted 2 months ago

· 2072nd in this Competition

"The Play in Browser provided by the event seems to differ from the problem description. For example, DROP — orthogonally adjacent to the shed, dump the active farmer/hand's entire current inventory into the shed. Overflow past shedCapacity is discarded. No-op if not shed-adjacent. The browser version does not implement this, and the movement of the helper/hand also deviates somewhat from the problem description."


Reply

React

Appreciation (1)
rishabh_guptaz
Posted 2 months ago

Thanks for the info.


Bovard Doerschuk-Tiberi · 9374th in this Competition · Posted 2 months ago
·
Kaggle Staff
Daily Top Episodes Dataset
Each day we order episodes by the average rating of the agents playing (at the time). Then we download up to 20 GB of replays and make a new daily dataset! This should be helpful for everyone trying IL/BC, bootstrapping RL, or just gathering statistics.

https://www.kaggle.com/datasets/kaggle/kaggriculture-episodes-index


35

13
7 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Ragheb haddara
Posted 2 months ago

The ARC-AGI-2 tasks are significantly harder than AGI-1 because they require compositional reasoning — combining multiple transformations in sequence. Common patterns include: 1) Tiling/repeating the input grid, 2) Color substitution, 3) Object detection (find the largest/smallest object), 4) Symmetry completion. The evaluation format allows two attempts per task, so having a sensible fallback ensures you don't get zero.


Reply

React
Syed Asad Ali
Posted 3 days ago

· 36th in this Competition

@bovard unable to download the latest dataset, it is stuck on "Awaiting Compression"?


Reply

React
Noberto Frota
Posted 9 days ago

· 4908th in this Competition

Really useful dataset for imitation learning and behavior cloning.

Since episodes are prioritized by the average rating of the agents playing, I wonder how much this selection affects strategy diversity in the dataset. Training mostly on high-rated agents could be great for learning strong behavior, but it might also underrepresent alternative strategies.

Has anyone compared training on these top episodes with a more diverse sample to see how it affects generalization?


Reply

React
Georgy Mamarin
Posted 15 days ago

· 576th in this Competition

The 20 GiB budget binds on 43 of the 44 days, each one landing within 0.6 MB of the limit. So the episode count tracks replay weight rather than how many strong games a day had: a replay averaged 22.0 MiB on Jul 31 and 31.1 MiB on Sep 11, and the daily file went from 928 episodes to 657 over the same stretch. Weight the days equally and September games get more of the sample than the day count suggests.

Median avg_score was 670 on Jul 30 and 2,767 by Aug 4, and it has sat between 2,735 and 3,080 since. Those first days are a different population from the rest of the archive, worth splitting out before pooling.


Reply

React
CemBas
Posted 2 months ago

· 630th in this Competition

Super useful :) instead of handpicking replays. Thank you!!!


Reply

React
Weijun Guo
Posted 2 months ago

· 7934th in this Competition

Hello, might be a stupid question. The 20GB data is quite interesting for me to train my agents. The current csv file at the link seems to be a csv file that has the top ranking agent index numbers. Is the 20GB data also available for download at the link? If so, would appreciate how to download it from client side. Thanks!


Reply

React
QuasarHeart
Posted 2 months ago

· 7155th in this Competition

Check the csv file and u will find urls for downloading


Snorlax · 48th in this Competition · Posted 10 days ago
Finally reached the silver medal zone with Reinforcement Learning
After a lot of experiments, failed runs, weird policies, and watching my agent make decisions that no human would ever make…

It finally reached the silver medal zone 🎉

Built mainly with reinforcement learning, which made the whole journey much more painful — and much more fun.

Still plenty of room to improve. Let’s see if the agent can climb a little higher before the end.

Back to training. :)


49

11
27 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
D Chakraborty
Posted a day ago

· 29th in this Competition

How to get top 10?


Reply

React
madmax0404
Posted 6 days ago

· 837th in this Competition

hello, may i ask what kind of compute you have?


Reply

React
nofreewill42
Posted 10 days ago

· 1134th in this Competition

i wish this competition was like 6 months long


Reply

2
KKY
Posted 10 days ago

· 773rd in this Competition

Great job, thanks for sharing your progress!


Reply

React
Vishal Kishore
Posted 10 days ago

· 2543rd in this Competition

I have a doubt are you using RL for macro (policies) or micro (turn based) level decisions ?


Reply

React
Snorlax
Topic Author
Posted 10 days ago

· 48th in this Competition

Macro level


Reply

8
Ankith Savio
Posted 10 days ago

· 1531st in this Competition

How many steps did it take to achieve this?


Reply

React
Snorlax
Topic Author
Posted 10 days ago

· 48th in this Competition

Roughly 300k games in total. I’ll keep the exact step count private for now :)


Reply

4
Syed Asad Ali
Posted 9 days ago

· 36th in this Competition

@pku1400010735 Congratulations on reaching Silver via the RL route. This is no small feat! Could you please clarify a few details regarding your approach? What are the macro actions, how frequently are they chosen, and what supplied the BC demonstrations?


Reply

React
Snorlax
Topic Author
Posted 8 days ago

· 48th in this Competition

Thanks! For the BC data, you can use the official collection of top-match replays, or build a local pipeline to collect replays from top teams yourself.


Reply

1
Syed Asad Ali
Posted a day ago

· 36th in this Competition

Hi @pku1400010735 Nice work! Did the RL agent finally pass your rule-based agent to take your top spot, or is the deterministic one still ahead? Do you think this setup has a shot at pushing into gold?


Reply

React
TheoDaimon
Posted 6 days ago

· 2026th in this Competition

hi! Can u share notebook after competition's end?


Reply

React
OmerZalman
Posted 7 days ago

· 555th in this Competition

Congrats on the gold medal


Reply

React
9Hash
Posted 7 days ago

· 2870th in this Competition

I did improved with rl, but eventually down the line, some aspects are collapsing completely. Are you training on bank improvement objective or solely improving the win ratio?


Reply

React
Snorlax
Topic Author
Posted 7 days ago

· 48th in this Competition

I found the bank difference to be a informative reward early in training, then later added the final win/loss outcome as well. I also use a few auxiliary rewards to make learning and convergence more stable.


Reply

1
WOOSUNG YOON
Posted 7 days ago

You’re achieving great results with a really good method.

I’ll be watching and cheering you on 😄.


Reply

React
Snorlax
Topic Author
Posted 7 days ago

· 48th in this Competition

Thanks! I’ll keep going!


Reply

React
Alex Paul
Posted 8 days ago

· 1569th in this Competition

congrats on the silver btw. trying the BC warmup then PPO route myself at the macro level. curious about the data side since you mentioned the official top match replays: did you clone only the winner seat actions or both seats? and did you filter games by bank or opponent rating at all? also how did you decide a checkpoint was good enough to submit, replaying against recorded games or just live ladder reads?


Reply

React
Snorlax
Topic Author
Posted 7 days ago

· 48th in this Competition

Thanks! I don’t think the exact BC warm-up setup is the key part — roughly speaking, higher-scoring players are more valuable demonstrations. For checkpoint selection, I built a small local leaderboard for evaluation and occasionally submit checkpoints to the real Kaggle ladder to validate it. The hard part is that Kaggle feedback is quite slow, so deciding which agent to trust for the final submission still takes some careful judgment.


Reply

React
OmerZalman
Posted 9 days ago

· 555th in this Competition

did you use native RL or a more specific version?


Reply

React
Snorlax
Topic Author
Posted 8 days ago

· 48th in this Competition

I used PPO


Reply

React
Adarsh
Posted 10 days ago

· 689th in this Competition

Congrats, especially with RL, not easy to do


Reply

React
Navneet
Posted 10 days ago

Bravo for reaching the silver medal zone @pku1400010735


Reply

React
J.Moriuchi
Posted 10 days ago

· 848th in this Competition

Congratulations on reaching the silver medal zone! 🎉 That’s an amazing achievement, especially with an RL-based agent. I can imagine how many failed experiments and bizarre policies you had to go through to get here. Your persistence is truly inspiring. Good luck in the final stretch—I hope your agent climbs even higher!


Reply

React
Krzysztof Gonia
Posted 10 days ago

· 1135th in this Competition

Congrats! I focused on heuristic solution because I found RL to slow - running experiments takes too much time locally.


Reply

React
Khánh Vũ
Posted 10 days ago

· 83rd in this Competition

Was it trained from scratch?


Reply

React
Snorlax
Topic Author
Posted 10 days ago

· 48th in this Competition

I used behavior cloning for warm-up, then switched to RL training.


Reply

React
Khánh Vũ
Posted 10 days ago

· 83rd in this Competition

make sense, thnx


Omkar Kadam · 2521st in this Competition · Posted 13 days ago
Will code sharing also be closed in this competition, as it was in the PTCG Competition ?
I wanted to ask whether code sharing will also be closed in this competition, similar to what was done in the PTCG Competition.


React
7 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Less
Posted 13 days ago

· 1678th in this Competition

Can new versions of open code be prohibited?


Reply

React
Addison Howard
Kaggle Staff
Posted 13 days ago

· 1538th in this Competition

Yes - the public notebook sharing deadline is 23 Sep at 11:59pm UTC


Reply

2

3
mernak
Posted 3 days ago

· 188th in this Competition

@addisonhoward Hello, it seems that notebook sharing is still on, could you please fix it? It really seems as a problem for this competition


Reply

1
Addison Howard
Kaggle Staff
Posted 3 days ago

· 1538th in this Competition

Hey there - we're looking into this. We're only seeing one newly published notebook today, which is related to a bug we'll fix.


Reply

1
mernak
Posted 3 days ago

· 188th in this Competition

I am not sure what you've meant by "sharing", but there are notebooks updated having diffs like 5k lines, basically creating new ones instead, might be another issue


Reply

React
Joseph Ayanda
Posted 9 days ago

· 322nd in this Competition

Hi @yamakawanin — your live score is tip-class, but the public king-v4e notebook looks older than LastSub.

If you can push a new public notebook (or OSI dataset + main.py) that matches the current live agent before the 23 Sep 23:59 UTC share lock (#741281), that would unlock a fair public clone path. Public artifacts only — no DMs for code (#737885). Thanks either way. — Joseph (@josephayanda)


Reply

React
Joseph Ayanda
Posted 9 days ago

· 322nd in this Competition

Hi @fogflower — quick public ask only.

Public notebook sharing closes 23 Sep 23:59 UTC (host #741281). If you have a transferable agent you are willing to release, a public notebook or OSI-licensed dataset containing main.py before the lock would be hugely useful to the community.

No request for private code or DMs (see host #737885). Decline is fine. Thanks. — Joseph (@josephayanda)


Reply

React
Joseph Ayanda
Posted 9 days ago

· 322nd in this Competition

Hi @peikopon (Crop Dustas) — congrats on the strong run.

Host public-notebook share lock is 23 Sep 23:59 UTC (#741281). If you planned to open-source any transferable agent eventually, could you publish a public notebook or an OSI-licensed dataset with main.py before that lock? Even an older ≥2800-class body (not necessarily live SOTA) would help the field finish as public research.

Please keep any share on Kaggle public artifacts only — no DMs for code (host #737885). Totally fine to decline. Thanks either way. — Joseph Ayanda (@josephayanda)


Reply

React
Joseph Ayanda
Posted 10 days ago

· 322nd in this Competition

Hi hosts (@AddisonHoward / team) — confirming the public notebook sharing deadline is 23 Sep 23:59 UTC.

Request: please pin a short reminder asking teams who can to publish a ≥2800-class agent notebook (or OSI-licensed dataset with main.py) before that lock, so the final week stays a public research finish rather than a fully closed private ladder.

Not asking anyone to leak private SOTA; even a slightly older ≥2800 body or a distilled public cousin would help the field. Thanks for running this.


sobameshi · 588th in this Competition · Posted 24 days ago
I came here to build a farming agent. I ended up building a replay-measurement pipeline
I want to share something slightly strange about how our approach to this competition has evolved, along with some measurements of the replay meta.

This is not a rules question. #737788 established that public code and public episodes are fair game, and in #738837 the host said that using public replays to build a submission is allowed and encouraged. It is also not a criticism of teams using replay or cloning strategies. We are one of them.

What we have actually been doing
Since late August, our tracked submissions have mostly been tapes: recorded 720-turn action histories from strong public episodes, replayed verbatim on new seeds, sometimes with a small market-side adjustment.

We collect recordings from the daily top-episodes dataset and from public notebooks, reproduce them locally, run them against the other public strategies, and replace our current tape when a stronger one appears.

This works surprisingly well. In our experience, cloning a sufficiently recent strong public strategy has been enough to sit around the top 10% of the leaderboard, although the exact position moves as the meta changes.

That led us to investigate why.

What we measured
We fingerprint seats in the daily dumps and in our own games by their first 120 actions. This lets us track, approximately, which opening or strategy family is being played over time.

We then ran a round-robin of 14 public implementations spanning roughly a month of the competition, on 96 fresh seeds, both seats.

What surprised me most is that the result looks much more like a ladder than a rock-paper-scissors game:

Across the 14 implementations there is no intransitive triple.
Of the 91 chronological pairs, the newer implementation beat the older one in 86.
Adjacent generations typically won 60–80% of their games; two generations apart, 90–100%.
The ordering tracks average final money remarkably closely.
In other words, at least among the public implementations we tested, a stronger economy is simply a stronger economy, regardless of which other public strategy it faces.

The replay waves
The daily dumps show the same pattern.

Across 19 daily dumps, once an opening fell below 5% of observed seats, we never saw it become common again. A new wave peaks roughly a day after its source becomes public and fades within a few days as another, stronger economy appears.

Most of these waves originate from a very small number of sources: a few prolific notebook authors, and the public recordings of a handful of strong runtime-agent teams. In the 2026-09-02 dump, the single most common opening we detected came from one public episode of one strong team: 18 teams were playing that opening, a minority replaying all 720 turns verbatim and the rest changing the later turns.

So the picture we currently see is roughly:

runtime agents discover strong economies → their episodes become public → those economies are replayed or cloned → local testing identifies which replay is currently strongest → a new runtime economy appears → the ladder moves up one rung.

The part I find strange
I think this is the source of my discomfort.

I entered Kaggriculture because I wanted to learn how to build a strong farming agent: something that observes the town, makes plans, adapts when the world changes, and discovers better economies.

A month later, the system I have spent the most time building is not a farming agent. It is a measurement pipeline. It fingerprints public episodes, reproduces strategies locally, runs them against one another, tells us which rung of the current ladder is strongest, and helps us reproduce it quickly.

There is real engineering and experimentation in doing this well, and I have learned a lot from building the evaluation infrastructure. But it is not quite the problem I thought I was signing up to solve. And the better our measurement and cloning pipeline becomes, the less farming intelligence our submitted agent needs to contain.

Where I honestly stand
I do not think the answer is simply "replaying is bad." The data is public, the rules allow it, using public information well is part of Kaggle, and checking whether a public strategy actually generalizes to fresh seeds is a legitimate experimental problem in its own right. Watching strategies diffuse through a competitive population is also genuinely interesting.

At the same time, I find myself much more impressed by the teams whose runtime agents are actually producing the new economies that the rest of us later measure, replay, and modify. That is also the direction I originally hoped to explore when I entered this competition.

So I have started asking myself a different question: am I getting better at solving the farming problem, or at measuring and making use of the information ecosystem around it? Maybe both count.

Maybe discovering, evaluating, and rapidly adapting public strategies is an intended part of this competition. Or maybe verbatim replay is unusually strong here simply because economies transfer so well across seeds. I genuinely do not know.

I would be especially interested to hear from people building runtime agents, from people using replay-based approaches like us, and from the hosts: is this replay ladder something you expected to emerge? And how do you think about the distinction between solving the underlying simulation and solving the meta around it?

If there is interest, I am happy to share the fingerprinting method and the full round-robin results.


1

1

1
18 Comments
Hotness
 
Comment here. Be patient, be friendly, and focus on ideas. We're all here to learn and improve!

This comment will be made public once posted.


Post Comment
Georgy Mamarin
Posted 3 days ago

· 576th in this Competition

I am on the tape side of this and not far up it. My biggest single jump on this ladder came from adopting a strong public tape, and the tape was Michael's. So here is a number for one corner of your picture.

You named the shared market as the one place where direct interference really happens. Same farm, same season, opponent held fixed, same seat, changing only the size of each sell order. Trickling three units a turn instead of emptying the shed:

against an opponent that does nothing: +280 ± 89 coins, ahead on 8 of 8 seeds
against an opponent that sells on sight: patience costs me 547 ± 6 and hands the opponent 593 ± 21. The head-to-head gap is 1,154, but the two banks together are up 46.
So it is a transfer between the two farms, and the mechanism is not the one I assumed. Price support from holding back is about 2% on a mean of 15.90, far too small to be that 593. The impatient farm wins by selling early into a market that decays afterwards. The patient one sells everything too, just later and lower, and carries inventory on 175 turns out of 720 against its opponent's seven.

The interaction surface is real and it is sizeable, then, but shaped so that the cooperative move loses against the field as it stands. That may be part of why it reads as flat from where the tapes sit.


Reply

1
冯老虎
Posted 11 days ago

· 1545th in this Competition

拥抱变化，接受一切，哈哈，没招了


Reply

3
Zejun_
Posted 24 days ago

· 395th in this Competition

Not fun, the goal from "be the best" turn to "be better a little than most public notebook". Only very few participants still make new things.


Reply

3

1
sobameshi
Topic Author
Posted 24 days ago

· 588th in this Competition

I can relate to that. I don't think public sharing is bad in itself, but once the main path becomes "take the strongest public replay and improve it a little," it does feel like there's less incentive to try genuinely different ideas. Hopefully we eventually reach a point where runtime agents and new approaches matter more again.


Reply

React
Yusuke Hayashi
Posted 24 days ago

· 523rd in this Competition

I strongly relate to this. I’ve also built and shared a replay-based agent, but it feels quite different from what I expected to be doing when I entered this competition. Still, part of me hopes the field climbs this ladder faster and gets closer to its ceiling—so that replay-based approaches yield diminishing returns, while genuine runtime agents become relatively more valuable.


Reply

2

1
sobameshi
Topic Author
Posted 24 days ago

· 588th in this Competition

That's a framing I hadn't considered — replay strategies eventually running into diminishing returns as the ceiling gets closer, rather than the ladder just climbing indefinitely. That's a genuinely useful way to look at it, thanks.

And I'd like that too, if it's at all possible: for the second half of this competition to turn into more of a real runtime-agent contest.


Reply

React
Navneet Prabhat
Posted 3 days ago

· 6365th in this Competition

Well, seems like most of the folks are doing that only. Building an agent which crosses 1 lakh coins is difficult. And by analyzing the top replays and building agents by AI folks are able to do. And I think it's fair. Competition allows this and philosophically, that's how life is. You watch others, get inspired, and act accordingly.


Reply

React
Nathan Jacob
Posted 14 days ago

· 494th in this Competition

This resonates — went down the exact same rabbit hole.

After watching LB replays of v40, I noticed 3/4 of losses had the same bug: 2 cows dying on day 1 because the tape missed a FEED action. Each dead cow = $12–32K lost. So I built a local arena that runs LB-identical games, tested v40 recurring failure mode.

4 fixes kept, 12 reverted. Most "improvements" that sound good actually hurt - deterministic testing catches that before you burn a submission slot.

The fun part: the patched v40 beats Ahmed's new v41 23-7 in H2H, because v41 solved the cow problem by earning less money (conservative funding), while the patches solve it by just… feeding the cows.

Full writeup + fork-and-submit agent:
https://www.kaggle.com/code/nathanjacob/no-cow-left-behind-v40-autopsy-fix

Testing framework:
https://www.kaggle.com/code/nathanjacob/colosseum-876-2600-agent-testing-framework


Reply

1

1
Michael Timbs
Posted 19 days ago

· 134th in this Competition

I've been doing the same. I also noticed when i did spend a bunch of time finding novel play the entire field copied me within 24 hours so i didnt submit again for over a week.

Interestingly, for the first time since the competition started we have someone (SpaTaro) in the top 10 who is not taking this approach though and every single one of their matchups has played a unique strategy which means they are doing more than a static policy book.


Reply

2
Justin Gao
Posted 20 days ago

· 3373rd in this Competition

I tried to build a three-tier real-time decision system consisting of planner, scheduler, and worker, responsible respectively for macro-level situation monitoring, micro-level fixed-task management, and actual execution. However, even with this approach, I still couldn't achieve the efficiency of a tape-based strategy. Improving efficiency in my micro-task management has been slow and frustrating—and that is the paradox of this game.


Reply

1
sobameshi
Topic Author
Posted 19 days ago

· 588th in this Competition

That sounds very similar to what I’ve been seeing with my own runtime line. Even if you separate the system into layers, meaningful improvements often require changes that cut across several of them at once. Once that happens, it becomes much harder to isolate causes cleanly, so the iteration cycle slows down a lot.

At the same time, I still have the feeling that runtime agents may overtake tape-based approaches once they cross some threshold. What’s interesting is that the newer public non-runtime solutions already seem to be moving in that direction: they are no longer just “better tapes,” but tape + mechanism, with routers or state-dependent logic deciding which trajectory to follow.

So I’m still optimistic that runtime will win eventually—the hard part is getting through the stage where every useful improvement becomes a multi-layer coordination problem.


Reply

React
Chris Is Kaggling
Posted 22 days ago

· 3301st in this Competition

​I initially built a tape model simply because I joined this competition a bit late and wanted to study how others were playing, see the differences between strong models and ordinary ones, and analyze, dissect, and ponder the difference between the "essence of this competition" and the "essence of winning a top 10 spot."

​To my surprise, as everyone has shared, the proportion of runtime agents is very low and widely distributed, while meta tapes are updated heavily every day. I myself felt pretty good for a while after submitting a few tapes that got me into the top 10% on the leaderboard, but when I repeatedly thought about the final scoring system and the leaderboard ratings, I realized that trying to win in the end relying on tapes depends more on early-game winning streak luck combined with late-game rock-paper-scissors luck among same-generation tapes. However, whether it's the essence of the competition or the essence of winning, it ultimately points to runtime agents being the most stable solution under this game mode, so I also plan to try building my own agent in the time remaining, and I no longer intend to chase a good-looking leaderboard ranking.

​Though I still feel that by the end game, we'll probably see runtime agents coexisting with their tapes, haha


Reply

3
Prema Ananda
Posted 23 days ago

· 3979th in this Competition

Special thanks to everyone building replay-based bots — they're great benchmarks to calibrate a dynamic agent against.

Sure, my agent's rating is nothing to write home about right now, since it computes everything in real time. But working on it is way more fun than dealing with scripted moves — those eventually hit a ceiling. So I'm betting on real-time economy and dispatch logic — feels like the more promising path to me.


Reply

2
sobameshi
Topic Author
Posted 23 days ago

· 588th in this Competition

I'm also starting to work on a runtime agent myself — honestly, seeing the reactions and discussion here gave me the push to finally start. I'm definitely getting a late start compared with some of you, but I'm going to give it a serious try. Good luck with yours too!


Reply

1
Prema Ananda
Posted 14 days ago

· 3979th in this Competition

@sobameshi Just curious about your current position around 401 on the leaderboard — is that submission running a dynamic real-time rule-based agent, or is it still driven by replay tapes? I’ve built a fairly comprehensive real-time bot that handles macro purchase planning, dynamic market trading, and worker task dispatching. Tuning and polishing the micro-efficiency to perfection is proving to be the hardest part, so I’m really curious which approach is carrying you there right now!


Reply

React
sobameshi
Topic Author
Posted 14 days ago

· 588th in this Competition

Sorry to disappoint you, but unfortunately the submission sitting around rank 400 is the tape-router one. I currently have two submissions active: that tape-router baseline, and a separate real-time runtime agent. The runtime one is currently around 1640 score, which is roughly around rank 2000.

The tape-router side is actually quite automated at this point. I barely inspect the internals anymore — I mostly start from one of the stronger public baselines, run it through a fixed modification pipeline once, and submit the result. I update that line maybe once every three days, and it takes around 30 minutes each time. The runtime agent is where I’m spending most of my actual research time. The biggest problem is that its underlying economic base is still weaker than the strongest tape-based policies. For example, even against an opponent that simply PASSes every turn, the runtime still loses in final money to the strongest tape-based agents in most cases. Because of that, I’m currently focusing less on the reactive layer itself and more on things like market interpretation, capital allocation, and worker efficiency. So far, closing that basic economic gap has been much harder than I expected. So I definitely relate to what you said about micro-efficiency — that’s probably the hardest part for me too right now.


Reply

React
Prema Ananda
Posted 14 days ago

· 3979th in this Competition

Appreciate the transparent breakdown! I'll try to climb up to the ~1600 score level so our runtime bots can meet :) Mine is currently around 1200 score.


Reply

React
Andrew Reed
Posted 24 days ago

· 671st in this Competition

Your experience is eerily similar to mine. Why do you think tape-replay is so effective? Is there just not enough opportunity to interact with (i.e., undermine) your opponent in this game? Are matches not sufficiently long enough (or random enough) for a dynamic agent to succeed consistently against tapes?


Reply

1
sobameshi
Topic Author
Posted 24 days ago

· 588th in this Competition

Good questions. My current guess, based on what we've measured, is that the interaction surface between two agents is simply smaller than it looks. Most of the farm plan is fairly self-contained, so a stronger economic plan often stays stronger regardless of the opponent, with the shared market being the main place where direct interference really happens.

That said, I don't think dynamic play is weak. We've had several cases where adding a small reactive layer specifically for tape-like or near-mirror opponents made those matchups noticeably easier to win.

So my current picture is: strong underlying economy first, then a relatively thin adaptive layer for the parts of the game where the opponent actually matters. That reactive layer alone has never been enough to get us into the top 100, though, so I suspect there still needs to be something fundamentally better in the underlying plan as well.


Reply

React
cygn
Posted 24 days ago

· 3592nd in this Competition

You've hit the nail on the head. I've also been in the top 10 with some tape replay approach and if you looked at what others were doing it seems like 85% of people do it like this. It's not particular interesting to me and I don't enjoy this competition atm for this reason.


Reply

1
sobameshi
Topic Author
Posted 24 days ago

· 588th in this Competition

Hi cygn, thanks for the reply!

On the "not interesting" part, I feel exactly the same way, and it means something to hear that from someone that much higher up the ladder.

Lately, I've mostly given up trying to solve that part and settled for at least being honest with myself about what I'm actually doing — which is really what most of the post above was about.

One thing I do want to try, once our tape-making pipeline is stable enough that it no longer needs daily attention, is to build an actual runtime agent from scratch and put it in our other submission slot, just to see how far it can get on its own.