Name:		texlive-libertinus-fonts
Version:	72339
Release:	1
Summary:	The Libertinus font family
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/libertinus-fonts
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinus-fonts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinus-fonts.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a fork of the Linux Libertine and Linux Biolinum fonts
that started as an OpenType math companion of the Libertine
font family, but grown as a full fork to address some of the
bugs in the fonts. The family consists of: Libertinus Serif:
forked from Linux Libertine. Libertinus Sans: forked from Linux
Biolinum. Libertinus Mono: forked from Linux Libertine Mono.
Libertinus Math: an OpenType math font for use in OpenType
math-capable applications like LuaTeX, XeTeX or MS Word 2007+.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/opentype/public/libertinus-fonts
%doc %{_texmfdistdir}/doc/fonts/libertinus-fonts

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
