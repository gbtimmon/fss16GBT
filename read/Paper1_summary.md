##1 Reference
    
F. Khomh, T. Dhaliwal, Y. Zou and B. Adams. 2012.Do Faster Releases Improve Software Quality?: An Empirical Case Study of Mozilla Firefox.Proceedings of the 9th IEEE Working Conference on Mining Software Repositories. IEEE Press, 2012.

##2 Keywords
i Release Cycle - the rate at which updates to software are pushed out to the consumer

ii Rapid Release - A methodology of keeping releases small and pushing them often in the hopes that this will imporve the release quality.

iii Post Release Bugs - Bugs reported by users after the release of an update. These are typically bugs missed by QA.

iv Uptime - The overall time that an application is available on average between crashes

##3 Summary

i Introduction 


The paper cites new Agile or XP trends pushing companies to move to generally shorter release dates. The core claim is the with shorter release periods, planning becomes eaiser, QA can be implemented more earlier in the process and customers can get critical bug fixes sooner. The claims of higher quality have not been empircally proven and studies have given mixed results when trying to measure the change. Firfox was used for this study since there was relatively little change in aspects other then the release cycle in the measured period. Metrics monitored where uptime, number of post release bugs and daily crash counts. The goals of these metrics was to answer the questions do shorter release affect quality, does it affect the fixing of bugs, and does it affect adoption to software updates. 

ii Measurements 

Many of the metrics were measured via a built in auto crash reporter tool that comes withh all versions of the browser.  QA staff tie bugs to the crash reporter data, or bugs can be files manually. The bug data was also extensively used in this paper, and the data comes from Firefoxes bug reporting framework bugzilla.  This paper study all multiple version of firfox from Firfox 3.6 to 9 across the switch from Traditional devleopment model to rapid release models. 

iii Results 

In relation to the first question of weather the change in developement model affects the soft ware quality : The paper found that there were no significant changes in the number of post release bugs, there is no significant decrease in daily crash count but there is a significant decrease in uptime in a rapid release model.  

In relation to the second question of weather the change in development model affects the length of bux fixes : The paper found in a rapid release model the number of bugs fix ed during the testing period we significantly loer than in the traditional model. Bugs are fixed faster under a rapid release model.

In relation to the final question of weather the release model affect the adoption of software updates. The paper found in a rapid release model, users switch fast to newer versions then in the traditional model (New version of FF had auto update and update reminders that did not exist, this doesnt seem to be corrected for). 
