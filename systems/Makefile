TARGET = SystemNode
ARDUINO_LIB_PATH  = $(ARDUINO_DIR)/libraries
ARDUINO_CORE_PATH = ../simulation/mock-teensy/core
ARDUINO_HEADER=WProgram.h
OBJDIR=build

CPPFLAGS += -I$(ARDUINO_CORE_PATH)

REMOVE  = rm -rf
MKDIR   = mkdir -p

# the ino -> o file
# $(OBJDIR)/%.ino.o: %.ino $(COMMON_DEPS) | $(OBJDIR)
#
# C_FILES := $(wildcard *.c)
# CPP_FILES := $(wildcard *.cpp)
# OBJS := $(C_FILES:.c=.o) $(CPP_FILES:.cpp=.o)

$(OBJDIR)/%.o: %.c
	@$(MKDIR) $(dir $@)
	$(CXX) -x c++ -include $(ARDUINO_HEADER) -MMD $(CPPFLAGS) $(CXXFLAGS) $< $(ARDUINO_CORE_PATH)/main.cpp -o $@

all: $(OBJDIR)/SystemNode.o

clean:
	$(REMOVE) build/
