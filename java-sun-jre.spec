Summary:	Sun JRE (Java Runtime Environment) for Linux
Summary(pl):	Sun JRE - �rodowisko uruchomieniowe Javy dla Linuksa
Name:		java-sun-jre
Version:	1.4.2_12
Release:	0.1
License:	restricted, non-distributable
Group:		Development/Languages/Java
# download through forms from http://java.sun.com/j2se/1.4.2/download.html
Source0:	j2re-1_4_2_12-linux-i586.bin
# NoSource0-md5: 1df6655d341c736d8e3845d920612420
NoSource:	0
Patch0:		%{name}-ControlPanel-fix.patch
URL:		http://java.sun.com/linux/
BuildRequires:	rpm-build >= 4.3-0.20030610.21
BuildRequires:	unzip
Requires:	XFree86-libs
Requires:	java-jre-tools
Provides:	java1.4
Provides:	jre = %{version}
Provides:	j2re = %{version}
Provides:	java
Provides:	javaws = %{version}
Provides:	jndi = %{version}
Provides:	jndi-ldap = %{version}
Provides:	jndi-cos = %{version}
Provides:	jndi-rmi = %{version}
Provides:	jndi-dns = %{version}
Provides:	jaas = %{version}
Provides:	jsse = %{version}
Provides:	jce = %{version}
Provides:	jdbc-stdext = 3.0
Provides:	jdbc-stdext = %{version}
Obsoletes:	jre
Obsoletes:	java-blackdown-jre
Obsoletes:	jndi
Obsoletes:	jndi-provider-ldap
Obsoletes:	jndi-provider-cosnaming
Obsoletes:	jndi-provider-rmiregistry
Obsoletes:	jndi-provider-dns
Obsoletes:	jaas
Obsoletes:	jsse
Obsoletes:	jce
Obsoletes:	jdbc-stdext
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		javasun		java-sun
%define		javadir		%{_libdir}/java
%define		jredir		%{_libdir}/java/jre
%define		_javalibdir	%{_datadir}/java
%define		netscape4dir	/usr/lib/netscape
%define		mozilladir	/usr/lib/mozilla

# rpm doesn't like strange version definitions provided by Sun's libs
%define		_noautoprov	'\\.\\./.*' '/usr/re/.*'
# these with SUNWprivate.* are found as required, but not provided
# the rest is because -jdbc wants unixODBC-devel(?)
%define		_noautoreq	'libjava.so(SUNWprivate_1.1)' 'libnet.so(SUNWprivate_1.1)' 'libverify.so(SUNWprivate_1.1)' libodbcinst.so libodbc.so
# don't depend on other JRE/JDK installed on build host
%define		_noautoreqdep	libjava.so libjvm.so

%description
Java Runtime Environment for Linux.

%description -l pl
�rodowisko uruchomieniowe Javy dla Linuksa.

%package jdbc
Summary:	JDBC files for Sun Java
Summary(pl):	Pliki JDBC dla Javy Suna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libodbc.so.1
Requires:	libodbcinst.so.1

%description jdbc
This package contains JDBC files for Sun Java.

%description jdbc -l pl
Ten pakiet zawiera pliki JDBC dla Javy Suna.

%package alsa
Summary:	JRE module for ALSA sound support
Summary(pl):	Modu� JRE do obs�ugi d�wi�ku poprzez ALSA
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description alsa
JRE module for ALSA sound support.

%description alsa -l pl
Modu� JRE do obs�ugi d�wi�ku poprzez ALSA.

%package tools
Summary:	Shared Java tools
Summary(pl):	Wsp�dzielone narz�dzia Javy
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Provides:	java-jre-tools

%description tools
This package contains tools that are common for every Java(TM)
implementation, such as rmic.

%description tools -l pl
Pakiet ten zawiera narz�dzia wsp�lne dla ka�dej implementacji
Javy(TM), takie jak rmic.

%package -n netscape4-plugin-%{javasun}
Summary:	Netscape 4.x Java plugin
Summary(pl):	Wtyczka Javy do Netscape 4.x
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	netscape-common >= 4.0
Obsoletes:	blackdown-java-sdk-netscape4-plugin
Obsoletes:	netscape4-plugin-java-blackdown
Obsoletes:	java-sun-nn4-plugin
Obsoletes:	jre-netscape4-plugin

%description -n netscape4-plugin-%{javasun}
Java plugin for Netscape 4.x.

%description -n netscape4-plugin-%{javasun} -l pl
Wtyczka z obs�ug� Javy dla Netscape 4.x.

%package -n mozilla-plugin-gcc2-%{javasun}
Summary:	Mozilla Java plugin
Summary(pl):	Wtyczka Javy do Mozilli
Group:		Development/Languages/Java
Requires:	mozilla-embedded
Requires:	jre = %{version}
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	java-sun-moz-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-java-blackdown
Obsoletes:	mozilla-plugin-java-sun
Obsoletes:	mozilla-plugin-gcc32-%{name}

%description -n mozilla-plugin-gcc2-%{javasun}
Java plugin for Mozilla compiled using gcc 2.9x.

%description -n mozilla-plugin-gcc2-%{javasun} -l pl
Wtyczka z obs�ug� Javy dla Mozilli skompilowana przy u�yciu gcc 2.9x.

%package -n mozilla-plugin-gcc32-%{javasun}
Summary:	Mozilla Java plugin
Summary(pl):	Wtyczka Javy do Mozilli
Group:		Development/Languages/Java
Requires:	mozilla-embedded
Requires:	jre = %{version}
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	java-sun-moz-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-java-blackdown
Obsoletes:	mozilla-plugin-java-sun
Obsoletes:	mozilla-plugin-gcc2-%{javasun}

%description -n mozilla-plugin-gcc32-%{javasun}
Java plugin for Mozilla compiled using gcc 3.2.

%description -n mozilla-plugin-gcc32-%{javasun} -l pl
Wtyczka z obs�ug� Javy dla Mozilli skompilowana przy u�yciu gcc 3.2.

%prep
%setup -q -T -c -n j2re%{version}
cd ..
export MORE=10000
sh %{SOURCE0} <<EOF
yes
EOF
cd j2re%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{jredir},%{_javalibdir},%{_bindir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_mandir}/{,ja/}man1

cp -rf bin lib $RPM_BUILD_ROOT%{javadir}
install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install man/ja/man1/* $RPM_BUILD_ROOT%{_mandir}/ja/man1

mv -f lib/i386/client/Xusage.txt Xusage.client
mv -f lib/i386/server/Xusage.txt Xusage.server
mv -f lib/*.txt .
mv lib/font.properties{,.orig}
mv lib/font.properties{.Redhat6.1,}

cp -rf {bin,lib} $RPM_BUILD_ROOT%{jredir}

# conflict with heimdal
for i in kinit klist ; do
	ln -sf %{jredir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/j$i
	mv -f $RPM_BUILD_ROOT%{_mandir}/man1/${i}.1 $RPM_BUILD_ROOT%{_mandir}/man1/j${i}.1
	mv -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/${i}.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1/j${i}.1
done

for i in ControlPanel java java_vm keytool ktab orbd policytool \
	rmid rmiregistry servertool tnameserv ; do
	ln -sf %{jredir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

for i in HtmlConverter appletviewer extcheck idlj jar jarsigner java-rmi.cgi \
         javac javadoc javah javap jdb native2ascii rmic serialver ; do
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

rm -f $RPM_BUILD_ROOT%{javadir}/bin/java
ln -sf %{jredir}/bin/java $RPM_BUILD_ROOT%{javadir}/bin/java

install -d $RPM_BUILD_ROOT%{netscape4dir}/{plugins,java/classes}
install plugin/i386/ns4/libjavaplugin.so $RPM_BUILD_ROOT%{netscape4dir}/plugins
for i in javaplugin rt sunrsasign ; do
	ln -sf %{jredir}/lib/$i.jar $RPM_BUILD_ROOT%{netscape4dir}/java/classes
done

install -d $RPM_BUILD_ROOT{%{mozilladir}/plugins,%{jredir}/plugin/i386/{ns610,ns610-gcc32}}
install plugin/i386/ns610/libjavaplugin_oji.so \
	$RPM_BUILD_ROOT%{jredir}/plugin/i386/ns610
ln -sf %{jredir}/plugin/i386/ns610/libjavaplugin_oji.so \
	$RPM_BUILD_ROOT%{mozilladir}/plugins
install plugin/i386/ns610-gcc32/libjavaplugin_oji.so \
	$RPM_BUILD_ROOT%{jredir}/plugin/i386/ns610-gcc32
ln -sf %{jredir}/plugin/i386/ns610-gcc32/libjavaplugin_oji.so \
	$RPM_BUILD_ROOT%{mozilladir}/plugins/libjavaplugin_oji-gcc32.so

# these binaries are in %{jredir}/bin - not needed in %{javadir}/bin?
rm -f $RPM_BUILD_ROOT%{javadir}/bin/{ControlPanel,keytool,kinit,klist,ktab,orbd,policytool,rmid,rmiregistry,servertool,tnameserv}

ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{_javalibdir}/jsse.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{_javalibdir}/jcert.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{_javalibdir}/jnet.jar
ln -sf %{jredir}/lib/jce.jar $RPM_BUILD_ROOT%{_javalibdir}/jce.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javalibdir}/jndi.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javalibdir}/jndi-ldap.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javalibdir}/jndi-cos.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javalibdir}/jndi-rmi.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javalibdir}/jaas.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javalibdir}/jdbc-stdext.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javalibdir}/jdbc-stdext-3.0.jar

install -d $RPM_BUILD_ROOT%{jredir}/javaws
cp -a javaws/* $RPM_BUILD_ROOT%{jredir}/javaws
perl -p -i -e 's#javaws\.cfg\.jre\.0\.path=.*#javaws\.cfg\.jre\.0\.path=%{jredir}/bin/java#' $RPM_BUILD_ROOT%{jredir}/javaws/javaws.cfg
ln -sf %{jredir}/javaws/javaws.jar $RPM_BUILD_ROOT%{_javalibdir}/javaws.jar
ln -sf %{jredir}/javaws/javaws-l10n.jar $RPM_BUILD_ROOT%{_javalibdir}/javaws-l10n.jar

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -L %{jredir} ]; then
	rm -f %{jredir}
fi
if [ -L %{javadir} ]; then
	rm -f %{javadir}
fi

%files
%defattr(644,root,root,755)
%doc {CHANGES,COPYRIGHT,LICENSE,README,Xusage*,*.txt}
%doc Welcome.html ControlPanel.html
%attr(755,root,root) %{_bindir}/ControlPanel
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/java_vm
%attr(755,root,root) %{_bindir}/keytool
%attr(755,root,root) %{_bindir}/jkinit
%attr(755,root,root) %{_bindir}/jklist
%attr(755,root,root) %{_bindir}/ktab
%attr(755,root,root) %{_bindir}/orbd
%attr(755,root,root) %{_bindir}/policytool
%attr(755,root,root) %{_bindir}/rmid
%attr(755,root,root) %{_bindir}/servertool
%attr(755,root,root) %{_bindir}/tnameserv
%dir %{javadir}
%dir %{javadir}/bin
%attr(755,root,root) %{javadir}/bin/java
%dir %{jredir}
%dir %{jredir}/bin
%attr(755,root,root) %{jredir}/bin/ControlPanel
%attr(755,root,root) %{jredir}/bin/java
%attr(755,root,root) %{jredir}/bin/java_vm
%attr(755,root,root) %{jredir}/bin/keytool
%attr(755,root,root) %{jredir}/bin/kinit
%attr(755,root,root) %{jredir}/bin/klist
%attr(755,root,root) %{jredir}/bin/ktab
%attr(755,root,root) %{jredir}/bin/orbd
%attr(755,root,root) %{jredir}/bin/policytool
%attr(755,root,root) %{jredir}/bin/rmid
%attr(755,root,root) %{jredir}/bin/servertool
%attr(755,root,root) %{jredir}/bin/tnameserv
%dir %{jredir}/lib
%{jredir}/lib/applet
%{jredir}/lib/audio
%{jredir}/lib/cmm
%{jredir}/lib/ext
%{jredir}/lib/fonts
%attr(755,root,root) %{jredir}/lib/i386/client
%attr(755,root,root) %{jredir}/lib/i386/native_threads
%attr(755,root,root) %{jredir}/lib/i386/server
%{jredir}/lib/i386/jvm.cfg
%attr(755,root,root) %{jredir}/lib/i386/awt_robot
%attr(755,root,root) %{jredir}/lib/i386/lib[acdfhijmnrvz]*.so
%exclude %{jredir}/lib/i386/libjsoundalsa.so
%{jredir}/lib/im
%{jredir}/lib/images
%dir %{jredir}/lib/security
%{jredir}/lib/security/*.*
%verify(not md5 mtime size) %config(noreplace) %{jredir}/lib/security/cacerts
%{jredir}/lib/zi
%{jredir}/lib/*.jar
%{jredir}/lib/*.properties
#%%{jredir}/lib/*.cfg
#%%{jredir}/lib/tzmappings
%lang(ja) %{jredir}/lib/*.properties.ja
##%lang(zh) %{jredir}/lib/*.properties.zh
%dir %{jredir}/plugin
%dir %{jredir}/plugin/i386
%dir %{_javalibdir}
%{_javalibdir}/jaas.jar
%{_javalibdir}/javaws*.jar
%{_javalibdir}/jce.jar
%{_javalibdir}/jcert.jar
%{_javalibdir}/jdbc-stdext*.jar
%{_javalibdir}/jndi*.jar
%{_javalibdir}/jnet.jar
%{_javalibdir}/jsse.jar
%{_mandir}/man1/java.1*
%{_mandir}/man1/javaws.1*
%{_mandir}/man1/keytool.1*
%{_mandir}/man1/jkinit.1*
%{_mandir}/man1/jklist.1*
%{_mandir}/man1/ktab.1*
%{_mandir}/man1/orbd.1*
%{_mandir}/man1/policytool.1*
%{_mandir}/man1/rmid.1*
%{_mandir}/man1/servertool.1*
%{_mandir}/man1/tnameserv.1*
%lang(ja) %{_mandir}/ja/man1/java.1*
%lang(ja) %{_mandir}/ja/man1/javaws.1*
%lang(ja) %{_mandir}/ja/man1/keytool.1*
%lang(ja) %{_mandir}/ja/man1/jkinit.1*
%lang(ja) %{_mandir}/ja/man1/jklist.1*
%lang(ja) %{_mandir}/ja/man1/ktab.1*
%lang(ja) %{_mandir}/ja/man1/orbd.1*
%lang(ja) %{_mandir}/ja/man1/policytool.1*
%lang(ja) %{_mandir}/ja/man1/rmid.1*
%lang(ja) %{_mandir}/ja/man1/servertool.1*
%lang(ja) %{_mandir}/ja/man1/tnameserv.1*
%dir %{jredir}/javaws
%{jredir}/javaws/resources
%attr(755,root,root) %{jredir}/javaws/javaws
%attr(755,root,root) %{jredir}/javaws/javawsbin
%{jredir}/javaws/cacerts
%{jredir}/javaws/*.gif
%{jredir}/javaws/*.jar
%{jredir}/javaws/*.policy
%{jredir}/javaws/*.html


%files jdbc
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/lib/i386/libJdbcOdbc.so


%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/lib/i386/libjsoundalsa.so

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/bin/rmiregistry
%{_mandir}/man1/rmiregistry.1*
%lang(ja) %{_mandir}/ja/man1/rmiregistry.1*

%files -n netscape4-plugin-%{javasun}
%defattr(644,root,root,755)
%attr(755,root,root) %{netscape4dir}/plugins/libjavaplugin.so
%{netscape4dir}/java/classes/*
%dir %{jredir}/lib/locale
%lang(de) %{jredir}/lib/locale/de
%lang(es) %{jredir}/lib/locale/es
%lang(fr) %{jredir}/lib/locale/fr
%lang(it) %{jredir}/lib/locale/it
%lang(ja) %{jredir}/lib/locale/ja
%lang(ko) %{jredir}/lib/locale/ko
%lang(ko) %{jredir}/lib/locale/ko.UTF-8
%lang(sv) %{jredir}/lib/locale/sv
%lang(zh_CN) %{jredir}/lib/locale/zh
%lang(zh_CN) %{jredir}/lib/locale/zh.GBK
%lang(zh_TW) %{jredir}/lib/locale/zh_TW
%lang(zh_TW) %{jredir}/lib/locale/zh_TW.BIG5

%files -n mozilla-plugin-gcc2-%{javasun}
%defattr(644,root,root,755)
%dir %{jredir}/plugin/i386/ns610
%attr(755,root,root) %{jredir}/plugin/i386/ns610/libjavaplugin_oji.so
%attr(755,root,root) %{mozilladir}/plugins/libjavaplugin_oji.so

%files -n mozilla-plugin-gcc32-%{javasun}
%defattr(644,root,root,755)
%dir %{jredir}/plugin/i386/ns610-gcc32
%attr(755,root,root) %{jredir}/plugin/i386/ns610-gcc32/libjavaplugin_oji.so
%attr(755,root,root) %{mozilladir}/plugins/libjavaplugin_oji-gcc32.so
