#include <vector>
#include <string>

namespace blah = std::rel_ops;
namespace Test
{
    typedef std::vector<int> intvector;
    typedef std::vector<std::string> stringvector;
    class Class1
    {
        enum
        {
            E1,
            E2,
            E3
        };
    };
    void Function1();
    int Field1;

    namespace Test2
    {
        namespace Test3
        {
            class T3Class
            {
                public:
                    static int t3Member;
            };
        }
    }
}
namespace a = Test;
namespace b = a::Test2;
namespace c = b::Test3;
namespace d = Test::Test2;
namespace e = Test::Test2::Test3;
