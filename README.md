simcalWithAdmobs
=
Sample iOS application (a simple calculator) with google Admobile build from python and some Object-C. Several buttons not implemented though.<br>
For Object-C part, check [here](https://gist.github.com/shirubei/65cb741eadd64a71d5e7cc3eaaf5567e)<br>
[vedio1](https://www.youtube.com/watch?v=9V9kxHxaV0M) in Chinese<br>
<br>
packages: https://github.com/googleads/swift-package-manager-google-mobile-ads.git<br>
Build settings: "Enable Modules(C and Object-C)" set to "Yes"<br>
                "Other Linker Flags": add "-ObjC" and "$(inherited)"<br>
                "Header Search Paths": add "$(inherited)"
