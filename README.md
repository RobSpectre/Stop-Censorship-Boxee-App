# Stop Censorship

A Boxee application facilitating direct contact with the United States Congress
to voice disapproval of the
[SOPA](http://en.wikipedia.org/wiki/Stop_Online_Piracy_Act) and
[PROTECT-IP](http://en.wikipedia.org/wiki/PROTECT_IP_Act) bills.


## Summary

The Internet we know and love is at risk.  You can help save it.

Two very dangerous bills are currently under consideration by the Congress of
the United States.  Dubbed the [Stop Online Piracy
Act](http://en.wikipedia.org/wiki/Stop_Online_Piracy_Act) and
[PROTECT-IP](http://en.wikipedia.org/wiki/PROTECT_IP_Act), the bills
collectively hand over editorial control of much of the Internet to media
special interests and the United States government, granting new powers to block
domain names merely accused of copyright infringement.  Additionally, it would
force user-generated content sites like [YouTube](http://www.youtube.com),
[Tumblr](http://www.tumblr.com), [Vimeo](http://www.vimeo.com), and many others
to unprecedented lengths to police content and put people in prison for
violations.

These two bills represent an existential threat to the Internet fueling the only
economic growth seen in the Western world during these troubled times.  Should
these bills become law, the regulations they represent would crush Internet
innovation, destroy wealth and kill jobs, to say nothing of curbing freedoms we
all currently enjoy.

It is incumbent upon all technologists in the United States to take action to
end this threat.  To that end, this Boxee application makes it easy for you to
call your Congressional representatives from the comfort of your couch. 


## Usage

1. Install Boxee app from the App Library
1. Input telephone number
1. Input zipcode
1. Click Call Congress
1. Save the Internet.


## Hacking

### Installation

To install Stop Censorship to your local Boxee client or Boxee Box, follow 
the instructions on the [Boxee Developer
Wiki](http://developer.boxee.tv/Applications#Debugging).

### Structure

- client - The Boxee app
    - descriptor.xml - Manifest file for application
    - stopcensorship.py - Method for making request to
      [MobileCommons](http://www.mobilecommons.com).
    - skins
        - boxee
            - 720p - User interface files
            - media - Art assets 
- server - Server assets for the application thumbnail (just a PNG)


## Contributors

* [Rob Spectre](http://www.brooklynhacker.com), [Twilio](http://www.twilio.com)
* [Jim Colgan](http://twitter.com/#!/jim_colgan), [Mobile Commons](http://www.mobilecommons.com)


## License

* [Mozilla Public License](http://www.mozilla.org/MPL/) 

[![githalytics.com
alpha](https://cruel-carlota.pagodabox.com/66361dd754066bd5b5de64914d99bed3
"githalytics.com")](http://githalytics.com/RobSpectre/Stop-Censorship-Boxee-App)
