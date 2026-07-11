%global tl_name dad
%global tl_revision 54191

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Simple typesetting system for mixed Arabic/Latin documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/arabic/dad
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dad.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dad.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows simple typesetting in Arabic script, intended for
mixed Arabic/Latin script usage in situations where heavy-duty solutions
are discouraged. The system operates with both Unicode and
transliterated input, allowing the user to choose the most appropriate
approach for every situation.

