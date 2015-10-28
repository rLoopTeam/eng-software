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
$(OBJDIR)/%.o: %.c
	@$(MKDIR) $(dir $@)
	$(CXX) -x c++ -include $(ARDUINO_HEADER) -MMD $(CPPFLAGS) $(CXXFLAGS) $< -o $@

all: $(OBJDIR)/SystemNode.o

clean:
	$(REMOVE) build/
