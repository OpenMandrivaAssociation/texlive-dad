Name:		texlive-dad
Version:	54191
Release:	1
Summary:	Simple typesetting system for mixed Arabic/Latin documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dad
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dad.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dad.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows simple typesetting in Arabic script,
intended for mixed Arabic/Latin script usage in situations
where heavy-duty solutions are discouraged. The system operates
with both Unicode and transliterated input, allowing the user
to choose the most appropriate approach for every situation.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/dad
%{_texmfdistdir}/fonts/type1/public/dad
%{_texmfdistdir}/fonts/tfm/public/dad
%{_texmfdistdir}/fonts/ovf/public/dad
%{_texmfdistdir}/fonts/ofm/public/dad
%{_texmfdistdir}/fonts/map/dvips/dad
%{_texmfdistdir}/fonts/afm/public/dad
%doc %{_texmfdistdir}/doc/fonts/dad

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
