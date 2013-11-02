%global packname  igraphdata
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.1.1
Release:          1
Summary:          A collection of network data sets for the igraph package
Group:            Sciences/Mathematics
License:          CC BY-SA 2.0 + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildArch:        noarch
Requires:         R-core



Requires:         R-igraph0 R-igraph 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

BuildRequires:   R-igraph0 R-igraph 
%description
A small collection of various network data sets, to use with the igraph
package. They also work with the igraph0 package.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
