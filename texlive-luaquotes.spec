%global tl_name luaquotes
%global tl_revision 65652

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4.0
Release:	%{tl_revision}.1
Summary:	Smart setting of quotation marks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luaquotes
License:	lppl1.3c cc-by-sa-3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaquotes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaquotes.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package automatically generates quotation marks and punctuation
depending on the selected language.

