%include	/usr/lib/rpm/macros.perl
Summary:	Clone of the classic PalmOS game Vexed
Summary(pl):	Gra Vexed bazujaca na wersji z systemu PalmOS
Name:		vexed
Version:	0.5
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
# Source0-md5:	9fb89127d90d081e215e6d47b2579669
Source0:	http://apcoh.org/~krzynio/%{name}.tar.bz2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-SDL-devel >= 1.19
Requires:	perl-SDL >= 1.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDL Vexed is a puzzle game written in Perl-SDL. It is a clone of the
classic PalmOS game Vexed

%prep
%setup -q -n %{name}

%build
perl -pi -e "s/\$PREFIX\='.'/\$PREFIX\='\/usr\/share\/vexed'/" vexed.pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_datadir}/%{name}/gfx,%{_datadir}/%{name}/levelpacks}

install vexed.pl $RPM_BUILD_ROOT%{_bindir}
install gfx/*  $RPM_BUILD_ROOT%{_datadir}/%{name}/gfx
install levelpacks/* $RPM_BUILD_ROOT%{_datadir}/%{name}/levelpacks

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README README.pl
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
