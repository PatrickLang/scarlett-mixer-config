Name:           scarlett-mixer-config
Version:        0.1
Release:        1%{?dist}
Summary:        Configure snd_usb_audio for Focusrite Scarlett 2nd/3rd gen devices

License:        MIT
URL:            https://www.kernel.org

Requires:       kernel >= 5.14.0

%description
This sets the options needed in /etc/modprobe.d/scarlett-mixer.conf to enable
the mixer devices to be initialized. In combination with alsa-scarlett-gui,
this enables to you configure hardware mixing and routing of the many PCM
devices provided by the Focusrite Scarlett series of audio interfaces.

%files
%{_sysconfdir}/modprobe.d/scarlett-mixer.conf

%changelog
* Wed Apr 05 2023 Patrick
- 
