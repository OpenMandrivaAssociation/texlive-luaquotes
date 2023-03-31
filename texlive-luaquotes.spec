Name:		texlive-luaquotes
Version:	65255
Release:	2
Summary:	Smart setting of quotation marks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/luaquotes
License:	lppl1.3 cc-by-sa-3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaquotes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaquotes.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package automatically generates quotation marks and
punctuation depending on the selected language.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/luaquotes
%doc %{_texmfdistdir}/doc/lualatex/luaquotes

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
