%global tl_name dad
%global tl_revision 54191
%global tl_version 1.2

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Simple typesetting system for mixed Arabic/Latin documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/arabic/dad
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dad.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dad.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package allows simple typesetting in Arabic script, intended for
mixed Arabic/Latin script usage in situations where heavy-duty solutions
are discouraged. The system operates with both Unicode and
transliterated input, allowing the user to choose the most appropriate
approach for every situation.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from dad:
Map dad.map
TL_DROPIN_EOF
