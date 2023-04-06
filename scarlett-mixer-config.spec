Name:           scarlett-mixer-config
Version:        0.1
Release:        2%{?dist}
Summary:        Configure snd_usb_audio for Focusrite Scarlett 2nd/3rd gen devices

License:        MIT
URL:            https://www.kernel.org

Requires:       kernel >= 5.14.0, kernel-modules-extra

%description
This sets the options needed in /etc/modprobe.d/scarlett-mixer.conf to enable
the mixer devices to be initialized. In combination with alsa-scarlett-gui,
this enables to you configure hardware mixing and routing of the many PCM
devices provided by the Focusrite Scarlett series of audio interfaces.


# The full list is based off https://github.com/torvalds/linux/commit/4be47798d76e6e694d8258eeb4d4be0a64371e34
%build
cat > scarlett-mixer.conf <<EOF
# Scarlett 6i6 2nd gen
options snd_usb_audio vid=0x1235 pid=0x8203 device_setup=1
# Scarlett 18i8 2nd gen
options snd_usb_audio vid=0x1235 pid=0x8204 device_setup=1
# Scarlett 18i20 2nd gen
options snd_usb_audio vid=0x1235 pid=0x8201 device_setup=1
# Scarlett 4i4 3rd gen
options snd_usb_audio vid=0x1235 pid=0x8212 device_setup=1
# Scarlett 8i6 3rd gen
options snd_usb_audio vid=0x1235 pid=0x8213 device_setup=1
# Scarlett 18i8 3rd gen
options snd_usb_audio vid=0x1235 pid=0x8214 device_setup=1
# Scarlett 18i20 3rd gen
options snd_usb_audio vid=0x1235 pid=0x8215 device_setup=1
EOF

%install
mkdir -p %{buildroot}/%{_sysconfdir}/modprobe.d/
install -m 644 scarlett-mixer.conf %{buildroot}/%{_sysconfdir}/modprobe.d/scarlett-mixer.conf

%files
%{_sysconfdir}/modprobe.d/scarlett-mixer.conf

%changelog
* Wed Apr 05 2023 Patrick
- 
