%define		_theme 	reinhardt
%define		_theme_ver 0.6.1
%define         _icons_ver 0.7

Summary:	KDE theme - %{_theme}
Summary(pl):	Motyw KDE - %{_theme}
Name:		kde-theme-%{_theme}
Version:	%{_theme_ver}
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/5962-%{_theme}style-%{version}.tar.bz2
# Source0-md5:	eb8198b851621ae173f16e18cb7a7403
Source1:	slickerwallpaper.png
Source2:	http://slicker.sourceforge.net/%{_theme}icons-%{_icons_ver}.tar.bz2
# Source2-md5:	98a87759a5ac58621c1e20a8c3ef0f30
Source3:	http://www.kde-look.org/content/files/9399-myreinhart.kcsrc
# Source3-md5:	9df54d0b9137e59bea3339ee096e77d5
Source4:	http://www.kde-look.org/content/files/7021-slickersplash-0.1.tar.bz2
# Source4-md5:	f609df4c9fe6a0fa08d1320efbb168e9
Source5:	http://www.kde-look.org/content/files/9411-reinhardt.kcsrc
# Source5-md5:	15f86c7f4b05d37532e2b812dd234b56
URL:		http://www.kde-look.org/content/show.php?content=5962
# Also: http://www.kde-look.org/content/show.php?content=5993
# Also: http://www.kde-look.org/content/show.php?content=6153
# Also: http://www.kde-look.org/content/show.php?content=9399
# Also: http://www.kde-look.org/content/show.php?content=7021
# Also: http://www.kde-look.org/content/show.php?content=9411

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        %{_docdir}/kde/HTML

%description
%{_theme} is a slicker theme that was designed to look nice with
slicker. To developer's surprise, this style looks good even without
slicker.

%description -l pl
%{_theme} to motyw stworzony by wspó³gra³ z aplikacj± slicker. Ku
zaskoczeniu twórców, styl ten jednak okaza³ siê piêknie wygl±daæ nawet
bez slickera.

%package -n kde-style-%{_theme}
Summary:	KDE style - %{_theme}
Summary(pl):	Styl do KDE - %{_theme}
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_theme}
%{_theme} is a slicker style that was designed to look nice with
slicker. To developer's surprise, this style looks good even without
slicker.

%description -n kde-style-%{_theme} -l pl
%{_theme} to styl stworzony by wspó³gra³ z aplikacj± slicker. Ku
zaskoczeniu twórców, styl ten jednak okaza³ siê piêknie wygl±daæ nawet
bez slickera.

%package -n kde-icons-%{_theme}
Summary:	KDE style - %{_theme}
Summary(pl):	Styl do KDE - %{_theme}
Group:		Themes
Requires:	kdelibs

%description -n kde-icons-%{_theme}
%{_theme} is a slicker icons theme that was designed to look nice with
slicker style.

%description -n kde-icons-%{_theme} -l pl
%{_theme} to motyw ikon stworzony by wspó³gra³ ze stylem slicker.

%package -n kde-colorscheme-%{_theme}
Summary:        Color scheme for KDE style - %{_theme}
Summary(pl):    Schemat kolorów do stylu KDE - %{_theme}
Group:          Themes
Requires:       kdebase-core

%description -n kde-colorscheme-%{_theme}
Color scheme for KDE style - %{_theme}

%description -n kde-colorscheme-%{_theme} -l pl
Schemat kolorów do stylu KDE - %{_theme}


%package -n kde-wallpaper-%{_theme}
Summary:	KDE wallpaper - %{_theme}
Summary(pl):	Tapeta do KDE - %{_theme}
Group:		Themes
# Contains /usr/share/wallpapers
Requires:	kdebase

%description -n kde-wallpaper-%{_theme}
A wallpaper to go with KDE slicker style.

%description -n kde-wallpaper-%{_theme} -l pl
Tapeta pasuj±ca do stylu KDE slicker.

%package -n kde-splashplugin-%{_theme}
Summary:        ksplash plugin %{_theme}
Summary(pl):    Wtyczka ksplash %{_theme}
Group:          X11/Amusements
Requires:       %{name}-desktop = %{epoch}:%{version}-%{release}

%description -n kde-splashplugin-%{_theme}
ksplash plugin %{_theme}

%description -n kde-splashplugin-%{_theme} -l pl
Wtyczka ksplash %{_theme}


%prep
%setup -q -n %{_theme}style-%{version}

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure

%{__make}

mkdir icons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes
install -d $RPM_BUILD_ROOT%{_datadir}/wallpapers
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/wallpapers

%{__tar} xfj  %{SOURCE2} -C $RPM_BUILD_ROOT%{_iconsdir}

install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes/
rm -rf tmp
mkdir tmp
%{__tar} xfj  %{SOURCE4} -C ./tmp
%{__tar} xfj ./tmp/slickersplash-0.1/Slicker.tar.bz2 -C $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/
cp -f ./tmp/slickersplash-0.1/splash.png  $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/Slicker/
cp -f ./tmp/slickersplash-0.1/login_bg.jpg $RPM_BUILD_ROOT%{_datadir}/wallpapers/


install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes/


%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-style-%{_theme}
%defattr(644,root,root,755)
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/reinhardt.themerc

%files -n kde-splashplugin-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/

%files -n kde-colorscheme-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.*

%files -n kde-wallpaper-%{_theme}
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*

%files -n kde-icons-%{_theme}
%defattr(644,root,root,755)
%{_iconsdir}/
