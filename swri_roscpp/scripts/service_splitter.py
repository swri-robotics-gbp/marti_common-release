# *****************************************************************************
#
# Copyright (c) 2018, Southwest Research Institute (SwRI)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of Southwest Research Institute (SwRI) nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL SOUTHWEST RESEARCH INSTITUTE BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# *****************************************************************************

# This file takes in a service file and splits it into two topics and a header file with useful
# includes and type definitions to match standard services.

# Arguments are:
# 1. Input service file path
# 2. Output Request message file path
# 3. Output Response message file path
# 4. Package name
# 5. Service name
# 6. Output header file path

import sys

data = sys.argv


rf = open(data[1], "rt")
contents = rf.read();
lines = contents.split('---')# split by statement
#split by brackets
rf.close()


oi = open(data[2], "w")
oi.write("marti_common_msgs/ServiceHeader srv_header\n")
oi.write(lines[0])
oi.close()

oi = open(data[3], "w")
oi.write("marti_common_msgs/ServiceHeader srv_header\n")
oi.write(lines[1])
oi.close()

# Write out a wrapper header so we can use and include it like it is a service
# Data 4 has the message name and 5 has the message name
data[5] = data[5].replace(".srv", "")

oi = open(data[6], "w")
name = data[4] + "_" + data[5]
oi.write("// This file is autogenerated, do not modify\n")
oi.write("#ifndef _" + name + "_TOPIC_SERVICE_H_\n")
oi.write("#define _" + name + "_TOPIC_SERVICE_H_\n")

oi.write("#include <" + data[4] + "/" + data[5] + "Response.h>\n")
oi.write("#include <" + data[4] + "/" + data[5] + "Request.h>\n\n")

oi.write("namespace " + data[4] + "{\n")
oi.write("class " + data[5] + "{ public: \n")
oi.write("typedef " + data[5] + "Response Response;\n")
oi.write("typedef " + data[5] + "Request Request;\n")
oi.write("  Request request; Response response;\n")
oi.write("};\n}\n")

oi.write("#endif")
