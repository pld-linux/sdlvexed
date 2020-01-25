Summary:	Clone of the classic PalmOS game Vexed
Summary(pl.UTF-8):	Gra Vexed bazująca na wersji z systemu PalmOS
Name:		sdlvexed
Version:	0.6
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://core.segfault.pl/~krzynio/vexed/sdlvexed-%{version}.tar.bz2
# Source0-md5:	5cc4afe52786e52a1b02d8057b0e25ec
Source1:	%{name}.desktop
Source2:	%{name}.png
BuildRequires:	perl-base >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-SDL >= 1.19
Obsoletes:	vexed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDL Vexed is a puzzle game written in Perl-SDL. It is a clone of the
classic PalmOS game Vexed.

%description -l pl.UTF-8
SDL Vexed to układanka napisana w Perl-SDL. Jest klonem klasycznej gry
Vexed z PalmOS-a.

%prep
%setup -q

%build
%{__perl} -pi -e "s/\$PREFIX\='\.'/\$PREFIX\='\/usr\/share\/sdlvexed'/" vexed

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_datadir}/%{name}/gfx,%{_datadir}/%{name}/levelpacks,%{_pixmapsdir}} \
$RPM_BUILD_ROOT%{_desktopdir}

install vexed $RPM_BUILD_ROOT%{_bindir}/sdlvexed
install gfx/*  $RPM_BUILD_ROOT%{_datadir}/%{name}/gfx
install levelpacks/* $RPM_BUILD_ROOT%{_datadir}/%{name}/levelpacks
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README README.pl
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*
