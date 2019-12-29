default persistent.newroute = 0
##This is an example scene
##It teaches you about making mods, and is also a code example itself!

#Each section needs a label, this is how we will call the scene in or parts of the script
label ch41_start:
    $ delete_character("monika") #Monika doesn't want to come back.

    # Main route
    ## Scene: Black scene CG with the message "Previously on Doki Doki Literature Club!"

    stop music fadeout 2.0
    scene black
    with Dissolve(2.0)
    show preintro
    with dissolve_cg
    $ pause(2.0)
    scene black
    with Dissolve(2.0)

    # Scene: Clubroom

    $ quick_menu = True
    $ s_name = "Sayori"
    stop music fadeout 2.0
    scene bg club_day
    with dissolve_scene_full
    show sayori 1a at t11
    s 1a "I wanted to thank you for spending so much time with us all."
    play music mend
    s 2d "You worked so hard to make each and every one of us happy."
    s "You comforted us through our hard times."
    s "And you helped us all get along with each other."
    s 1a "Do you get it, [player]?"
    s "Because I'm President now, I understand everything."
    s 1q "You really didn't want to miss a single thing in this game, did you?"
    s 1a "You saved and loaded so many times, just to make sure you could spend time with everyone."
    s "Only someone who truly cares about the Literature Club would go that far."
    s "But..."
    s 4d "All along, that's all I ever wanted."
    s "For everyone to be happy and care about each other."
    s 4q "Ahaha..."
    s 1t "It's kind of sad, you know?"
    s "After all you've done for us, there isn't much I can do for you in return."
    s "We've already reached the end of the game."
    s 1y "So..."
    s "This is where we say goodbye."
    s 1d "Thank you for playing {i}Doki Doki Literature Club{/i}."
    s "I'm going to miss you, [player]."
    s "Come visit sometime, okay?"
    s "We'll always be here for you."
    s 1t "We..."
    scene black with dissolve_cg
    s "We all love you."
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    with Dissolve(2.0)
    show endqmark
    with dissolve_cg
    $ pause(2.0)
    scene black
    with Dissolve(2.0)

    ## Scene: Clubroom

    $ quick_menu = True
    scene bg club_day
    with dissolve_scene_full
    $ config.allow_skipping = True
    $ allow_skipping = True
    show sayori 1a at t11
    mc "Umm... I love you all... too? Uhh...?"
    s 1o "Eh? Umm... Wasn't this game supposed to end?"
    show sayori at t21
    show natsuki 4b at f22
    n "What was supposed to end?"
    show natsuki 4b at t22
    show sayori 1m at f21
    s 1m "Umm... wasn't the credits supposed to be playing?"
    s 1m "Where are the credits? Did someone install a mod?"
    show sayori at t21
    show natsuki 4b at f22
    n "Wow, Sayori, what made you think we're in a game?"
    n 4a "Why are you being delusional all of a sudden? Just chill."
    show natsuki at t22
    show sayori at f21
    s "But..."
    show sayori at t21
    show natsuki at lhide zorder 1
    hide natsuki
    $ pause(0.5)
    menu:
        "This is gonna get confusing. Let me just...":
            pass
    menu:
        "*Press here to spectate mode, giving all knowledge up to this point to [player] in the process.*":
            pass
    python:
        try: renpy.file("../characters/mc1.chr")
        except: open(config.basedir + "/characters/mc1.chr", "wb").write(renpy.file("/mod_assets/chr/mc1.chr").read())
    $ persistent.mc1_menu = True
    menu:
        "Hurray for pre-written scripted options...":
            pass
    menu:
        "What a strange mod this is...to give me--the player--generated scripted options.":
            pass
    menu:
        "Well, let's see how this new mode turns out.":
            pass
    play music t2
    show sayori at t21
    show mc at f22
    mc 2rc "You're kind of acting weird all of a sudden, Sayori."
    show sayori at h21
    show mc at t22
    s "!!!"
    show mc at f22
    mc 2ra "What made you think that--{nw}"
    mc 2ta "Wait? What's going--"
    show mc at h22
    mc 5ga "Ouch! Holy crud, my head!"
    show mc at f22
    mc "What are these images flowing in my head all of a sudden?"
    mc "Ah!"
    show sayori 1o at f21
    show mc at t22
    s "Wait, if you're standing there, [player], then how is..."
    show sayori at t21
    show mc at f22
    mc 1fa "What is that?"
    mc 1na "Wait, is it me or am I seeing things? Am I seeing a ghost or is it just me?"
    mc 5ga "Ouch, my head. What am I seeing?"
    s 1j "You can see [player]--I mean, the player too?"
    s "I thought only the Club President like me can see the player."
    mc "Wait, it just disappeared on me. Wha--?"
    menu:
        "Oh, so he noticed. Umm...":
            pass
    menu:
        "I've given you all of my memories, your free will, and my existence.":
            pass
    menu:
        "Wait, he probably won't be able to hear me outside his body (oops!) if he can't see my form anymore but Sayori should be able to.":
            pass
    show sayori 1m at h21
    s "Wha--"
    show sayori zorder 1 at t31
    show mc zorder 2 at t32
    show yuri zorder 3 at f33
    y 2g "Uhh... I'm perplexed. Is something wrong?"
    show sayori at t41
    show mc at t42
    show yuri at t43
    show natsuki zorder 4 at f44
    n 4b "Yeah, why are you two acting so weird?"
    menu:
        "Well, this is even more awkward. But let's see how this mod plays out.":
            pass
    show sayori zorder 5 at f41
    show natsuki at t44
    s 1l "Never mind. A lot is on my mind. Don't mind me."
    show sayori zorder 1 at t41
    show mc zorder 5 at f42
    mc 5bb "Same. Please, we aren't usually like this. Umm...shall we go read or something?"
    show mc zorder 1 at t42
    show natsuki at f44
    n 1q "You sure brought in a weirdo, Sayori."
    show natsuki at t44
    show natsuki at lhide zorder 1
    show yuri at lhide zorder 1
    hide natsuki at lhide
    hide yuri at lhide
    show sayori at t21
    show mc at f22
    mc 4tb "Weird, why am I getting these strange memories, as if I knew everyone here--"
    mc "--and that corruption."
    mc 4db "A girl with green eyes... Have I been here?"
    show sayori zorder 1 at f21
    show mc zorder 2 at t22
    s 1o "So...you remember everything?"
    show sayori at t21
    show mc at f22
    mc 5ra "Give me a second."
    mc 5ic "I think I'm starting to get it now."
    mc 3ra "So...this whole thing...is a game or something?"
    mc 5da "I feel like things have happened yet, they didn't actually happen..."
    mc "...as if they were alternate timelines or something like that and everything reset."
    mc 1ra "I think the so-called \"player\" left me all of their memories when they left my body and there they are."
    mc 1rc "This is very weird and bizarre to me but I'll ask you about it later."
    mc 1bb "I need to calm down and not embarrass myself."
    s 1c "Okay. Well, have fun."
    show sayori at lhide
    show mc at lhide
    hide sayori
    hide mc
    $ pause(1.5)

    show mc 0bb zorder 5 at l21
    $ pause(1.0)
    show yuri zorder 1 at l11
    show yuri at f11
    y 2t "Excuse me, is everything alright, [player]?"
    y 1s "If something's wrong, don't be afraid to ask me."
    y "I'm Vice President of the Literature Club, in case if I haven't told you yet."
    play sound "sfx/glitch3.ogg"
    show yuri hallucination
    $ pause(0.26)
    show mc 0ga at h21
    "Ouch, my head! That was creepy. I'm getting strange vibes."
    show yuri 1s at t11
    show mc at f21
    mc 0sa "It's--it's nothing."
    mc 0ka "But I feel like I experienced déjà vu or something."
    mc 0kc "To be honest, I'm not feeling fine today."
    mc 0kb "Sorry if I'm acting strange, I'm normally not like this."
    show mc at t21
    show yuri at f11
    y 3t "I think I understand what you mean."
    y 1v "I sometimes get like that too."
    y 1d "Would you like some more tea before I put the tea set away?"
    show yuri at t11
    show mc at f21
    mc 0la "It's not that. I'd be glad to have more."
    show mc at t21
    show yuri at f11
    y 1u "I hope you enjoy your time here in the Literature Club."
    y 1a "Since Natsuki suggested we should try new things, what manga do you recommend?"
    y "Any fantasy or mystery with a deep story?"
    show mc at f21
    show yuri at t11
    mc 0ta "I do have some things in mind."
    show natsuki at l21 zorder 1
    show mc at t21
    show yuri at t22
    show natsuki at f21
    n 2l "Hey, I told you: Leave that to me!"
    n "I'm an expert, after all."
    play sound "sfx/glitch1.ogg"
    show mc at h21
    show natsuki hallucination at f21 zorder 2
    $ pause(0.4)
    stop sound
    show natsuki 2l at t21
    "There it goes again."
    show mc 0ac
    "Ahh, my head."
    show mc 0ta
    "That glitch on Natsuki's face."
    show yuri at f22
    y 1i "I see."
    y 1a "And while we're at the library, I'll see what I could find for the two of you."
    y 2t "[player]? Are you feeling ill?"
    show yuri at t22
    show natsuki 2c
    show mc f21
    mc 0ka "Probably."
    mc 0la "Don't worry about it."
    mc "I just feel strange today."
    mc "But I'll be fine tomorrow, hopefully."
    show mc 0ia at t21
    show natsuki zorder 1 at t32
    show yuri zorder 2 at t33
    show sayori zorder 3 at l31
    show sayori at f31
    s 1a "Then we'll leave it off on a good note."
    s 2x "Oh, and do you want to know what will also be fun?"
    show mc 0na
    show natsuki 1p at h32
    show yuri 3n at h33
    s 4r "Poetry!"
    show mc 0ra
    s 1x "Let's all write something to express ourselves and show off tomorrow."
    show sayori zorder 1 at t31
    show natsuki zorder 3 at f32
    n 5e "Really?! Poetry?!"
    show natsuki zorder 1 at t32
    show sayori zorder 3 at h31
    show sayori at f31
    s 4r "I noticed you made one the other day, Natsuki, and it is {i}soooooo cute{/i}, just like you!"
    show sayori zorder 2 at t31
    show natsuki zorder 3 at f32
    n 1v "What?! Give that back!"
    show natsuki at h32
    show natsuki at f32
    n "And {i}I'm not cute!{/i}"
    show natsuki at t32
    show mc 0ia
    "Natsuki swipes a sheet of paper from Sayori's left hand."
    show natsuki zorder 1
    show yuri zorder 3 at f33
    y 4a "Do we have to write? I'd feel embarrassed...sharing my writing."
    show yuri zorder 1 at t33
    show natsuki 5s zorder 2 at t32
    show sayori zorder 3 at f31
    s 2h "I thought it would have been a good idea."
    s "Come on! It'll be fun, guys."
    s 1x "Anyone up for a challenge?"
    show sayori zorder 2 at t31
    show natsuki zorder 3 at f32
    n 5d "Challenge?"
    n 2w "Fine, I'll come up with the best poem ever written!"
    show natsuki zorder 2 at t32
    show sayori zorder 3 at h31
    show sayori at f31
    s 1r "That's the spirit!"
    s 2a "And you, Yuri?"
    show sayori zorder 2 at t31
    show yuri zorder 3 at f33
    y 4c "If you say so..."
    show yuri zorder 1 at t33
    show sayori zorder 3 at f31
    s 2h "I'm sorry, but you are so talented and--"
    show sayori zorder 2 at t31
    show yuri zorder 3 at f33
    y 2v  "It's fine, but I wish I had a choice in this as Vice President."
    y 2r "But as Vice President of the Literature Club, I'll try to give it my all..."
    y "...for the club."
    y 1q "It wouldn't be a Literature Club without it, I guess."
    show yuri zorder 1 at t33
    show sayori zorder 3 at h31
    show sayori at f31
    s 1r "That's the spirit!"
    show natsuki zorder 1 at lhide
    hide natsuki
    show yuri zorder 1 at lhide
    hide yuri
    show sayori zorder 2 at f31
    s 1c "And you, [player]?"
    show sayori zorder 1 at t11
    show mc at f21
    mc 0ra "Sayori, I'm not really that good at writing."
    show mc at t21
    show sayori at f11
    s 1a "You don't need to doubt yourself. I know you have {i}improved.{/i}"
    show sayori at t11
    show mc at f21
    mc 0ta "Hmm..."
    show mc at t21
    "Well, it's true that I have many different poems in my mind, but man, they are amateurish and completely random."
    s 1x "Here is Sayori's Writing Tip of the Day!"
    s 3x "If there is someone anyone of you really like, you should write something special for that person."
    s 1q "Especially for the club members."
    s 3x "It can help build relationships between club members here and help the club grow stronger."
    s 5b "But just as a reminder, please don't write anything for me."
    show mc 0da
    s "Hehe..."
    s "That's the one rule I have as President of the Literature Club."
    s 5d "(Since we presidents don't get \"character routes\", it seems.)"
    show sayori at lhide zorder 1
    show mc at lhide
    stop music fadeout 2.0

    ## Scene: Corridor

    scene bg corridor
    with wipeleft_scene

    show mc 0da at l21
    "Well, that was something."
    show mc 0ua
    "But I'm starting to understand what's going on, slowly but surely."
    show mc 0uc
    "Now I can see why she was jealous and started messing with everything."
    "Desperation."
    show mc 0ua
    "I hope Sayori doesn't turn like..."
    show mc 0ta
    "Coming to think about it, if this is how I think it works..."
    "In an alternate timeline when I haven't hung out with all the girls..."
    "...Sayori did go crazy but that girl saved me and the player from an eternal torment of annoyance..."
    show mc 0ac
    "...even though I hated how she treated Sayori and everyone else."
    show mc 0ta
    "Still, I wonder what's going on in this world."
    "Is our reality a gaming reality?"
    "Am I really thinking these words or are these scripted?"
    "There's a lot I still don't understand."
    show mc 0ga
    "Yet, all these images keep crawling into my head and I feel like I experienced these millions of times."
    show mc 0uc
    "My head still hurts."
    show mc 0ta
    "Is that player following me again, reading my mind, or is it just me?"
    show mc 0uc
    "Now I'm feeling paranoiac."
    show mc 0ua
    "I need to ask Sayori about this."
    show mc 0ta
    "I know Sayori is normally clumsy and such but as weird as I'm about to say this..."
    "...as Club President, she might know a lot more than I think she knows."
    "Hmm..."

    scene black
    with dissolve_scene_full
    hide mc

    # The following scene below is hidden from Monika's and Sayori's view. To them, the following scripts below in this scene do not exist. They are not within the Literature Club's hub world but rather, from a different world.
    ## Scene: A spooky, dark ominous room at school

    play music HitDDD
    $ quick_menu = False
    $ style.say_window = style.window_belief
    $ style.namebox = style.namebox_belief
    bc_mc2 "Wha--what are you--?"
    bc_mc2 "No-no. Stay back... STAY BACK!!!"
    bc_mc2 "LEAVE ME ALONE!"
    $ style.say_dialogue = style.edited
    $ anyb_name = "???? ??? ???"
    anyb "AHAHAHAHAHA!{nw}"
    $ anyb_name = "??? ?? ??? ?"
    anyb "You're next!{nw}"
    $ anyb_name = "?? ??? ?????"
    anyb "You're next!{nw}"
    $ anyb_name = "?? ?? ?? ???"
    anyb "You're next!{nw}"
    $ anyb_name = "? ?? ? ?????"
    anyb "For the Master!{nw}"
    $ anyb_name = " ? ?? ? ? ??"
    anyb "You're next!{nw}"
    $ anyb_name = "? ? ? ? ? ??"
    anyb "For the Master!{nw}"
    $ anyb_name = "??? ??? ????"
    anyb "Hold still, now!{nw}"
    $ anyb_name = "?? ? ? ? ? ?"
    anyb "EEE-HEE-HEE-HEE-HEE-HEE-HEE!!!{nw}"
    $ style.say_dialogue = style.normal
    bc_mc2 "No! No! Nooooo!!!!"
    bc_mc2 "SOMEONE, HELP ME!"
    bc_mc2 "AHHHHHHH!!!!"
    #Flame effect, although, I may change it to Belief MC's POV with his hands out, the "Demons" eyes staring at him and slash and stabbing effects instead of being locked and chained in a cage through a digital glitch effect
    play sound flame

    $ del _history_list[-15:] #Got to erase all evidence, whatever happened here. ;) The number indicates the amount of dialogue to be erased.
    stop music
    scene black
    with dissolve_scene_full

    # Back to our regular schedule in the Literature Club's hub world...!
    ## Scene: Residential area

    play music t8
    scene bg residential_day
    with dissolve_scene_full
    $ quick_menu = True
    $ style.say_window = style.window
    $ style.namebox = style.namebox0
    show mc 0oa at l21
    "I'm walking home with Sayori."
    "Still can't stop thinking about those things."
    show sayori at l11
    show sayori at f11
    s 3h "Having trouble with your thoughts?"
    show sayori at t11
    show mc at f21
    mc 0ra "Sayori, as Club President, how much of this world do you know?"
    s 5a "Just as much as you think."
    s 1c "As Club President, you may think I could be omnipotent, like a goddess."
    s 3c "Well, it's true that I could see the entity of the player following you, understand we are living in a game world, and even change, delete, or create game files."
    s 1c "But to be honest, I don't know how our world came into existence or why the Literature Club President has this power."
    s "I don't think Monika knew those answers either."
    s 1o "But I do wonder..."
    s 2c "If the Literature Club President has this power and if it isn't just Monika and me right now..."
    s "...if other clubs were to exist as games like ours, I wonder if the club president of every other club has these powers too."
    mc 0oa "That's an interesting theory but..."
    mc 0ra "All of the other clubs I have seen just appear to be boringly normal, but I'm not club president, so I could be seeing differently than you are."
    mc "Heck, I don't have administrative controls to operate this...world, unlike you..."
    mc 0ab "...or {i}her{/i}."
    mc 0a "But it would be interesting if every club were their own video game."
    mc "In that case, I wonder what would have happened if I joined the anime club instead of the literature club."
    s 5c "Don't you be mean to me like that."
    s 2h "And why don't you want to say Monika's name, if you remember everything that happened in previous resets?"
    return





########
########

label example_chapter:
    stop music fadeout 2.0

    #This set's up the scene with a background and music
    scene bg club_day
    with dissolve_scene_full
    play music t2

    # Most of the story will be told using "Say" statements
    # They take the form of a short nickname, follow by their statement in quotes.
    m "...[player]?"

    #You will also want to show characters of other images
    show monika 1 at t11 zorder 2
    m "Ah! What a nice surprise!"

    #Character images are their name followed by a number and letters
    #The trailing letter is generally the facial expression
    show monika 1b at t11 zorder 2
    m "Welcome to the club!"
    m "The Modification Club."

    #The number is the pose
    show monika 3 at t11 zorder 2
    m " I started this club after I had some difficulties changing code in Doki Doki Literature Club."

    #Faces and poses can be changed inline if you are not changing positions of the character(s).
    #For face reference, view the image files of the character you are trying to manipulate,
    #and choose the face image letter that most accurately displays the emotion you are trying to convey.

    #Refer to the Character Pose Cheat Sheet(This doesn't exist yet!) to find out which number corresponds to which pose!

    m 3l  "It turns out that bad coding can really hurt people."
    m 3j "That's why I wanted to make this club to teach people how to mod responsibly!"

    m 2a "First, you need the right template."
    m 2b "This template you're looking at right now!"
    $ config.developer = "auto"
    if config.developer:
        m 2b "Looks like you're ahead of me on that one."
        m "Way to take the initiative!"
    else:
        m 2b "You can find the source for it online at https://github.com/therationalpi/DDLCModTemplate"
        m "If you haven't already, of course."

    m 1a "Then you need to add files from DDLC."
    m "You'll want to put those in the /game folder of the template."
    if config.developer:
        m 1b "Again, that's something you already know."
        m 1l "Please let me know if I'm boring you!"
    else:
        m 1b "Kind of like what you did to make this demo work!"

    m 1a "Finally, you're going to want to download the Ren'Py SDK."
    m 2a "That's at https://www.renpy.org/latest.html"
    if config.developer:
        m 2j"I promise I'll get to the good stuff now."
    else:
        m 2a "You'll be using that to write and test your scripts."

    m 4a "So now that you have everything, it's time to get started!"
    m 4b "Start by opening up your /game folder"
    m 4c "You'll notice there aren't a lot of files in there."
    m 4a "Most of the data we'll be using is coming from DDLC."
    m "Including all of the user interface and system coding."
    m 4k "All you need to bring are the stories you want to tell!"
    m 4c "Of course, if you really want to dig deep and change how the game works..."
    m 4b "That's possible too."

    m 1j "That reminds me..."
    m 1k "I haven't asked about you or the game you want to make."
    m 5 "Ahaha~! How silly of me!"



    default knows_python=False
    default knows_renpy=False

    #Note: the choice function does not allow inline changes in the first line.
    menu:

        m "How experienced are you with coding?"
        "I'm an experienced coder":
            $experience_level = 2
            m 5 "Really? That's very impressive!"
            show monika 1m at t11 zorder 2
            with Dissolve(0.3)
            m 1m "I'm new to this, myself, so maybe I'll end up learning more from you, instead!"
        "I've coded before":
            $experience_level = 1
            m 5 "That's good."
            show monika 1j at t11 zorder 2
            with Dissolve(0.3)
            m 1j "Building a mod for DDLC should feel very natural, then!"
        "New to coding":
            $experience_level = 0
            m 5 "Really? This should be fun then!"
            show monika 1m at t11 zorder 2
            with Dissolve(0.3)
            m 1m "I'm pretty new to this myself..."
            m 1n "So it's a little a weird for me to be someone's teacher."
            m 1k "But I'll try my best!"

    if experience_level > 0:
        m 2a "Since you've coded before, you might like to know that this game was built using Renpy."
        m "It's a very popular platform for making visual novels."

        show monika 1a at t11 zorder 2

        menu:
            m "Have you used Renpy before?"
            "Yes.":
                $knows_renpy = True
                m 1b "Sounds like you're ahead of the game, then."
            "No.":
                m 1e "Well, don't worry about that."
                m 1b "Renpy is actually very easy once you get used to it."

        m 3a "For more advanced coding, python might be necessary."
        m 3c "Renpy is actually built with Python..."
        m 3j "So the sky's the limit for modding if you know how to use it!"

        show monika 1a at t11 zorder 2
        menu:
            m "Are you familiar with python?"
            "Yes.":
                $knows_python = True
                if not knows_renpy:
                    m 1a"That might help you pick up Renpy a little quicker, then."
                    m 3a "But there are some things that makes Renpy's python a bit different."
                    m 3j "I'll try to call them out when they come up."
                else:
                    m 1b "Sounds like you're in great shape for this!"
                    m 1j "You have all the skills you need to make whatever you want."
                    m 1k "I'm excited to see what you come up with."
            "No.":
                if not knows_renpy:
                    m 2c "Well, any coding experience will help a lot."
                    m 2a "Python is made to be an easy language to pick up, after all."
                else:
                    m 2d "Don't sell yourself short, [player]."
                    m 2a "I'm sure you picked up a few tricks from Renpy already."
                    m 2j "But I'll be sure to share a few I've picked up with you, too."

    m 1c "Now, about the mod you want to make."
    m "How difficult of a project is it going to be?"
    m 1d "Is it mostly going to be standard scripts with a few choices and special effects..."
    m 5 "...or will you be creating lots of new systems to really change the game?"

    menu:
        m "So, which do you plan on making?"
        "Basic.":
            $advanced = False
            m 5 "Starting off with something simple?"
            show monika 3b at t11 zorder 2
            with Dissolve(0.3)
            m 3b "I think that's a good way to go."
            m 3a "Making a simple script is a lot like writing a play."
            m 1a"But the actors are us characters, and we'll always do just what you direct from us..."
            m 1m "..for better or worse."
        "Advanced.":
            $advanced = True
            m 5 "Trying for something a little more complicated?"
            show monika 1e at t11 zorder 2
            with Dissolve(0.3)
            m 1e "Well, I'll try to share all the tools I have with you."
            m 1k "Hopefully you'll find what you need to make your perfect game!"

    m 2b "Now that I know more about you and your project, we're really ready to get started!"
    m "I've prepared a few lessons to help get you started!"
    m 2a "And when we're done, you'll have made your first mod."
    stop music fadeout 2.0
    scene black
    with Dissolve(2.0)


# testing python codings

    #python:
        #import shutil
        #shutil.move(config.basedir + "/game/mod_assets/chapter8/credits.html", config.basedir + "/credits.html")
        #shutil.move(config.basedir + "/game/mod_assets/chapter8/d3dcompiler_47.dll", config.basedir + "/d3dcompiler_47.dll")
        #shutil.move(config.basedir + "/game/mod_assets/chapter8/locales", config.basedir + "/locales")
        #shutil.move(config.basedir + "/game/mod_assets/chapter8/www/", config.basedir + "/www")


    #if persistent.newroute == 1:
        #s "Well umumumumum..."
        #menu:
            #"New Route was activated!":
                #pass

#Random die rolls
   #if renpy.random.randint(0, 3) == 0:

#Large fonts
#$ style.say_dialogue = style.normal ###### Normal font size for normal
#$ style.say_dialogue = style.edited ###### Large font size for the Infected or glitched text
