Name:           adreno
Version:        1.877.5
%global source_release 1
Release:        %{source_release}%{?dist}
Summary:        Qualcomm Adreno userspace GPU driver libraries

# The payload consists of prebuilt libraries with no corresponding debug source.
%global debug_package %{nil}

License:        Qualcomm.nologin.binaries.license
URL:            https://www.qualcomm.com/processors/adreno
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/gfx-adreno.le.0.0/260922.1/prebuilt_rpm/%{name}-%{version}_%{source_release}.el10.%{_arch}.tar.gz

ExclusiveArch:  aarch64
BuildRequires:  patchelf

%global _udevrulesdir %{_prefix}/lib/udev/rules.d

%description
Prebuilt Qualcomm Adreno userspace libraries for OpenGL ES, EGL, OpenCL, and
Vulkan on Qualcomm Adreno GPUs.

%package common
Summary:        Common Qualcomm Adreno runtime libraries

%description common
Common runtime libraries and environment configuration for the Qualcomm Adreno
userspace driver.

%package gles1
Summary:        Qualcomm Adreno OpenGL ES 1 runtime library
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Requires:       libglvnd-gles%{?_isa}
Requires:       gbm-msm-backend
Requires:       kgsl-dkms

%description gles1
Qualcomm Adreno userspace runtime library for OpenGL ES 1.

%package gles2
Summary:        Qualcomm Adreno OpenGL ES 2 runtime library
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Requires:       libglvnd-gles%{?_isa}
Requires:       gbm-msm-backend
Requires:       kgsl-dkms

%description gles2
Qualcomm Adreno userspace runtime library for OpenGL ES 2.

%package egl1
Summary:        Qualcomm Adreno EGL runtime library
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Requires:       %{name}-gles1%{?_isa} = %{version}-%{release}
Requires:       %{name}-gles2%{?_isa} = %{version}-%{release}
Requires:       libglvnd-egl%{?_isa}
Requires:       gbm-msm-backend
Requires:       kgsl-dkms

%description egl1
Qualcomm Adreno userspace runtime library for EGL.

%package opencl-icd
Summary:        Qualcomm Adreno OpenCL installable client driver
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Requires:       acl
Requires:       ocl-icd%{?_isa}

%description opencl-icd
Qualcomm Adreno OpenCL installable client driver and vendor manifest.

%package opencl-devel
Summary:        Qualcomm Adreno OpenCL vendor extension headers
Requires:       ocl-icd-devel%{?_isa}

%description opencl-devel
Qualcomm Adreno vendor extension header for OpenCL development.

%package vulkan-icd
Summary:        Qualcomm Adreno Vulkan installable client driver
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Requires:       vulkan-loader%{?_isa}
Requires:       gbm-msm-backend
Requires:       kgsl-dkms

%description vulkan-icd
Qualcomm Adreno Vulkan installable client driver and ICD manifest.

%prep
%autosetup -n %{name}-%{version}

%build
# The source archive contains prebuilt ARM64 libraries.

%install
install -d %{buildroot}%{_libdir}/adreno
install -d %{buildroot}%{_includedir}/CL
install -d %{buildroot}%{_sysconfdir}/profile.d
install -d %{buildroot}%{_sysconfdir}/OpenCL/vendors
install -d %{buildroot}%{_datadir}/glvnd/egl_vendor.d
install -d %{buildroot}%{_datadir}/vulkan/icd.d
install -d %{buildroot}%{_udevrulesdir}
install -d %{buildroot}%{_libdir}/environment.d
install -d %{buildroot}%{_libdir}/adreno-common
install -d %{buildroot}%{_libdir}/adreno-vulkan

install -pm 0755 usr/lib64/adreno/libadreno-llvm-glnext.so.1.0.0 %{buildroot}%{_libdir}/adreno/
install -pm 0755 usr/lib64/adreno/libadreno-llvm-qcom.so.1.0.0 %{buildroot}%{_libdir}/adreno/
install -pm 0755 usr/lib64/adreno/libadreno-llvm-qgl.so.1.0.0 %{buildroot}%{_libdir}/adreno/
install -pm 0755 usr/lib64/adreno/libadreno-gsl.so.1.0.0 %{buildroot}%{_libdir}/adreno/
install -pm 0755 usr/lib64/adreno/libadreno-utils.so.1.0.0 %{buildroot}%{_libdir}/adreno/
install -pm 0755 usr/lib64/adreno/libadreno-q3dtools.so.1.0.0 %{buildroot}%{_libdir}/adreno/
install -pm 0755 usr/lib64/adreno/libadreno-q3dtools-esx.so.1.0.0 %{buildroot}%{_libdir}/adreno/
install -pm 0755 usr/lib64/adreno/libadreno-GLESv1-CM.so.1.0.0 %{buildroot}%{_libdir}/adreno/
install -pm 0755 usr/lib64/adreno/libadreno-GLESv2.so.2.0.0 %{buildroot}%{_libdir}/adreno/
install -pm 0755 usr/lib64/adreno/libadreno-EGL.so.1.0.0 %{buildroot}%{_libdir}/adreno/
install -pm 0755 usr/lib64/adreno/libadreno-eglSubDriverWayland.so.1.0.0 %{buildroot}%{_libdir}/adreno/
install -pm 0755 usr/lib64/adreno/libadreno-eglSubDriverX11.so.1.0.0 %{buildroot}%{_libdir}/adreno/
install -pm 0755 usr/lib64/adreno/libadreno-CB.so.1.0.0 %{buildroot}%{_libdir}/adreno/
install -pm 0755 usr/lib64/adreno/libadreno-OpenCL.so.1.0.0 %{buildroot}%{_libdir}/adreno/
install -pm 0755 usr/lib64/adreno/libadreno-vulkan.so.1.0.0 %{buildroot}%{_libdir}/adreno/

find %{buildroot}%{_libdir}/adreno -maxdepth 1 -type f -name '*.so*' \
    -exec patchelf --set-rpath '$ORIGIN' {} +

ln -s libadreno-llvm-glnext.so.1.0.0 %{buildroot}%{_libdir}/adreno/libadreno-llvm-glnext.so.1
ln -s libadreno-llvm-qcom.so.1.0.0 %{buildroot}%{_libdir}/adreno/libadreno-llvm-qcom.so.1
ln -s libadreno-llvm-qgl.so.1.0.0 %{buildroot}%{_libdir}/adreno/libadreno-llvm-qgl.so.1
ln -s libadreno-gsl.so.1.0.0 %{buildroot}%{_libdir}/adreno/libadreno-gsl.so.1
ln -s libadreno-utils.so.1.0.0 %{buildroot}%{_libdir}/adreno/libadreno-utils.so.1
ln -s libadreno-q3dtools.so.1.0.0 %{buildroot}%{_libdir}/adreno/libadreno-q3dtools.so.1
ln -s libadreno-q3dtools-esx.so.1.0.0 %{buildroot}%{_libdir}/adreno/libadreno-q3dtools-esx.so.1
ln -s libadreno-GLESv1-CM.so.1.0.0 %{buildroot}%{_libdir}/adreno/libadreno-GLESv1-CM.so.1
ln -s libadreno-GLESv2.so.2.0.0 %{buildroot}%{_libdir}/adreno/libadreno-GLESv2.so.2
ln -s libadreno-EGL.so.1.0.0 %{buildroot}%{_libdir}/adreno/libadreno-EGL.so.1
ln -s libadreno-eglSubDriverWayland.so.1.0.0 %{buildroot}%{_libdir}/adreno/libadreno-eglSubDriverWayland.so.1
ln -s libadreno-eglSubDriverX11.so.1.0.0 %{buildroot}%{_libdir}/adreno/libadreno-eglSubDriverX11.so.1
ln -s libadreno-CB.so.1.0.0 %{buildroot}%{_libdir}/adreno/libadreno-CB.so.1
ln -s libadreno-OpenCL.so.1.0.0 %{buildroot}%{_libdir}/adreno/libadreno-OpenCL.so.1
ln -s libadreno-vulkan.so.1.0.0 %{buildroot}%{_libdir}/adreno/libadreno-vulkan.so.1
ln -s libadreno-CB.so.1 %{buildroot}%{_libdir}/adreno/libadreno-CB.so
ln -s libadreno-OpenCL.so.1 %{buildroot}%{_libdir}/adreno/libadreno-OpenCL.so

install -pm 0644 usr/include/CL/cl_ext_qcom.h %{buildroot}%{_includedir}/CL/
install -pm 0755 usr/lib64/adreno-common/adreno-common-vars.sh %{buildroot}%{_libdir}/adreno-common/
install -pm 0755 usr/lib64/adreno-vulkan/adreno-vulkan-vars.sh %{buildroot}%{_libdir}/adreno-vulkan/
install -pm 0755 etc/profile.d/adreno-common-profile.sh %{buildroot}%{_sysconfdir}/profile.d/
install -pm 0755 etc/profile.d/adreno-vulkan-profile.sh %{buildroot}%{_sysconfdir}/profile.d/
install -pm 0644 usr/lib64/environment.d/50-qpa-platform.conf %{buildroot}%{_libdir}/environment.d/
install -pm 0644 usr/lib64/environment.d/10-adreno-vulkan.conf %{buildroot}%{_libdir}/environment.d/
install -pm 0644 usr/share/glvnd/egl_vendor.d/10_adreno.json %{buildroot}%{_datadir}/glvnd/egl_vendor.d/
install -pm 0644 usr/share/vulkan/icd.d/adrenovk.json %{buildroot}%{_datadir}/vulkan/icd.d/
install -pm 0644 etc/OpenCL/vendors/adrenocl.icd %{buildroot}%{_sysconfdir}/OpenCL/vendors/
install -pm 0644 usr/lib/udev/rules.d/60-adreno-opencl-icd.rules %{buildroot}%{_udevrulesdir}/

for package in common gles1 gles2 egl1 opencl-icd opencl-devel vulkan-icd; do
    install -Dpm 0644 usr/share/licenses/%{name}-${package}/LICENSE %{buildroot}%{_licensedir}/%{name}-${package}/LICENSE
    install -Dpm 0644 usr/share/doc/%{name}-${package}/NOTICE %{buildroot}%{_docdir}/%{name}-${package}/NOTICE
done

%files common
%license %{_licensedir}/%{name}-common/LICENSE
%doc %{_docdir}/%{name}-common/NOTICE
%dir %{_libdir}/adreno
%{_libdir}/adreno/libadreno-llvm-glnext.so.1*
%{_libdir}/adreno/libadreno-llvm-qcom.so.1*
%{_libdir}/adreno/libadreno-llvm-qgl.so.1*
%{_libdir}/adreno/libadreno-gsl.so.1*
%{_libdir}/adreno/libadreno-utils.so.1*
%{_libdir}/adreno/libadreno-q3dtools.so.1*
%{_libdir}/adreno/libadreno-q3dtools-esx.so.1*
%{_libdir}/environment.d/50-qpa-platform.conf
%{_libdir}/adreno-common/adreno-common-vars.sh
%config(noreplace) %{_sysconfdir}/profile.d/adreno-common-profile.sh

%files gles1
%license %{_licensedir}/%{name}-gles1/LICENSE
%doc %{_docdir}/%{name}-gles1/NOTICE
%{_libdir}/adreno/libadreno-GLESv1-CM.so.1*

%files gles2
%license %{_licensedir}/%{name}-gles2/LICENSE
%doc %{_docdir}/%{name}-gles2/NOTICE
%{_libdir}/adreno/libadreno-GLESv2.so.2*

%files egl1
%license %{_licensedir}/%{name}-egl1/LICENSE
%doc %{_docdir}/%{name}-egl1/NOTICE
%{_libdir}/adreno/libadreno-EGL.so.1*
%{_libdir}/adreno/libadreno-eglSubDriverWayland.so.1*
%{_libdir}/adreno/libadreno-eglSubDriverX11.so.1*
%{_datadir}/glvnd/egl_vendor.d/10_adreno.json

%files opencl-icd
%license %{_licensedir}/%{name}-opencl-icd/LICENSE
%doc %{_docdir}/%{name}-opencl-icd/NOTICE
%{_libdir}/adreno/libadreno-CB.so.1*
%{_libdir}/adreno/libadreno-OpenCL.so.1*
%{_udevrulesdir}/60-adreno-opencl-icd.rules
%config(noreplace) %{_sysconfdir}/OpenCL/vendors/adrenocl.icd

%files opencl-devel
%license %{_licensedir}/%{name}-opencl-devel/LICENSE
%doc %{_docdir}/%{name}-opencl-devel/NOTICE
%{_includedir}/CL/cl_ext_qcom.h
%{_libdir}/adreno/libadreno-CB.so
%{_libdir}/adreno/libadreno-OpenCL.so

%files vulkan-icd
%license %{_licensedir}/%{name}-vulkan-icd/LICENSE
%doc %{_docdir}/%{name}-vulkan-icd/NOTICE
%{_libdir}/adreno/libadreno-vulkan.so.1*
%{_libdir}/environment.d/10-adreno-vulkan.conf
%{_libdir}/adreno-vulkan/adreno-vulkan-vars.sh
%config(noreplace) %{_sysconfdir}/profile.d/adreno-vulkan-profile.sh
%{_datadir}/vulkan/icd.d/adrenovk.json

%changelog
* Wed Sep 09 2026 Maintainers.pkg-rpm-adreno <Maintainers.pkg-rpm-adreno@qualcomm.com> - 1.877.5-1
- Package Qualcomm Adreno 1.877.5 prebuilt ARM64 libraries.
